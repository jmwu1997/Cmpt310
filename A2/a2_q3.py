import time
from csp import *
from a2_q1 import *
from a2_q2 import *


class CSP(search.Problem):
    """This class describes finite-domain Constraint Satisfaction Problems.
    A CSP is specified by the following inputs:
        variables   A list of variables; each is atomic (e.g. int or string).
        domains     A dict of {var:[possible_value, ...]} entries.
        neighbors   A dict of {var:[var,...]} that for each variable lists
                    the other variables that participate in constraints.
        constraints A function f(A, a, B, b) that returns true if neighbors
                    A, B satisfy the constraint when they have values A=a, B=b

    In the textbook and in most mathematical definitions, the
    constraints are specified as explicit pairs of allowable values,
    but the formulation here is easier to express and more compact for
    most cases (for example, the n-Queens problem can be represented
    in O(n) space using this notation, instead of O(n^4) for the
    explicit representation). In terms of describing the CSP as a
    problem, that's all there is.

    However, the class also supports data structures and methods that help you
    solve CSPs by calling a search function on the CSP. Methods and slots are
    as follows, where the argument 'a' represents an assignment, which is a
    dict of {var:val} entries:
        assign(var, val, a)     Assign a[var] = val; do other bookkeeping
        unassign(var, a)        Do del a[var], plus other bookkeeping
        nconflicts(var, val, a) Return the number of other variables that
                                conflict with var=val
        curr_domains[var]       Slot: remaining consistent values for var
                                Used by constraint propagation routines.
    The following methods are used only by graph_search and tree_search:
        actions(state)          Return a list of actions
        result(state, action)   Return a successor of state
        goal_test(state)        Return true if all constraints satisfied
    The following are just for debugging purposes:
        nassigns                Slot: tracks the number of assignments made
        display(a)              Print a human-readable representation
    """

    def __init__(self, variables, domains, neighbors, constraints):
        """Construct a CSP problem. If variables is empty, it becomes domains.keys()."""
        super().__init__(())
        variables = variables or list(domains.keys())
        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        self.constraints = constraints
        self.curr_domains = None
        self.nassigns = 0
        #initial for unassign
        self.unassigns = 0

    def assign(self, var, val, assignment):
        """Add {var: val} to assignment; Discard the old value if any."""
        assignment[var] = val
        self.nassigns += 1

    def unassign(self, var, assignment):
        """Remove {var: val} from assignment.
        DO NOT call this if you are changing a variable to a new value;
        just call assign for that."""
        if var in assignment:
            del assignment[var]
            self.unassigns += 1
        # count number of unassign
            

    def nconflicts(self, var, val, assignment):
        """Return the number of conflicts var=val has with other variables."""

        # Subclasses may implement this more efficiently
        def conflict(var2):
            return var2 in assignment and not self.constraints(var, val, var2, assignment[var2])

        return count(conflict(v) for v in self.neighbors[var])

    def display(self, assignment):
        """Show a human-readable representation of the CSP."""
        # Subclasses can print in a prettier way, or display with a GUI
        print(assignment)

    # These methods are for the tree and graph-search interface:

    def actions(self, state):
        """Return a list of applicable actions: non conflicting
        assignments to an unassigned variable."""
        if len(state) == len(self.variables):
            return []
        else:
            assignment = dict(state)
            var = first([v for v in self.variables if v not in assignment])
            return [(var, val) for val in self.domains[var]
                    if self.nconflicts(var, val, assignment) == 0]

    def result(self, state, action):
        """Perform an action and return the new state."""
        (var, val) = action
        return state + ((var, val),)

    def goal_test(self, state):
        """The goal is to assign all variables, with all constraints satisfied."""
        assignment = dict(state)
        return (len(assignment) == len(self.variables)
                and all(self.nconflicts(variables, assignment[variables], assignment) == 0
                        for variables in self.variables))

    # These are for constraint propagation

    def support_pruning(self):
        """Make sure we can prune values from domains. (We want to pay
        for this only if we use it.)"""
        if self.curr_domains is None:
            self.curr_domains = {v: list(self.domains[v]) for v in self.variables}

    def suppose(self, var, value):
        """Start accumulating inferences from assuming var=value."""
        self.support_pruning()
        removals = [(var, a) for a in self.curr_domains[var] if a != value]
        self.curr_domains[var] = [value]
        return removals

    def prune(self, var, value, removals):
        """Rule out var=value."""
        self.curr_domains[var].remove(value)
        if removals is not None:
            removals.append((var, value))

    def choices(self, var):
        """Return all values for var that aren't currently ruled out."""
        return (self.curr_domains or self.domains)[var]

    def infer_assignment(self):
        """Return the partial assignment implied by the current inferences."""
        self.support_pruning()
        return {v: self.curr_domains[v][0]
                for v in self.variables if 1 == len(self.curr_domains[v])}

    def restore(self, removals):
        """Undo a supposition and all inferences from it."""
        for B, b in removals:
            self.curr_domains[B].append(b)

    # This is for min_conflicts search

    def conflicted_vars(self, current):
        """Return a list of variables in current assignment that are in conflict"""
        return [var for var in self.variables
                if self.nconflicts(var, current[var], current) > 0]

def MapColoringCSP(j, neighbors):
    """Make a CSP for the problem of coloring a map with different colors
    for any two adjacent regions. Arguments are a list of colors, and a
    dict of {region: [neighbor,...]} entries. This dict may also be
    specified as a string of the form defined by parse_neighbors."""

    #create colors according to j
    colors = []
    for i in range(j+1):
        colors.append(i)

    if isinstance(neighbors, str):
        neighbors = parse_neighbors(neighbors)
    return CSP(list(neighbors.keys()), UniversalDict(colors), neighbors, different_values_constraint)

def get_stats(graph):
    #list initial
    team_len=[]
    for i in range(31):
        team_len.append(0)
    #sum up all teams
    for i in range(len(graph)):
        for j in range(len(graph)):
            if i == graph[j]:
                team_len[i] += 1
    #remove empty teams for calculation
    team_number=[i for i in team_len if i != 0]
    print("Length of each teams:",team_number)
    #return (Max, Min, Avgerage)
    return max(team_number),min(team_number),round(sum(team_number)/len(team_number),1)

def solve(graphs):
    assigns= 0
    unassigns = 0
    start_time = time.time()
    #At max 31 colors for 31 teams, one player each color
    for i in range(31):
        #add color and map it
        csp = MapColoringCSP(i,graphs)
        #return True when problem satisfied, which only return false when i = 0
        AC3(csp)
        #print(AC3(csp))
        #change default variable ordering to mrv and value ordering to lcv
        solution = backtracking_search(csp,mrv,lcv,forward_checking)
        #total up unassigned and assigns
        assigns = assigns+csp.nassigns
        unassigns = unassigns+csp.unassigns
        #when result return actual value
        if solution != None and check_teams(graphs,solution):
            elasped_time = time.time()
            #return solution, number of teams, unassigns, assigns,
            return solution, i+1, assigns, unassigns , elasped_time-start_time,


def run_q3():
    #run the interation 5 times and will result in 30 solutions
    for i in range (5):
        print('*******************************')
        print('Iteration :',i+1)
        print('*******************************')
        #graphs initial
        graphs = [rand_graph(0.1, 31), rand_graph(0.2, 31), rand_graph(0.3, 31), 
        rand_graph(0.4, 31), rand_graph(0.5, 31), rand_graph(0.6, 31)]

        #Loop for each graph above
        for i in range(6):
                print('Graph: %s---------------------------------------------------' % (i+1))
                print(graphs[i])
                solution, number_of_teams ,assigns,unassigns,time = solve(graphs[i])
                print('')
                print('Testing Graph %s with p: 0.%s and n = 31' % (i+1,i+1))
                print("Solution:",solution)
                print('')
                print('1: number of teams that the people are divided into: ',number_of_teams)
                print('2: the running time of the solver : ',time)
                print('3: the count of the number of times CSP variables were assigned: ',assigns)
                print('4: the count of the number of times CSP variables were unassigned: ',unassigns)
                print('5: Max, Min, Average number in a team: ',get_stats(solution))
                print('')

run_q3()
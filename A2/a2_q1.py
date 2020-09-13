import random 
"""rand_graph(p, n) that returns a new random graph with 
n nodes numbered 0 to n−1 such that every different pair 
of nodes is connected with probability p. Assume n>1, and 0≤p≤1."""
def rand_graph(p, n):
    graph = {}
    #create empty graph
    for i in range(n):
        graph[i] = []
    
    #loop through all possible nodes
    for j in range(n):
        for k in range(j+1,n):
            random_val = random.uniform(0, 1)
            #print(j,k,random_val)
            #if random is within the probability, connect node
            if (random_val <= p):
                graph[j].append(k)
                graph[k].append(j)

    return graph

# print(rand_graph(0.5, 5))
# print("--------------")
# print(rand_graph(0.1, 10))
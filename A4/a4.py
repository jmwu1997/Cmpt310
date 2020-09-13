#Jia Ming Wu
#A4
#301278354
# returns True if, and only if, string s is a valid variable name
def is_atom(s):
    if not isinstance(s, str):
        return False
    if s == "":
        return False
    return is_letter(s[0]) and all(is_letter(c) or c.isdigit() for c in s[1:])

def is_letter(s):
    return len(s) == 1 and s.lower() in "_abcdefghijklmnopqrstuvwxyz"

def load_text(file,rules):
    try:
        f = open(file, "r")
        Lines = f.readlines()
        append_lines=[]
        for line in Lines:
            for i in range(len(line.split())):
                if i%2==0 and i==0:
                    rules[line.split()[i]]=[]
                elif i%2==0:
                    rules[line.split()[0]].append(line.split()[i])
        return rules
    except:
        #error case
        print("Error: " + file + " is not a valid knowledge base")
        return False
#infer_all followed by sudo code
def infer_all(rules,atoms):
    c = set()
    for key in rules.keys():
        check =  all(item in atoms for item in rules[key])
        if check is True:
            c.add(key)
    return c
#Main
atoms=[]
rules=dict()
tellcount=0
while True:
    #user input
    userinput = input("kb>" )
    #if user input tell
    if userinput.startswith("tell"):
        #error case for tell
        if len(userinput.split())<2:
            print("Error: tell needs at least one atom")
        #normal case for tell
        input_words=userinput.split()
        check_false=True
        for i in range(1,len(input_words)):
            #if word is not atom
            if is_atom(input_words[i])!=True:
                print('Error: '+'"'+input_words[i]+'"'+' is not a valid atom')
                check_false=False
        if check_false==True:
            #for words that are atoms
            for i in range(1,len(input_words)):
                if input_words[i] in atoms:
                    print('atom'+'"'+input_words[i]+'"'+'already known to be true')
                elif is_atom(input_words[i])==True:
                    atoms.append(input_words[i])
                    print('"'+input_words[i]+'"'+" added to KB")
                    tellcount+=1
    #if user input load file
    elif userinput.startswith('load'):
        input_words=userinput.split()
        if len(input_words)==2:
            #load rules successfully
            rules=load_text(input_words[1],rules)
        else:
            #error case when load rules
            print("Error: please enter a valid load file")
    #if user input infer_all
    elif userinput=="infer_all":
        #can not inferall if there are no atoms
        if tellcount==0:
            print("Error: please enter a valid tell atom first")
        #normal case
        else:
            new_inferred=infer_all(rules,atoms)
            #print inferred atoms
            print('  Newly inferred atoms:')
            if not new_inferred:
                print('     <none>')
            else:
                for i in new_inferred:
                    print("   "+i, end=" ")
                print('')
            #print atomes known to be true
            print('  Atoms already known to be true:')
            for i in atoms:
                print("   "+i, end=" ")
            print('')

    #other commands
    else:
        print("Error: unknown command: " + '"'+userinput+'"')


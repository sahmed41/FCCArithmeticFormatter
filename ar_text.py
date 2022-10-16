digs = [[],[],[]]
def arithmetic_arranger(problem):
    for i,pr in enumerate(problem):
        pr = pr.strip()
        longest = max(len(pr.split()[0]), len(pr.split()[2]))
        print(pr.split(), longest)
        if ('+' in pr):
            if (len(pr.split('+')[0]) > len(pr.split('+')[1])):
                digs[0].append("  " + pr.split('+')[0].strip())            
                digs[1].append("+" + ((len(pr.split('+')[0].strip())-len(pr.split('+')[1].strip()) + 1)* " ") + pr.split('+')[1].strip())
                digs[2].append(len("  " + pr.split('+')[0].strip()) * '-')
            else:
                digs[1].append("+ " + pr.split('+')[1].strip())            
                digs[0].append(((len(pr.split('+')[1].strip())-len(pr.split('+')[0].strip()) + 1)* " ") + pr.split('+')[0].strip())
                digs[2].append(len("+ " + pr.split('+')[1].strip()) * '-')

        elif ('-' in pr):
            pr.split('-')[0]
            digs[0].append("  " + pr.split('-')[0].strip())
            digs[1].append("-" + ((4 - len(pr.split('-')[1])) * " ") + pr.split("-")[1].strip())
    
    digs[0][-1] += "\n" 
    digs[1][-1] += "\n" 
            
    exp =""
    for d in digs:
        for n in d:
            if (n == d[-1]):
                exp += n
            else:
                exp += n + "\t"
    exp += len(digs[0]) * "-----\t"
    # print(pr)
    
        
        # for n in d:
        #     if (n == d[-1]):
        #         print(n,end="")
        #     else:
        #         print(n + "\t", end="")
        # print()
    # print(len(digs[0])*"_____\t")
    
# x = "home"
# print("z" in x)
arithmetic_arranger(["3145 + 45", "485 + 1190", "3 + 2", "1 + 2"])
print(digs)
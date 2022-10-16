def arithmetic_arranger(problem, expect_answer=False):
    # Checking the number of problems and returns and error if it is more than 5
    if len(problem) > 5:
        return "Error: Too many problems."
        

    digs = [[],[],[],[],[]] # The list that will contain the operation lines as arrays
    for i,pr in enumerate(problem):
        pr = pr.strip()
        longest = max(len(pr.split()[0]), len(pr.split()[2]))
        
        if (longest > len(pr.split()[0])):            
            digs[0].append((longest - len(pr.split()[0]) + 2) * " " + pr.split()[0])
        else:
            digs[0].append("  " + pr.split()[0])

        if (longest > len(pr.split()[2])):            
            digs[2].append((longest - len(pr.split()[2]) + 1) * " " + pr.split()[2])
        else:
            digs[2].append(" " + pr.split()[2])
        digs[1].append(pr.split()[1])
        digs[3].append((longest + 2) * "-")

    # Checks if there are more than four digits to both sides of the operator. If so the program throws an error
    for k,d in enumerate(digs):
        if k == 1 or k >= 3:
            continue
        for n in d:
            n = n.strip()
            if len(n.strip()) > 4:
                return "Error: Numbers cannot be more than four digits."
            elif not(n.isnumeric()):
                return "Error: Numbers must only contain digits."

    if expect_answer: # Adding answers if True is passed as second parameter
        for i in range(len(digs[0])):
            ans = str(eval(digs[0][i] + digs[1][i] + digs[2][i]))
            digs[4].append(((len(digs[3][i]) - len(ans)) * " ") + ans)
        
    
    for i,d in enumerate(digs[2]): # combining operator and second operand
        digs[2][i] = digs[1][i] + digs[2][i]
    
    # digs[1] = []   
    # Checks if there are any other operators besides '+' and '-'. If so it throws an error
    for k,o in enumerate(digs[1]):
        if o != '+' and o != '-':
            return "Error: Operator must be '+' or '-'."

    
  
    operation =""
    for k,d in enumerate(digs):
        if k==1:
            continue
        for i,n in enumerate(d):
            if (i == len(d)-1): 
                if expect_answer and k == 4:
                    operation += n
                elif not expect_answer and k == 3:
                    operation += n
                else:
                    operation += n + "\n"
            else:
                operation += n + "    "
    return operation
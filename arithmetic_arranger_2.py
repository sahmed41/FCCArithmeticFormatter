from string import digits
from unicodedata import digit


digs = []
def arithmetic_arranger(problem):
    for i,pr in enumerate(problem):
        if (pr == pr.split('+')[0]):       
            for k,p in enumerate(pr.split('-')):

                if (k > 0):
                    p = "-" + ((4 - len(p)) * " ") + p.strip()
                else:
                    p = ((5 - len(p)) * " ") + p.strip()
                            
                digs.append([k,p])
        else:
                   
            for k,p in enumerate(pr.split('+')): 
                if (k > 0):
                    p = "+" + ((4 - len(p)) * " ") + p.strip()                
                else:
                    p = ((5 - len(p)) * " ") + p.strip()
                             
                digs.append([k,p])
    
    count = 0
    x = 0
    while(count < len(digs)):
        for i,d in enumerate(digs):
                      
            if (d[0] == x):
                print(d[1] + "\t", end="")
        print()
        x += 1
        count += 1
    print(int(len(digs)/2)* "-----\t")

    
    


        # if (p == p.split('+')[0]):
        #     if (i == (len(problem) - 1)):
        #         print(p.split('-')[0].strip())
        #     else:
        #         print(p.split('-')[0].strip() + "\t", end = ' ')

        # else:
        #     if (i == (len(problem) - 1)):
        #         print(p.split('+')[0].strip())
        #     else:
        #         print(p.split('+')[0].strip() + "\t", end = ' ')
        
    # print("\n")

    # for p in problem:
    #     if (p == p.split('+')[0]):
    #         print(p.split('-')[1].strip() + "\t", end = ' ')
    #     else:
    #         print(p.split('+')[1].strip() +  "\t", end = ' ')
    # # print(len(problem))




arithmetic_arranger(["3145-45", "485-90", "3-2", "1 + 2"])

# x = ["345-45", "485-90"]

# print(x[0] == x[0].split('+')[0])
print()
print(digs)



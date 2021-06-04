def find_all_sols(n, operands, op_strings):
    total = find_all_sols_recur(n, operands, op_strings, 0)
    if total == 0:
        print("No solutions.")
    else:
        print("Number of solutions: " + str(total))

#equals curr_total + number of new solutions
def find_all_sols_recur(n, operands, op_strings, curr_total):
    #n: Goal value
    #operands: List of integer operands
        #Math performed on this list
    #op_strings: String form of operands
        #Tracks performed operations
        #Ex. operands = [6, 7] may mean op_strings = ["(3 * 2)", "(2 + 5)"]
    #curr_total: running total of successes

    if len(operands) == 1 and n == operands[0]:
        print(op_strings[0])
        curr_total = curr_total + 1
    else:
        for j in range(len(operands)):
            for i in range(j):
                tempi = operands[i]
                tempj = operands[j]
                strtempi = op_strings[i]
                strtempj = op_strings[j]
                operands[j] = operands[len(operands) - 1] #need only consider operands[:-1], tempj
                op_strings[j] = op_strings[len(op_strings) - 1] #need only consider op_strings[:-1], strtempj

                operands[i] = tempi + tempj
                op_strings[i] = "(" + strtempi + " + " + strtempj + ")"
                curr_total = find_all_sols_recur(n, operands[:-1], op_strings[:-1], curr_total)
                
                operands[i] = tempi - tempj
                op_strings[i] = "(" + strtempi + " - " + strtempj + ")"
                curr_total = find_all_sols_recur(n, operands[:-1], op_strings[:-1], curr_total)

                operands[i] = tempj - tempi
                op_strings[i] = "(" + strtempj + " - " + strtempi + ")"
                curr_total = find_all_sols_recur(n, operands[:-1], op_strings[:-1], curr_total)

                operands[i] = tempi * tempj
                op_strings[i] = "(" + strtempi + " * " + strtempj + ")"
                curr_total = find_all_sols_recur(n, operands[:-1], op_strings[:-1], curr_total)

                if tempj != 0: #prevents division by zero
                    operands[i] = tempi / tempj
                    op_strings[i] = "(" + strtempi + " / " + strtempj + ")"
                    curr_total = find_all_sols_recur(n, operands[:-1], op_strings[:-1], curr_total)

                if tempi != 0: #prevents division by zero
                    operands[i] = tempj / tempi
                    op_strings[i] = "(" + strtempj + " / " + strtempi + ")"
                    curr_total = find_all_sols_recur(n, operands[:-1], op_strings[:-1], curr_total)

                #Method terminated: reset variables
                operands[i] = tempi 
                operands[j] = tempj
                op_strings[i] = strtempi
                op_strings[j] = strtempj
        
    return curr_total

while True: 
    while True:
        N = input("N?   ")
        try:
            N = int(N)
            break
        except:
            print("Please input an integer.")

    while True:
        vals = input("Values? (separate each by a space)     ").split(" ")
        try:
            find_all_sols(N, list(map(int, vals)), vals) 
            break
        except: 
            print("Please input integer values separated by spaces.")

    while True:
        answer = input("Continue? Type Y or N     ")
        if answer in ("Y", "N"):
            break
        print("Invalid input. Try again.")

    if answer == "Y":
        continue
    else:
        print("Program terminated." )
        break



                                
    

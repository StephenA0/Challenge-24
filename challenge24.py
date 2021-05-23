#Maybe do an analysis of whether the cost of repeated sorting of the list is worth the benefit of only analyzing unique solutions. 
#Maybe do this only for the original iteration, or for a certain current list length
#Potential for some mathematical Big-O analysis here

#def unique_candidate(operands, i, j):
    #if operands[i] == operands[j]:
        #return i == 0 or operands[i] > operands[i-1]
    #else:
        #return operands[j] > operands[j-1]
    #return False

def find_all_sols(n, operands, op_strings):
    total = find_all_sols_recur(n, operands, op_strings, 0)
    if total == 0:
        print("No solutions.")
    else:
        print("Number of solutions: " + str(total))

def find_all_sols_recur(n, operands, op_strings, curr_total):
    if(len(operands) == 1) and n == operands[0]:
        print(op_strings[0])
        curr_total = curr_total + 1
    else:
        for j in range(len(operands)):
            for i in range(j):
                #if not unique_candidate(operands, i, j):
                    #continue
                tempi = operands[i]
                tempj = operands[j]
                strtempi = op_strings[i]
                strtempj = op_strings[j]
                operands[j] = operands[len(operands) - 1]
                op_strings[j] = op_strings[len(op_strings) - 1]

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

                if tempj != 0:
                    operands[i] = tempi / tempj
                    op_strings[i] = "(" + strtempi + " / " + strtempj + ")"
                    curr_total = find_all_sols_recur(n, operands[:-1], op_strings[:-1], curr_total)

                if tempi != 0:
                    operands[i] = tempj / tempi
                    op_strings[i] = "(" + strtempj + " / " + strtempi + ")"
                    curr_total = find_all_sols_recur(n, operands[:-1], op_strings[:-1], curr_total)

                operands[i] = tempi
                operands[j] = tempj
                op_strings[i] = strtempi
                op_strings[j] = strtempj
        
    return curr_total

while True: 
    N = input("N?   ")
    vals = input("Values? (separate each by a space)     ").split(" ")
    #vals.sort()
    print(vals)
    print(list(map(int, vals)))
    print(N)
    find_all_sols(N, list(map(int, vals)), vals)   

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

    

                                
    

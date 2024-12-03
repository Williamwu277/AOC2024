# AOC 2024 Day 3

# there are ~18000 characters attempt a more linear solution
line = input()
answer = 0
status = True


for i in range(len(line)-4):

    if not status:
        
        if line[i:i+4] == "do()":

            status = True
    
    else:

        if i < len(line)-7 and line[i:i+7] == "don't()":

            status = False

        elif line[i:i+4] == "mul(": # find the first mul(

            for j in range(i+4, len(line)):

                if line[j] == ',': # find the first , after mul(

                    for k in range(j+1, len(line)):
                        
                        if line[k] == ')': # find the first ) after ,

                            answer += int(line[i+4: j]) * int(line[j+1: k])
                            break
                        
                        elif not line[k].isdigit():

                            break
                    
                    break
                
                elif not line[j].isdigit():

                    break


print(answer)


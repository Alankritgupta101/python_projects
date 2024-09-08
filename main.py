import random
computer = random.choice([1,0,-1])

youstr  = input("select your move: ")

youDict = {"stone": -1, "paper": 0,  "scissor": 1}
you = youDict[youstr]
reversedict = {-1: "stone", 0: "paper",  1: "scissor"}

print(f"you chose :{reversedict[you]}\n computer chose :{reversedict[computer]}")

if(computer == you):
    print("the match is draw")

else:
    if(computer == -1 and you ==0):
        print("you win!")

    elif(computer == -1 and you ==1):
        print("you lose!")

    elif(computer == 1 and you ==-1):   
        print("you win!")

    elif(computer == 1 and you ==0):    
        print("you lose!")

    elif(computer == 0 and you ==1):
        print("you win!")

    elif(computer == 0 and you ==-1):
        print("you lose!")

    else:
        print("something went wrong")


#have fun
        


 

import random
print("\n\nWelcome to the Odd or Even Game\n")
print("Choose  1 for Heads and 2 for Tails \n\n1.Heads\n2.Tails")
chose = int(input("Enter The Heads Or Tails using numbers: "))
print("Tossing......")
desicion = random.choice([1,2])


def batting1():
    global i
    i=0
    while True:
        global num1,comp
        try:
            num1 = int(input("Please Enter the Number less than 10: \n"))
        except Exception as e:
            print(e)
            print("Please Enter the Correct Number")
        comp = int(random.randrange(0,11))
        # print(f"You have inputted {num} ")
        "\n"
        print(f"Computer selected {comp} \n")
        if num1<=10:
            if num1 != comp:
                i = i+num1
                print(f"Your Total Run is {i} \n")
                continue
            else:
                print("You are Out")
                break            
        else:
            print("You inputted Number more than 10")
            continue
    global finalbat
    finalbat = i

def bowling1():
    global i 
    i = 0
    while True:
        global num2,comp
        comp = int(random.randrange(0,11))
        try:
            num2 = int(input("Please Enter the Number less than 10: \n"))
        except Exception as e:
            print(e)
            print("Please Enter the Correct Number")
        # print(f"You have inputted {num} ")
        "\n"
        print(f"Computer selected {comp}\n ")
        if num2<=10:
            if comp != num2:
                i = i+comp 
                if i <= finalbat:
                    print(f"Computer Has Total Scored {i} \n")
                    continue   
                else:
                    global finalbowl
                    finalbowl = i
                    if finalbat>finalbowl:
                        print("You Won the Match")
                        exit()
                    elif finalbat == finalbowl:
                        print("Draw match")
                        exit()
                    elif finalbat<finalbowl:
                        print("You lose the match")
                        exit()
                    else:
                        break
            else:
                print("Because Computer got Out")
                finalbowl = i
                if finalbat>finalbowl:
                    print("You Won the Match")
                    exit()
                elif finalbat == finalbowl:
                    print("Draw match")
                    exit()
                elif finalbat<finalbowl:
                    print("You lose the match")
                    exit()
                else:
                    break

        else:
            print("You have selected Number More than 10")
            continue       
        

def batting2():
    global i
    i=0
    while True:
        global num1,comp
        try:
            num1 = int(input("Please Enter the Number less than 10: \n"))
        except Exception as e:
            print(e)
            print("Please Enter the Correct Number")
        comp = int(random.randrange(0,11))
        # print(f"You have inputted {num} ")
        "\n"
        print(f"Computer selected {comp} \n")
        if num1<=10:
            if num1 != comp:
                i = i+num1
                if i <= finalbowl:
                    print(f"Your Total Run is {i}\n ")
                    continue
                else:
                    global finalbat
                    finalbat = i
                    if finalbat>finalbowl:
                        print("You Won the Match")
                        exit()
                    elif finalbat == finalbowl:
                        print("Draw match")
                        exit()
                    elif finalbat<finalbowl:
                        print("You lose the match")
                        exit()
                    else:   
                        break 
            else:
                print("Because You are Out")    
                finalbat = i
                if finalbat>finalbowl:
                    print("You Won the Match")
                    exit()
                elif finalbat == finalbowl:
                    print("Draw match")
                    exit()
                elif finalbat<finalbowl:
                    print("You lose the match")
                    exit()
                else:   
                    break

        else:
            print("You inputted Number more than 10")
            continue
    

def bowling2():
    global i 
    i = 0
    while True:
        global num2,comp
        comp = int(random.randrange(0,11))
        try:
            num2 = int(input("Please Enter the Number less than 10: \n"))
        except Exception as e:
            print(e)
            print("Please Enter the Correct Number")
        # print(f"You have inputted {num} ")
   
        print(f"Computer selected {comp} \n")
        if num2<=10:
            if comp != num2:
                i = i+comp
                print(f"Computer Has Total Scored {i} \n")
            else:
                print("Congratulations, You have got a wicket.")
                break
        else:
            print("You have selected Number More than 10")
            continue
        global finalbowl
        finalbowl = i

if __name__ == '__main__':
    while True:
        if 1:
            if chose == desicion:
                print("You Won The Toss. Select 1 for Batting and 2 for Bowling \n\n1.Batting\n2.bowling")
                babo = int(input("Plese Enter Your Desicion as Number: "))
                "\n"
                if babo == 1:
                    print("You Are Batting Now")
                    batting1()
                    print(f"Now you Have to Take the wicket of Computer To win before Computer takes {i + 1} runs ")
                    bowling1()
                    
                elif babo == 2:
                    print("You are Bowling First ")
                    bowling2()
                    i2 = i + 1
                    print(f"Now you need to get {i2} runs to win")
                    batting2()
            else:
                print("Computer Won the toss\n")
                bob = random.choice([1,2])        
                if bob ==1:
                    print('Computer choose to Bat First')
                    bowling2()
                    print(f"Now you have to take {finalbowl + 1} runs to win")
                    batting2()
                else:
                    print("Computer have choose to bowl First")
                    batting1()    
                    print(f"Now You want to take wicket of computer before computer gets {finalbat} runs to win")
                    bowling1()

                
        




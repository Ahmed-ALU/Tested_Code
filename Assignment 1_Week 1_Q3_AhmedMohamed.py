def hangman():
    print("Hello Mr. Smart, you are here because you are an ALU student and we are here to test you kknowledge with some questions about ALU. You have ten questions and only six questions to miss while hanging, miss them and you die. ")

# We first define the answers of each question.

    q1 = int(2015)
    q2 = "Fred Swaniker"
    q3 = "Rwanda and Mauritius"
    q4 = int(2) 
    q5 = "Gaidi Faraj"
    q6 =  "Sila Ogidi" 
    q7 = "FabLab" 
    q8 = int(94)
    q9 =int(8) 
    q10 = "Mauritius"
    points = int()
    misses = int(0)
    
    p = str(input("You want to proceed? y/n : "))# ask if he/she want to proceed in the game

    x = int(0)#for controlling the start and the end of the loop


    if p == "y": 
        while x == 0 : #So that the loop continue until we tell her to finish

            print("Q1")
            if q1 == int(input("1. When was ALU founded (2015)? \
                : ")): #We will print every question and get the answers like this 
                points += 1 #we add one point to be stored if he got it right
            else :
                misses += 1 # one pount to be added in the missies if he missed it
                print ("you are a hanging man")
            

            print("Q2")
            if q2 == input("2. Who is the CEO of ALU (Fred Swaniker)? \
                : "):
                points += 1
            else :
                misses += 1
                print ("you are a hanging man")


            print("Q3")
            if q3 == input("3. Where are ALU campuses (Rwanda and Mauritius)? \
                : "):
                points += 1
            else :
                misses += 1
                print ("you are a hanging man")

            print("Q4")
            if q4 == input("4. How many campuses does ALU have (2)? \
                : "):
                points += 1
            else :
                misses += 1
                print ("you are a hanging man")
            
            
            print("Q5")
            if q5 == input("5. What is the name of ALU Rwanda’s Dean (Insert dean’s name)? \
                : "):
                points += 1
            else :
                misses += 1
                print ("you are a hanging man")

            print("Q6")
            if q6 == input("6. Who is in charge of Student Life (Sila Ogidi)? \
                : "):
                points += 1
            else :
                misses += 1
                print ("you are a hanging man")

            while misses < 6: #starting from question 7 and after question 6, we will have the chance to get six \
                #mistakes, so we made this extra while loop in every question from 7 :10 to catch if the mistakes 
                # are 6, so that we decide to continue or kill the man. 

                print("Q7")
                if q7 == input("7. What is the name of our Lab (Insert name here)? \
                    : "):
                    points += 1
                else :
                    misses += 1
                    print ("you are a hanging man")

            else:
                print("Sorry You are Dead...\n")
                print(f"You have missed {misses} questions, YOU ARE A DEAD MAN\n\n")  # a follow up for the second while loop to kill the man
                x = 1 # to finish the loop and go to the else condition


            while misses < 6:

                print("Q8")
                if q8 == input("8. How many students do we have in Year 2 CS(put the number of students)? \
                    : "):
                    points += 1
                else :
                    misses += 1
                    print ("you are a hanging man")

            else:
                print("Sorry You are Dead...\n")
                print(f"You have missed {misses} questions, YOU ARE A DEAD MAN\n\n")
                x = 1

            while misses < 6:

                print("Q9")
                if q9 == input("9. How many degrees does ALU offer (8)? \
                    : "):
                    points += 1
                else :
                    misses += 1
                    print ("you are a hanging man")

            else:
                print("Sorry You are Dead...\n")
                print(f"You have missed {misses} questions, YOU ARE A DEAD MAN\n\n")
                x = 1

            while misses < 6:
                print("Q10")
                if q10 == input("10. Where are the headquarters of ALU (Mauritius)? \
                    : "):
                    points += 1
                else :
                    misses += 1
                    print ("you are a hanging man")
            
            else:
                print("Sorry You are Dead...\n")
                print(f"You have missed {misses} questions, YOU ARE A DEAD MAN\n\n")
                x = 1


            if misses < 6 : # Here we check if he is a dead man or not so that we decide to congratulate or not
                print(f"you made {misses} mistakes and {points} right answers, but your man will live with no honour.")  
        
            elif points == 10 : # if he got all right
                print("CONGRATULATIONS, you passed with no mistakes at all, and you man will live with honour") 

            # else: # If he dies
            #     print("Sorry You are Dead...\n")
            #     print(f"You have missed {misses} questions, YOU ARE A DEAD MAN\n\n")

        else :
            print("Thank you for playing our game, hope you live next time")

            Playagaing = input("You want to play again?  y/n: ")

        if Playagaing == "y": 
            hangman()
        else:
            print('Thank you')
    else :
        print (" Thank you for not choosing us, see you next time when you don't find a game better than us") 
        #Sure I can't do that with a real customer
        


hangman()
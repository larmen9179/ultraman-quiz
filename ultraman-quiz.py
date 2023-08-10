import time

print("Welcome to my Ultraman Quiz!")

start = input("Are you ready to begin? Type 'Yes' or 'No': ")
start = start.lower()

#The initial question if the user wants to take the quiz or not
while start != 'yes':
    if start == 'no':
        print("Ok, well see you later I guess...")
        quit()
    else:
        start = input("What the heck is even that? Please enter in an option like 'Yes' or 'No': ")
        start = start.lower()


print("All right let's go!!")
print("...")

time.sleep(3)

while True:
    playerScore = 0
    
    possibleAnswers = ['a', 'b', 'c', 'd']

    #Question 1
    print()
    print("Question 1: Who was the first multi-type Ultraman?")
    time.sleep(1)

    print("A: Ultraman Trigger \nB: Ultraman Dyna \nC: Ultramn Hikari\nD: Ultraman Tiga")
    print()
    answer = input("Please input the letter of your answer: ")
    
    while answer.lower() not in possibleAnswers:
        answer = input("Hey, that's not an answer choice! Try again please: ")

    if answer.lower() == 'd':
            playerScore += 1    
    
    #Question 2
    print()
    print("Question 2: How many different looks did the original Ultraman have in his 1960s TV show?")
    time.sleep(1)

    print("A: 1 \nB: 2 \nC: None\nD: 4")
    print()
    answer = input("Please input the letter of your answer: ")

    while answer.lower() not in possibleAnswers:
        answer = input("Hey, that's not an answer choice! Try again please: ")

    if answer.lower() == 'b':
            playerScore += 1   
    
    #Question 3
    print()
    print("Question 3: What is true about Ultraman Mebius and Ultraman Hikari?")
    time.sleep(1)

    print("A: They both have swords \nB: Their first designs didn't have eyes \nC: They are brothers\nD: They are both multi-type Ultramen")
    print()
    answer = input("Please input the letter of your answer: ")

    
    while answer.lower() not in possibleAnswers:
        answer = input("Hey, that's not an answer choice! Try again please: ")

    if answer.lower() == 'a':
            playerScore += 1   

    #Question 4
    print()
    print("Question 4: How many Ultramen have numbers in their names?")
    time.sleep(1)

    print("A: None (That's ridiculous!) \nB: 3 \nC: 14\nD: 1")
    print()
    answer = input("Please input the letter of your answer: ")

    while answer.lower() not in possibleAnswers:
        answer = input("Hey, that's not an answer choice! Try again please: ")

    if answer.lower() == 'b':
            playerScore += 1   
    
    #Question 5
    print()
    print("Question 5: Which Ultraman was the first to have Horns?")
    time.sleep(1)

    print("A: Horns? \nB: Ultraman Trigger \nC: Ultraman Taro\nD: Ultraman Horns")
    print()
    answer = input("Please input the letter of your answer: ")

    while answer.lower() not in possibleAnswers:
        answer = input("Hey, that's not an answer choice! Try again please: ")

    if answer.lower() == 'c':
            playerScore += 1   
    
    #Question 6
    print()
    print("Question 6: Which Ultraman has a villian named after him?")
    time.sleep(1)

    print("A: Ultraseven \nB: Ultraman Cosmos \nC: Ultraman Gaia\nD: Ultraman Ace")
    print()
    answer = input("Please input the letter of your answer: ")

    while answer.lower() not in possibleAnswers:
        answer = input("Hey, that's not an answer choice! Try again please: ")

    if answer.lower() == 'd':
            playerScore += 1   
    
    #Question 7
    print()
    print("Question 7: Is every Ultraman born on their home planet?")
    time.sleep(1)

    print("A: No \nB: Yes")
    print()
    answer = input("Please input the letter of your answer: ")

    while answer.lower() not in possibleAnswers:
        answer = input("Hey, that's not an answer choice! Try again please: ")

    if answer.lower() == 'a':
            playerScore += 1   
    
    #Question 8
    print()
    print("Question 8: Which Ultraman wields the Ultra Bracelet?")
    time.sleep(1)

    print("A: Ultraman Jack \nB: Ultraman Ginga \nC: Ultra Father\nD: Ultraman the Next")
    print()
    answer = input("Please input the letter of your answer: ")

    while answer.lower() not in possibleAnswers:
        answer = input("Hey, that's not an answer choice! Try again please: ")

    if answer.lower() == 'a':
            playerScore += 1   
    
    #Question 9
    print()
    print("Question 9: Which Ultraman made their debut in 2004?")
    time.sleep(1)

    print("A: Ultra Mother \nB: Ultraman Agul \nC: Ultraman Zearth\nD: Ultraman Nexus")
    print()
    answer = input("Please input the letter of your answer: ")

    while answer.lower() not in possibleAnswers:
        answer = input("Hey, that's not an answer choice! Try again please: ")

    if answer.lower() == 'd':
            playerScore += 1   
    
    #Question 10
    print()
    print("Question 10: Which Ultraman video game has air combat mechanics?")
    time.sleep(1)

    print("A: Ultraman Fighting Evolution: Rebirth \nB: None of them \nC: Ultraman Fighting Evolution 3\nD: Ultraman Nexus")
    print()
    answer = input("Please input the letter of your answer: ")

    while answer.lower() not in possibleAnswers:
        answer = input("Hey, that's not an answer choice! Try again please: ")

    if answer.lower() == 'd':
            playerScore += 1   
    
    #Score calculation
    print()
    print("You got " + str(playerScore) + " out of 10 question correct")

    if (playerScore < 4):
        print("You got some learning to do!")
        time.sleep(1)
    elif playerScore >= 4 and playerScore <= 7:
        print("Ok you know some Ultraman knowledge!")
        time.sleep(1)
    elif playerScore >= 8:
        print("Wow, get a life nerd!!")
        time.sleep(1)


    print()
    answer = input("Do you want to play again?: ")

    while answer.lower() != 'yes':
        if answer.lower() == 'no':
            print("All right, thanks for playing!!")
            quit()
        
        answer = input("Ok man, that's not an answer that we're looking for. Please try again: ")
        
    print("Ok, let's run it again...")
    print()

    time.sleep(2)
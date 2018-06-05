#By Ali and Jason
#Last Edited by Ali at 11/22/16 
class Error(Exception):
    """ Base class for other exceptions """
    pass
class ValueNotYorN(Error):
    """Raised when value not Y or N"""
    pass
class ValueNotRight(Error):
    """Raise when value not between 1-5 for numQuestions"""
    pass

#This is a Basic Trivia Adventure game that also displays your IQ, have fun!
spaces = ' '
def Repeat():
    import random
    import time
    #This block allows to setup the game's instructions with nice formatting
    score = 0
    from random import shuffle
    
    print()
    print ("Welcome to Brainiac, a Trivia Adventure!")
    print()
    name = input('Please enter your name: ')
    print()
    print ("Hit the enter key to start")
    input()
    print()
    print ('Please Wait.........')
    print()
    time.sleep(2)
    print ('Loading.........')
    time.sleep (2)
    print()
    
    print(25*spaces,'How to play')
    print()
    print(2*spaces,'*YOU MUST READ THIS*')
    print ()
    time.sleep(2)
    print(2*spaces,'This trivia will include many different types of questions')
    print(2*spaces,'which vary in level from easy, medium, and hard to test your IQ!')
    print(2*spaces,'Easy = 1 point, Medium = 3 points & Hard = 5 points')
    print(2*spaces,'The purpose is to obtain the most correct answers within each set.')
    print(2*spaces,'You have 15 seconds for each easy question, ')
    print(2*spaces,'25 seconds for each medium level question and ')
    print(2*spaces,'35 seconds for each hard level question.')
    print()
    print(13*spaces,'Good luck {} and remember to have fun! :)'.format(name))
    print()
    print('Hit the ENTER key to answer the questions')
    input()
#FIRST BLOCK FOR EASY LEVEL QUESTIONS 
    print("Lets begin with the Easy-Level Questions!")
    print()
    time.sleep(2)
    easyQuestion = [
        ('Which continent is Togo in?','africa'),
        ('How many years was World War II? Enter a number: ','6'),
        ('What state was last to join the US union?','hawaii'),
        ('What is the element K?','potassium'),
        ('What is the square root of 1225?','35'),
        ('What is the last name of the author that wrote Harry Potter?', 'rowling'),
        ('What country can Machu Pichu be found in?', 'peru'),
        ('What kind of drink is popular in Russia?', 'vodka'),
        ('Name the seventh planet from the sun.', 'uranus'),
        ('What country has the worlds biggest island?','denmark'),
        ('What is the natural satelite of Earth?', 'moon'),
        ('How many matrix movies have there been? Enter a number: ','3'),
        ('How many presidents has USA had so far? Enter a number: ', '45'),
        ('Who is our current prime minister full name?', 'justin trudeau'),
        ('What is the last name of the only heavyweight boxer that never lost?', 'mayweather'), 
        ('Which chess piece can only move diagonally?', 'bishop'),
        ('What is full name of the GOAT in basketball', 'michael jordan'), 
        ('Who scored the hand of god goal?','maradona'),
        ('How many valves does a trumpet have? Enter a number: ','3'),
        ('What picture is Leonardo Da Vinci famous for? ','mona lisa')
        ]
    
    shuffle(easyQuestion) #Random question is chosen for the user
    Correct1 = 0
    Incorrect = []
    #Verify if the number of questions is in range
    #if they dont enter a number or if the number is not in range
    #Output incorrect
    while True:
        try:
            numQuestions1 = int(input("There are 20 questions, How many questions do you want to answer? Enter a number: "))
            if numQuestions1 < 0 or numQuestions1 >= 21:
                raise ValueNotRight
            else:
                print ()
                print ("Loading questions......")
                time.sleep(2)
            break
        except ValueNotRight:
            print ()
            print('Wrong number, please try again')
            print ()
        except ValueError:
            print()
            print('This is not a NUMBER ')
            print()
            
    print()
    
    #Asks user's input for answer and displays if they got correct/incorrect
    for question, rightAnswer in easyQuestion[:numQuestions1]:
        start_time = time.time()
        answer = input(question + ' ').lower()
        #If incorrect or time is over, print correct answer(s)
        while time.time() - start_time > 15 or answer != rightAnswer:
            print()
            print("You either got it wrong or time is up or maybe both!")
            time.sleep(2)
            print()
            print("The correct answer was: ", rightAnswer)
            time.sleep(2)
            print()
            Incorrect.append(question)
            break
        #If answered in time range, print correct 
        while time.time() - start_time < 15 and answer == rightAnswer:
            print()
            print("Correct!")
            print()
            Correct1 += 1
            score += 1
            break
    time.sleep(2)
    #Display questions correct & sub-score for this level of question
    print("You got %s correct answers." %(Correct1))
    print()
    time.sleep(2)
    print ("Your current score is: ",score)
    time.sleep(2)
    if (Incorrect):
        print()
        print("You got these questions wrong: ")
        for q in Incorrect:
            print(q)
            time.sleep(1)
#NEXT BLOCK FOR MEDIUM LEVEL QUESTIONS
    time.sleep (2)
    print()
    print("Lets continue with the Medium-Level Questions!")
    print()
    mediumQuestion = [
        ('Where is paddington Bear originally from?', 'peru'),
        ('What is the largest fresh water lake in North America? Add the word lake: ','lake superior'), 
        ('Which insect shorted out an early supercomputer and inspired the term "computer bug"?', 'moth'),
        ('Who gave the inspiring "Just say NO" speech (full name)?', 'nancy reagan'),
        ('What year did Canada break away from England?', '1867'), 
        ('In what year was the first modern Olympic Games held?','1896'),
        ('Which is the most widely spoken language in the world?', 'chinese'),
        ('What female singer has a wardrobe issue during Superbowl XXXVIII (full name)?', 'janet jackson'),
        ('Which animal has the largest brain?','sperm whale'),
        ('A teetotaler is a person that never drinks what?', 'alcohol'),
        ('One kilobyte is equal to how many bytes?', '1024'),
        ('Which US president was known as "The Great Communicator" (full name)?','ronald reagan'),
        ('Who was prime minister during World War II for Britain? Enter the last name:', 'churchill'),
        ('What year was the first iphone released?','2007'),
        ('Which year did Lion King come out?', '1994'),
        ('In what year was Prince Andrew born?','1960'),
        ('Who owns apple? (full name)', 'steve jobs'), 
        ('What is the capital city of Bangledesh?', 'dhaka'),
        ('In which 1979 film was the spaceship called Nostromo?','alien'),
        ('What sport is played in Wimbledon?','tennis')
        ]
    
    shuffle(mediumQuestion) #Random question is chosen for the user
    Correct2 = 0
    Incorrect = []
    #Verify if the number of questions is in range
    #if they dont enter a number or if the number is not in range
    #Output incorrect 
    while True:
        try:
            numQuestions2 = int(input("There are 20 questions, how many questions do you want to answer? Enter a number: "))
            if numQuestions2 < 0 or numQuestions2 >= 21:
                raise ValueNotRight
            else:
                print ()
                print ("Loading questions......")
                time.sleep(2)
            break
        except ValueNotRight:
            print ()
            print('Wrong number, please try again')
            print ()
        except ValueError:
            print()
            print('This is not a NUMBER ')
            print()
    print()
    #Asks user's input for answer and displays if they got correct/incorrect
    for question, rightAnswer in mediumQuestion[:numQuestions2]:
        start_time = time.time()
        answer = input(question + ' ').lower()
        #If incorrect or time is over, print correct answer(s)
        while time.time() - start_time > 25 or answer != rightAnswer:
            print()
            print("You either got it wrong or time is up or maybe both!")
            time.sleep(2)
            print()
            print("The correct answer was: ", rightAnswer)
            time.sleep(2)
            print()
            Incorrect.append(question)
            break
        #If answered in time range, print correct 
        while time.time() - start_time < 25 and answer == rightAnswer:
            print()
            print("Correct!")
            print()
            Correct2 += 1
            score += 3
            break
    #Display questions correct & sub-score for this level of question
    time.sleep(2)
    print("You got %s correct answers." %(Correct2))
    print()
    print('Your current score is: ',score)
    time.sleep(2)
    if (Incorrect):
        print()
        print("You got these questions wrong: ")
        for q in Incorrect:
            print(q)
            time.sleep(1)
#NEXT BLOCK FOR HARD LEVEL QUESTIONS
    time.sleep(2)
    print()
    print("Lets finish with the Hard-Level Questions!")
    print()
    hardQuestion = [
        ('How many countries on the security council? Enter number: ','5'), 
        ('How many seasons does the walking dead have? Enter number: ','7'), 
        ('The Newlyn School of the late 19th century, is associated with which group of people?','painters '),
        ('If you planted the seeds of Quercus robur, what would grow?','trees'),
        ('Which scientific unit is named after an Italian nobleman?', 'volt'),
        ('What is the deepest lake in the world? Enter name with lake in front: ', 'lake baikal'), 
        ('How many bones are there in a giraffes neck','7'),
        ('30% of adults do this while driving.', 'snapchat'),
        ('What game, originally called Pretzel, was first introduced as a beach game?','twister'),
        ('One in ten families don’t save these.', 'leftovers'),
        ('What street does Spongebob Squarepants live on?', 'conch street'), 
        ('150 people are killed by this food each year, what is it?','coconuts'),
        ('Which movie did Denzel Washington say "Whos your daddy?"','remember the titans'),
        ('Is it legal for a man to marry his widow’s sister, Yes or No?','no'),
        ('If you throw a red stone into the blue sea what it will become?','wet'),
        ('What gets wetter & wetter the more it dries?','towel'),
        ('If there are 12 fish and half of them drown, how many are there?', '12'), 
        ('Jason decided to give his bike 3 coats of paint. Which coat would go on the first?','second'),
        ('What word starts with IS, ends with AND and has LA in the middle?', 'island'),
        ('What’s the official language of the Bahamas?', 'english') 
        ]

    shuffle(hardQuestion) #Shuffles the questions in the list, hardQuestion
    Correct3 = 0
    Incorrect = []
    #Verify if the number of questions is in range
    #if they dont enter a number or if the number is not in range
    #Output incorrect 
    while True:
        try:
            numQuestions3 = int(input("There are 20 questions,how many questions do you want to answer? Enter a number: "))
            if numQuestions3 < 0 or numQuestions3 >= 21:
                raise ValueNotRight
            else:
                print ()
                print ("Loading questions......")
                time.sleep(2)
            break
        except ValueNotRight:
            print ()
            print('Wrong number, please try again')
            print ()
        except ValueError:
            print()
            print('This is not a NUMBER ')
            print()
    print()
    #Asks user's input for answer and displays if they got correct/incorrect
    for question, rightAnswer in hardQuestion[:numQuestions3]:
        start_time = time.time()
        answer = input(question + ' ').lower()
        #If incorrect or time is over, print correct answer(s)
        while time.time() - start_time > 35 or answer != rightAnswer:
            print()
            print("You either got it wrong or time is up or maybe both!")
            time.sleep(2)
            print()
            print("The correct answer was: ", rightAnswer)
            print()
            Incorrect.append(question)
            break
        #If answered in time range, print correct 
        while time.time() - start_time < 35 and answer == rightAnswer:
            print()
            print("Correct!")
            print()
            Correct3 += 1
            score += 5
            break
    #Display questions correct & sub-score for this level of question
    time.sleep(2)
    print("You got %s correct answers." %(Correct3))
    if (Incorrect):
        print()
        print("You got these questions wrong: ")
        time.sleep(2)
        print()
        print('Your current score is: ',score)
        time.sleep(2)
        for q in Incorrect:
            print(q)
            time.sleep(1)
    print ()
    #Displays final score with how many questions the user got correct
    time.sleep(2)
    correctFinal = Correct1 + Correct2 + Correct3
    QuestionTotal = numQuestions1 + numQuestions2 + numQuestions3
    print ('Your final score is {} and you got {} questions correct'.format(score,correctFinal))
    time.sleep(2)
    print()
    #Informs the user on their IQ level based on the # of questions correct
    percent = correctFinal / QuestionTotal * 100
    if percent == 100:
        print ('Your IQ is beyond our reach... Smart human....')
    elif percent >= 90:
        print ('Almost a genius, your IQ is 125')
    elif percent >= 80:
        print ('Above Average, your IQ is 115')
    elif percent >= 70:
        print ('Congrats you hit the average! Your IQ is 90')
    elif percent >= 60:
        print ('Could use some improvement, but great try! Your IQ is 80')
    else:
        print ('Needs some improvement, your IQ is below average.')
    #To repeat the program, takes user input
    print()
    while True:
        try:
            #Displays credits if the user does not want to repeat
            again = (input("Do you want to play Brainiac again? (Y/N) "))
            if again == "N":
                quit
                print ()
                print (25*spaces, 'Credits')
                print ()
                print (25*spaces,'Designed by')
                print (25*spaces,'Jason & Ali')
                print ()
                print (25*spaces,'Have a good day!')
            elif again == "Y":
                Repeat()
            else: 
                raise ValueNotYorN
            break
        
        except ValueNotYorN:
            print('Error please try again...')
            

        
if __name__ == '__main__':
    Repeat()

        

    


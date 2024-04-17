import random

def wordle_answer(): #Picks the word used for the answer
    with open ("wordlist.txt", "r") as file: #opens the file and reads
        words = file.readlines() #puts words into a list
    return random.choice(words).strip().lower() #selects a random word

def check_guess1(guess): #Checks if the guess is valid
    if len(guess) != 5: #Checks if the guess does not equal five letters
        print('Invalid guess, please try another word!')
        return False
    else:
        return True

def check_guess2(guess): #Checks if the guess is valid
    with open ("wordlist.txt", "r") as file: #opens and reads the file
        words = file.read().splitlines() #puts words into a list
    if guess not in words: #if the guess is not in the list of words then inform the user the guess is not valid
        print('Invalid guess, please try another word!')
        return False
    else:
        return True
    
def evaluate(guess, answer): #evaluates guess
    guess_display = '' #empty string to display the guess with different colors
    letter_guessed = set() #empty set to get the correct letters
    for i in range(len(guess)): #iterates through the word
        letter = guess[i] #sets letter to the current letter in the guess
        if letter == answer[i]: #if the letter is the same as the answer make it green
            guess_display += "\033[32m" + letter
            letter_guessed.add(i) #adds to the set
        elif letter in answer and answer.index(letter) not in letter_guessed: #If the letter is in the answer and not in the set then this executes
            guess_display += "\033[33m" + letter #colors it red
            letter_guessed.add(answer.index(letter)) #adds to the letter guessed set
        else:
            guess_display += "\033[0m" + letter #make the other letters white
    return guess_display + "\033[0m" #returns the evaluated guess

def main(): 
    check = True
    attempts = 0
    answer = wordle_answer() #sets answer to the wordle answer
    print('Welcome to Worlde! \
          \nImportant Information: \
              \nA white letter means the the letter is not in the word. \
                  \nA red letter means the letter is in the word but not in the right position. \
                      \nA green letter means the letter is in the word and in the right position. \
                          \nYou only get 6 guesses.')
                          #explains the basic rules of how to play the game
    while attempts < 6: #limiting attempts to six
        if check == True: #if this is true it iterates through
            guess = input('What is your guess: ') #asks the user for a guess
            guess = guess.lower() #makes it lower case
            if not check_guess1(guess): #if it passes the check keep going
                continue
            if not check_guess2(guess): #if it passes the check keep going
                continue
            print (evaluate(guess, answer)) #prints the output of the evaluate function
        attempts += 1 #increases attempts
        if guess == answer: #Display text when the answer is correct. 
            print(f'Congrats! You got the wordle in {attempts} attempts.')
            break #breaks the loop
    else: #if the user uses runs out of attempts then a text informing them they lost is displayed
        print(f'Sorry, you used up all of your guesses, the word was {answer}.')

main() #executes main
            
             
    

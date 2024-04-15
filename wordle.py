import random

def wordle_answer():
    with open ("wordlist.txt", "r") as file:
        words = file.readlines()
    return random.choice(words).strip().lower()

def check_guess1(guess):
    if len(guess) != 5:
        print('Invalid guess, please try another word!')
        return False
    else:
        return True

def check_guess2(guess):
    with open ("wordlist.txt", "r") as file:
        words = file.read().splitlines()
    if guess not in words:
        print('Invalid guess, please try another word!')
        return False
    else:
        return True
def evaluate(guess, answer):
    guess_display = ''
    letter_guessed = set()
    for i in range(len(guess)):
        letter = guess[i]
        if letter == answer[i]:
            guess_display += "\033[32m" + letter
            letter_guessed.add(i)
        elif letter in answer and answer.index(letter) not in letter_guessed:
            guess_display += "\033[33m" + letter
            letter_guessed.add(answer.index(letter))
        else:
            guess_display += "\033[0m" + letter
    return guess_display + "\033[0m"

def main():
    check = True
    attempts = 0
    answer = wordle_answer()
    print('Welcome to Worlde!')
    while attempts < 6:
        if check == True:
            guess = input('What is your guess: ')
            guess = guess.lower()
            if not check_guess1(guess):
                continue
            if not check_guess2(guess):
                continue
            print (evaluate(guess, answer))
        attempts += 1
        if guess == answer:
            print(f'Congrats! You got the wordle in {attempts} attempts.')
            break
    else:
        print(f'sorry, you used up all of your guesses, the word was {answer}.')

main()
            
             
    

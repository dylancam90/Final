import string, sys, random
from termcolor import colored

# hash first char for placement in load array
def hash(word, whole=True):
    if whole:
        char = word[0]
    else:
        char = word
    index = string.ascii_lowercase.index(char)
    return index

# loading into memory
def load(file):
    array = [set() for i in range(26)]

    with open(file, "r") as f:
        for words in f.readlines():
            index = hash(words)
            array[index].add(words.strip())
    return array
    
# filters all incorrect inputs    
def guess(num):
    ask = input("Quess #" + str(num) + ": ").lower().strip()
    if len(ask) == 5 or ask.isalpha():
        return ask
    return guess(num)
         

# chooses random word from memory
def winning_word(word_list):        
    rando = [random.choice(tuple(word_list[i])) for i in range(len(word_list))]  
    return random.choice(rando)
    
# ask player what to do when game is over        
def play_again():
    play_again = input(colored("Play Again? y/n ", "blue"))
    # calls on main again if answer is yes
    if play_again.lower() in ("yes", "y"):
        main()
    elif play_again.lower() in ("no", "n"):
        print(colored("Thanks for playing!", "blue"))
        sys.exit()
    # if not acceptable input call it again
    print(colored("Not acceptable input enter yes/y or no/n", "red"))
    return play_again()

# check if word is in list
def check(word, word_list):
    if word in word_list[hash(word)]:
        return True
    return False
                  
def compare(win_word, guess_word, valid_letters):
    # checks postion of word for correctness
    for i in range(len(guess_word)):
        if guess_word[i] == win_word[i]:
            valid_letters[hash(guess_word[i], False)] = colored(guess_word[i], "green")
            print(colored(guess_word[i], "green"), end="")
        elif guess_word[i] in win_word:
            print(colored(guess_word[i], "yellow"), end="")
            valid_letters[hash(guess_word[i], False)] = colored(guess_word[i], "yellow")
        else:
            print(colored(guess_word[i], "white"), end="")
            valid_letters.pop(hash(guess_word[i], False))
    print()

# checks words for duplicates
def duplicate_filter(win_word):
    duplicates = {}
    count = 0
    for char in win_word:
        if char in duplicates:
            duplicates[char] += 1
        else:
            duplicates[char] = 1
    for key, value in duplicates.items():
        if value > 1:
            count += 1
    return (count > 0)

# prints alphabet onto screen
def print_letters(valid):
    for i in valid:
        print(i, end=" ")
    print()


def main():
    # list of alphabet
    valid = [i for i in string.ascii_lowercase]
    TURNS = 5
    # entire list
    word_list = load("wordle.txt")
    # randomly selected word from list
    win_word = winning_word(word_list)

    print(colored("Welcome to Wordle", "blue"))

    # warning if there is a duplicate letter in word
    if duplicate_filter(win_word):
        print(colored("WARNING DUPLICATE LETTER", "red"))

    i = 1
    # main turn loop
    while i < TURNS + 1:
        print_letters(valid)
        ask = guess(i)
        # if in list process
        if check(ask, word_list):  
            compare(win_word, ask, valid)
            i += 1
        else:
            print(colored("Word not in list", "red"))
        
        # if words match exactly
        if ask == win_word:
            print(colored("WINNER", "red"))
            break
    
    print(colored("The word was ", "blue") + colored(win_word.upper(), "green"))
    # end of game options
    return play_again()

            


if __name__ == "__main__":
    main()


    
    
import string, sys, random
from termcolor import colored
from time import process_time

# hash first char for placement in load array
def hash(word):
    char = word[0]
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
        
    """
    for i in ask:
        if i.isnumeric() or i in string.punctuation:
            return quess(num)
    if len(ask) != 5:
        return quess(num)
    """
    

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
                  
def compare(win_word, guess_word):
    # checks postion of word for correctness
    for i in range(len(guess_word)):
        if guess_word[i] == win_word[i]:
            print(colored(guess_word[i], "green"), end="")
        elif guess_word[i] in win_word:
            print(colored(guess_word[i], "yellow"), end="")
        else:
                print(colored(guess_word[i], "white"), end="")
    print()
        
        
def main():
    a = [i for i in string.ascii_lowercase]
    print(a)
    TURNS = 5
    # entire list
    word_list = load("wordle.txt")
    # randomly selected word from list
    win_word = winning_word(word_list)

    print(colored("Welcome to Wordle", "blue"))
    i = 1
    # main turn loop
    while i < TURNS + 1:
        ask = guess(i)
        # if in list process
        if check(ask, word_list):  
            compare(win_word, ask)
            i += 1
        else:
            print(colored("Word not in list", "red"))
        
        # if words match exactly
        if ask == win_word:
            print(colored("WINNER", "red"))
    
    print(colored("The word was ", "blue") + colored(win_word.upper(), "green"))
    # end of game options
    return play_again()

            


if __name__ == "__main__":
    main()


    
    
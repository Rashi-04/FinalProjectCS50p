import requests
import sys
from bs4 import BeautifulSoup
from simple_colors import *


# our main function
def main():
    print(magenta("You can stop reading headines by pressing Ctrl+C"))
    url = "https://www.bbc.com/news"
    response = requests.get(url).text                                             
# read_flag to know whether the user wants to read Vocab file or not
    read_flag = print_headlines(response)
    read_notebook(read_flag)


# function to write in our Vocab_notebook
def write_notebook():
    learned_word = input(blue("Which word did you learned? "))
    with open("Vocab_notebook.txt", "a") as file:
        file.write(f"{learned_word}\n")


# function to read from our Vocab_notebook
def read_notebook(rflag):
    if rflag == True:
        print()
        with open("Vocab_notebook.txt", "r") as file:                     #Project Name - VocabEnhancer
            words = file.readlines()
        num = 1
        for word in words:
            print(num, word.rstrip())
            num += 1
        print(magenta("\nSee you tomorrow! Happy Learning"))

    else:
        sys.exit(magenta("No Problem! Happy Learning. Bye"))


# function to print the news headlines one by one
def print_headlines(response):
    soup = BeautifulSoup(response, "html5lib")
    headline = soup.find("body").find_all(attrs ={"class":"gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary"})
    try:
        for i in headline: 
            print()
            print("\033[1m"+i.text.strip()+"\033[0m")
            print()
            flag = input(green("Hey! Did you find any new word for your vocabulary in this headline\nIf yes type:y\nIf no type:n\n")).lower()
            if(flag == "y"):
                write_notebook()
    except KeyboardInterrupt:
        pass
    finally:
        read_flag = input(blue("\nDo you want to read your vocab notes? y or n\n")).lower()
        if(read_flag == "y"):
            return True
        else:
            return False




if __name__ == "__main__":
    main()
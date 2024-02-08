"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Michaela Rossmannová
email: rossmannova.m@gmail.com
discord: misa02907
"""

import random
import time
from datetime import timedelta

separator = "-" * 47
print("Hi there!")
print(separator)
print("Welcome in our game Bulls and Cows!")
print(separator)
print("""
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
"""
      )
print(separator)


def main():
      """
      Define main function and generating random number.
      While cycle checks for user inputs and compare with random number using 
      function user input.
      Function Bulls_and_cows checks the position of numbers and 
      return number of bulls and cows for each guess.
      """
      start_time = time.time()
      attempts = 0
      separator = "-" * 47
      number = random_number()

      while True:
            correctly_guessing = input_control()
            counter = number_of_bulls_and_cows(number, correctly_guessing)
            bulls = counter[0]
            cows = counter[1]
            printing_number_of_bulls_and_cows(bulls, cows)
            print(separator)
            attempts += 1
            if bulls == 4:
                  break
            
      result = []
      for n in number:
            result.append(str(n))

      result_time = int((time.time() - start_time))
      print(str(timedelta(seconds=result_time)))

      return print(
            f"""
            Correct number is {''.join(result)}.
            You needed {attempts} attempts to guess the right result.
            Time of your game: {str(timedelta(seconds=result_time))}
            """)


def random_number():
      """
      generate a random number
      """
      choose_number = True
      while choose_number:
            # random.seed(1)
            number = random.sample(range(10), k = 4)
            # print(number)
            if number[0] != 0:
                  right_number = number
                  break
            else:
                  continue
      return right_number

 
def input_control():
      """
      Function which takes user input and check the formatting, 
      if it is ok, then it return the user input back to main()
      """

      while True:
            list_of_number = []
            user_input = input("Enter a number: ")
            for n in user_input:
                  if not n.isnumeric():
                        print("Wrong format.")
                        continue
                  elif user_input.count(n) > 1:
                        print("The digits must not be repeated.")
                        break
                  else:
                        list_of_number.append(int(n))
            if list_of_number and list_of_number[0] == 0 or len(list_of_number) != 4:
                  print("The number must not start with 0 and the number must be four digits.")
                  continue
            else:
                  break
      return list_of_number



def number_of_bulls_and_cows(number, correctly_guessing):
      """
      function which takes, random number and user input and return the 
      number of 'bulls' and 'cows' for the round
      """

      index_of_number = list(enumerate(number))
      bulls = 0
      cows = 0
      for i, numeral in enumerate(correctly_guessing):
            pair = tuple([i, numeral])
            if pair in index_of_number:
                  bulls +=1
            elif numeral in number and number[i] != numeral:
                  cows += 1
      return [bulls, cows]

# printing
def printing_number_of_bulls_and_cows(bulls, cows):
      if bulls == 1 and cows == 1:
            return print(f"{bulls} bull,{cows} cow")
      elif bulls == 1 and cows != 1:
            return print(f"{bulls} bull,{cows} cows")
      elif bulls != 1 and cows == 1:
            return print(f"{bulls} bulls,{cows} cow")
      elif bulls == 4:
            return print("YES! You got it!")
      else:
            return print(f"{bulls} bulls,{cows} cows")



if __name__ == "__main__":
    main()
from code_breaker import Codebreaker

TOTAL_ATTEMPTS = 10

codebreaker = Codebreaker()
attempts = 0

print("Jugar Codebreaker!")

while attempts != TOTAL_ATTEMPTS:
    number_to_guess = input("Guess Number:")
    if resolve := codebreaker.guess(number_to_guess):
        print("You win!!")
        break
    attempts += 1

if attempts == TOTAL_ATTEMPTS:
    print("You lost all your attempts !!")

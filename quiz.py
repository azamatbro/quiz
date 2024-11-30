# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 09:37:15 2024
@author: Azamat
"""

questions = ("How many elements in the Mendeleyev table?: ",
             "Which palnet is the biggest in solar system?: ",
             "What is the acceptance rate in MIT?: ",
             "How many bones are in the human body?:",
             "the biggest creature on Earth?: ")

options = (("A. 128 ","B. 130","C. 119","D. 118"),
           ("A. Earth","B. Saturn","C. Jupyter","D. Sun"),
           ("A. 10%","B. 4%","C. 6%","D. 1%"),
           ("A. 206","B. 207","C. 208","D. 209"),
           ("A. Whale","B. Shark","C. elephant","D. Crocodile"))
score = 0
question_num = 0 

for question in questions:
    print("-----------------------")
    print(question)
    for option in options[questions]:           
        answers = ("D","C","B","A","A")
        guesses = [question_num]:
            print(option)
    
    guess = input("Enter your choice: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:  
        print("Incorrect")
        print(f"{answers[question_num]} is Correct answer")
    question_num += 1

print("-----------------")
print("|     RESULTS   |")
print("-----------------")

print("answer: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = (score / len(questions) * 100)
print(f"Your score is: {score}%")

if score >= 80:
    print("WIN")
else: print("LOST")

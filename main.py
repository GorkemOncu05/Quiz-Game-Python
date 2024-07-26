#Python quiz game


questions = ("You should write your questions here")

options = ("A. ", "B. ", "C. ", "D. ")#You should add all the answers to the questions here


answers = ("A","B","C","D")#How many questions you asked, you should write the correct answers to the questions here.
guesses = []
score = 0
questions_num = 0


for question in questions:
    print("----------------------")
    print(question)
for option in options[questions_num]:
    print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[questions_num]:
       score += 1
       print("CORRECT!")
else:
    print("INCORRECT!")
    print(f"{answers[questions_num]} is the correct answer")
    questions_num += 1

    print("----------------------")
    print("       RESULTS        ")
    print("----------------------")
    print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
    print()
    print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
    print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
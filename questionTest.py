import random # https://docs.python.org/3/library/random.html for pseudo-random as I don't think we covered it in class yet

def askQuestion(question, index, correctAnswer, seed=None):
    # question = the list of questions being asked
    # index = the specific question to ask (list inside a list)
    # correctAnswer = a number from 1-4 which is the index to the correct answer based on the list (index) given
    # seed = seed for random question sort

    # sets constant indexes
    questionAsked = question[index][0]
    feedback = question[index][5]

    if seed: #random seed if not inputted one
        random.seed(seed)
    else:
        random.seed()

    uniqueRandomList = random.sample(range(1, 5), 4) # generates a unique list of 4 numbers to be used to randomize questions

    # sets random indexes
    answerOne = question[index][uniqueRandomList[0]]
    answerTwo = question[index][uniqueRandomList[1]]
    answerThree = question[index][uniqueRandomList[2]]
    answerFour = question[index][uniqueRandomList[3]]


    answer = input(questionAsked #asks question
    + "\nA) " +answerOne
    + "\nB) " +answerTwo
    + "\nC) " + answerThree
    + "\nD) " + answerFour + "\n\n")

    answeredQuestion = False
    while answeredQuestion == False: # probably not the most efficient way of doing this but it works :P

        if answer.upper() == "A":
            answer = 1
            answeredQuestion = True
        elif answer.upper() == "B":
            answer = 2
            answeredQuestion = True
        elif answer.upper() == "C":
            answer = 3
            answeredQuestion = True
        elif answer.upper() == "D":
            answer = 4
            answeredQuestion = True
        else:
            answer = input("Please type a letter! \n")

    if uniqueRandomList[answer-1] == correctAnswer: # checks if answer is correct
        print("Correct!")
        print(feedback)
    else:
        letters = ["A) ", "B) ", "C) ", "D) "]
        print("Incorrect! The correct answer was " + str(letters[uniqueRandomList.index(correctAnswer)]) + str(question[index][correctAnswer]))
        print(feedback)
    print("")

questionList = [
    ["Asking question", "answerOne", "answerTwo", "answerThree", "answerFour", "feedback", 1],
    ["Asking question Two", "answerOne", "answerTwo", "answerThree", "answerFour", "feedback", 2],
    ["Asking question Three", "answerOne", "answerTwo", "answerThree", "answerFour", "feedback", 3],
    ["Asking question Four", "answerOne", "answerTwo", "answerThree", "answerFour", "feedback", 4]
]
# Format for adding new questions: ["question: ", "answerOne", "answerTwo", "answerThree", "answerFour", "feedback (context after answered)", 1-4 (correct answer)]

random.seed()
uniqueQuestionList = random.sample(range(0, len(questionList)), len(questionList)) # generates order for questions to be asked

for i in range(0, len(questionList)): #asks all questions in questionList at randomly generated order (uniqueQuestionList)
    askQuestion(questionList, uniqueQuestionList[i], questionList[uniqueQuestionList[i]][6])

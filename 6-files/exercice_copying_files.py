"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
# your code starts here:
with open('questions.txt', 'r') as f:
    questions = f.readlines()
pontos = 0

# poderia ter feito uma lista de compreensão para tratar questions:
# q_tratadas = [line.strip() for line in questions]
for question in questions:
    q = question.strip().split('=')
    answer = int(input(f'{q[0]} = '))
    if answer == eval(q[1]):
        pontos += 1

with open ('results.txt', 'a+') as f:
    f.write(f'Your final score is {pontos}/{len(questions)}.')

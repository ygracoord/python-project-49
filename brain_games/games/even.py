import random
import prompt

TITLE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    random_num = random.randint(1, 100)
    print(f'Question: {random_num}')
    user_answer = prompt.string('Your answer: ')

    if random_num % 2 == 0:
        success_answer = 'yes'
    else:
        success_answer = 'no'
    return user_answer, str(success_answer)

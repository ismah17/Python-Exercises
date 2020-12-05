from question import Question

question_prompts = [
    "What colour are apples?\n(a)Red/Green\n(b)Purple/Orange\n(c)Blue\n\n",
    "What colour are bananas?\n(a)yellow/Green\n(b)white/black\n(c)gold\n\n",
    "What colour are strawberries?\n(a)red\n(b)white/silver\n(c)gold\n\n",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print("you got {0}".format(score), " correct out of", len(questions))


run_test(questions)

questions = {
    'What is the biggest continent in the world?: ': 'asia',
    'Who was the first woman to fly solo across the Atlantic Ocean?: ': 'amelia earhart',
    'If you tipped 20% on a $15 bill, how much would the tip be?: ': '$3',
    'How many time zones are there in Russia?: ': "11"
}

score = 0

while True:
    start = input("Do you want to start the game (y/n): ")

    if start.lower() == 'y':
        for q, a in questions.items():
            userAns = input(q)
            if userAns.lower() == a:
                score += 1

        print('Correct answers:', score)
        print(f'Percentage: {score * 100 / len(questions)}%')
        break
    elif start.lower() == 'n':
        quit()
    else:
        print('Please type in y (yes) or n (no).')

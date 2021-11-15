with open('test_for1task.txt', 'w') as file:
    input_line = input('TEXT :\n')
    while input_line:
        file.write(f'{input_line}\n')
        input_line = input('Text :\n')

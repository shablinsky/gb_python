with open('test_for1task.txt') as file:
    file_lines = file.readlines()
    str_count = 0
    for num, line in enumerate(file_lines):
        str_count += 1
        words_count = len(line.split())
        print(f'string {num +1} have {words_count} words')
    print(f'{str_count} strings')

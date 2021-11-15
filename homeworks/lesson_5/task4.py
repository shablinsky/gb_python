nums = {
    'One': "Один",
    'Two': "Два",
    'Three': "Три",
    'Four': "Четыре",
}

with open('test_for4task.txt') as file, open('result_from_4task.txt', 'w') as new_file:
    file_lines = file.readlines()
    for line in file_lines:
        data = line.split()
        rus_num = nums.get(data[0])
        new_file.write(f'{line.replace(data[0], rus_num)}')
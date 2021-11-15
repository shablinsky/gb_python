with open('test_for3task.txt') as file:
    file_lines = file.readlines()
    employees = {}
    sum_salary = 0
    for line in file_lines:
        emp_info = line.split()
        employees.update({emp_info[0]: float(emp_info[1])})
        sum_salary += float(emp_info[1])
average_sal = sum_salary / len(employees)
print(f'average = {average_sal}')

for k, v in employees.items():
    if v < 20000:
        print(f'{k} have {v} (less 20k)')

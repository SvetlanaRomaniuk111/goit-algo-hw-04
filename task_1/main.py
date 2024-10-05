def total_salary(path):
    try:
        total_salary = 0  
        num_developers = 0  

        with open(path, 'r', encoding='utf-8') as file:

            try:
                for line in file:        
                    name, salary = line.split(',')       
                    total_salary += int(salary)          
                    num_developers += 1
            except ValueError:
                print(f"Помилка: Неправильний формат даних '{line}'")
                return 0, 0
            
        if num_developers > 0:
            average_salary = int(total_salary / num_developers)       
            return total_salary, average_salary
        else:
            return 0, 0
        
    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' відсутній або пошкоджений.")
        return 0, 0
    

total, average = total_salary("task_1/salary_file.txt")

print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

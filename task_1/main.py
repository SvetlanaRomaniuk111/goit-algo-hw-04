def total_salary(path):
    try:
        total_salary = 0  # Загальна сума зарплат
        num_developers = 0  # Лічильник кількості розробників

        # Відкриваємо файл для читання
        with open(path, 'r', encoding='utf-8') as file:
            # Читаємо кожен рядок файлу
            for line in file:
                developer_string = line.strip().split(',')
                # name, salary = line.strip().split(',')
                if len(developer_string) == 2:
                    try:
                        salary = int(developer_string[1])
                        total_salary += salary 
                        num_developers += 1
                    except ValueError:
                        print(f"Помилка: Неправильний формат заробітної плати '{line}'")
                else:
                    print(f"Помилка: Неправильний формат даних у рядку '{line}'")
        # Якщо є розробники, обчислюємо середню зарплату
        if num_developers > 0:
            average_salary = total_salary // num_developers  # Цілий поділ для середньої зарплати
            return total_salary, average_salary
        else:
            return 0, 0  # Якщо немає даних, повертаємо 0
    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' відсутній або пошкоджений.")
        return 0, 0  # Повертаємо 0 у випадку помилки з файлом

# Виклик функції та виведення результату
total, average = total_salary("task_1/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

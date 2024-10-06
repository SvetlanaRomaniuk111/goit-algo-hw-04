def get_cats_info(path):
    cats_list = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            try:
                for line in file:        
                    id_cat, name, age = line.strip().split(',')
                    info_each_cat = {'id': id_cat, 'name': name,'age': age}
                    cats_list.append(info_each_cat)
                return cats_list

            except ValueError:
                print(f"Помилка: Неправильний формат даних '{line}'")
                return []
    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' відсутній або пошкоджений.")
        return []
cats_info = get_cats_info("task_2/cats_file.txt")
print(cats_info)       
import sys
from pathlib import Path
from colorama import init, Fore

# Ініціалізація colorama
init(autoreset=True)

def visualize_directory_structure(directory, level=0):
    """Рекурсивна функція для візуалізації структури директорії з кольоровим виведенням."""
    indent = ' ' * 4 * level  # Визначаємо рівень вкладеності для відступів
    
    # Перевіряємо всі елементи в директорії
    for item in directory.iterdir():
        # Якщо це директорія, виводимо її синім кольором
        if item.is_dir():
            print(f"{indent}{Fore.BLUE}{item.name}/")
            # Рекурсивно заходимо у вкладені директорії
            visualize_directory_structure(item, level + 1)
        # Якщо це файл, виводимо його зеленим кольором
        else:
            print(f"{indent}{Fore.GREEN}{item.name}")

if __name__ == "__main__":
    # Перевіряємо, чи вказано шлях до директорії як аргумент командного рядка
    if len(sys.argv) != 2:
        print("Usage: python main.py <directory_path>")
        sys.exit(1)
    
    # Отримуємо шлях до директорії
    directory_path = Path(sys.argv[1])
    
    # Перевіряємо, чи існує вказана директорія і чи вона є директорією
    if not directory_path.exists() or not directory_path.is_dir():
        print(f"Error: Directory '{directory_path}' not found or is not a directory.")
        sys.exit(1)
    
    # Візуалізуємо структуру директорії рекурсивно
    visualize_directory_structure(directory_path)

from colorama import Fore
import sys
path = sys.argv[1]

from pathlib import Path

directory_structure = Path(path)

def parse_folder(path):
    # Якщо вказаний шлях не існує або об'єкт не єдиректорією, отримаємо помилку
    if not path.is_dir() or not path.exists():
        print(Fore.RED + f"Вказаний шлях '{path}' не існує або він не веде до директорії")
        return
    # Якщо вказаний шлях існує, виведемо список елементів з директорії
    for element in path.iterdir():
        if element.is_dir():
            print(Fore.BLUE + f"Folder: {element.name}")
            # parse_folder(element)
        if element.is_file():
            print(Fore.GREEN + f"File: {element.name}")

parse_folder(directory_structure)

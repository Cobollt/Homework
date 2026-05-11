import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)

def print_directory_structure(path: Path, indent: str = ''):
    try:
        item = sorted(path.iterdir(), key=lambda item :(item.is_file(), item.name.lower()))
    except PermissionError:
        print(indent + Fore.RED + "[Немае доступу]")
        return

    for item in item:
        if item.is_dir():
            print(indent + Fore.BLUE + f"📁 {item.name}")
            print_directory_structure(item, indent + "     ")
        else:
            print(indent + Fore.GREEN + f"📄 {item.name}")

def main() -> None:
    if len(sys.argv) != 2:
        print(Fore.RED + "Помилка: потрібно передати шлях до директорії.")
        print("Приклад запуску: python main.py ./my_folder")
        return

    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print(Fore.RED + "Помилка: вказаний шлях не існує.")
        return
    if not directory_path.is_dir():
        print(Fore.RED + "Помилка: вказаний шлях не є директорією.")
        return

    print(Fore.YELLOW + f"Структура директорії: {directory_path.resolve()}")
    print_directory_structure(directory_path)

if __name__ == "__main__":
    main()
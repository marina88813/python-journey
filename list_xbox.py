import os

# Путь к системной папке приложений Windows
path = r"C:\Program Files\WindowsApps"

try:
    # Получаем список всех папок внутри WindowsApps
    all_folders = os.listdir(path)
    
    # Фильтруем папки, в названии которых есть "xbox" (без учета регистра)
    xbox_folders = [f for f in all_folders if "xbox" in f.lower()]
    
    # Выводим результат
    if xbox_folders:
        print(f"Найдено папок Xbox: {len(xbox_folders)}\n")
        for folder in sorted(xbox_folders):
            print(f"- {folder}")
    else:
        print("Папки со словом Xbox не найдены.")

except PermissionError:
    print("Ошибка: Недостаточно прав для чтения папки. Запустите скрипт/CMD от имени администратора!")
except FileNotFoundError:
    print("Ошибка: Указанный путь не найден.")

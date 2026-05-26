import psutil

print("Проверка процессов, загружающих процессор (более 1%):")
print("-" * 50)

# Перебираем запущенные процессы
for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
    try:
        # Получаем процент загрузки процессора
        cpu = proc.info['cpu_percent']
        if cpu and cpu > 1.0:
            print(f"Процесс: {proc.info['name']} (PID: {proc.info['pid']}) — Загрузка: {cpu}%")
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

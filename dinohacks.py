import subprocess
import time
import pychrome
from pynput import keyboard  # Подключаем pynput для отслеживания нажатий клавиш
import threading
import random

# Запуск браузера
chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"  # macOS
subprocess.Popen([
    chrome_path,
    "--remote-debugging-port=9222",  # Порт для подключения
    "--user-data-dir=/tmp/ChromeDev",  # Временная директория профиля
    "--no-first-run",  # Пропускаем первый запуск
    "--disable-popup-blocking",  # Отключаем блокировку всплывающих окон
    "--enable-fullscreen"
])
time.sleep(2)  # Ожидание запуска браузера

# Подключение к браузеру
browser = pychrome.Browser(url="http://127.0.0.1:9222")
print(__file__)
# Открытие новой вкладки с определённым URL
url = "chrome://dino"  # Укажите нужный адрес
tab = browser.new_tab(url)
tab.start()
tab.Page.enable()

# Изменение цвета фона

def XDfunction(speed):
    global tab
    tab.Runtime.evaluate(expression=f'Runner.instance_.tRex.jumping = {speed}')

# Глобальная переменная для отслеживания состояния Shift
shift_pressed = False

# Обработчики событий нажатия и отпускания клавиш
def on_press(key):
    global shift_pressed
    if key == keyboard.Key.shift:
        shift_pressed = True

def on_release(key):
    global shift_pressed
    if key == keyboard.Key.shift:
        shift_pressed = False

# Функция для выполнения действий в цикле
def main_loop():
    while True:
        if shift_pressed:
            tab.Runtime.evaluate(expression="Runner.instance_.setSpeed(0.01)")
            while shift_pressed:
                tab.Runtime.evaluate(expression="Runner.instance_.distanceRan +=1000000")
        time.sleep(0.1)  # Задержка для снижения нагрузки на процессор
        tab.Runtime.evaluate(expression="Runner.instance_.setSpeed(6)")
# Запуск слушателя в отдельном потоке
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

# Запуск основного цикла
main_loop()

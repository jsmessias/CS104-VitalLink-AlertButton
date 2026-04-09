import time
import requests
import RPi.GPIO as GPIO
import requests

BOT_TOKEN = "8617191622:AAEYXOnPa86Os4gzVq0VaNKaqs_vLy3syuY"
CHAT_ID = "6034445994"

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

button_pressed = False

def send_alert():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": "Someone pressed the alert button!"
    }
    requests.post(url, json=data)

def send_alert():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": "Someone pressed the alert button!"
    }
    response = requests.post(url, json=data, timeout=10)
    print(response.json())

try:
    while True:
        if GPIO.input(7) == GPIO.HIGH and not button_pressed:
            print("Someone pressed the alert button!")
            send_alert()
            button_pressed = True

        elif GPIO.input(7) == GPIO.LOW:
            button_pressed = False

        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()

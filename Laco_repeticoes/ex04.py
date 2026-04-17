#Relogio
import time
from datetime import datetime

while True:
    now = datetime.now()
    hr = now.strftime("%H:%M:%S")
    print("Hora certa:", hr, end= "\r")
    time.sleep(1)
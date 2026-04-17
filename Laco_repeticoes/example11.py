from datetime import datetime

hr = datetime.now().hour


if hr >= 6 and hr < 12:
    print("Bom dia! =D")
elif hr >= 12 and hr < 18:
    print("Boa tarde! :b")
else:
    print("Boa noite! -_-")
import tkinter as tk
import requests

def convert():
    try:
        amount = float(entry.get())
        exchange_rate = get_exchange_rate()
        result.config(text="${:.2f}".format(amount * exchange_rate))
    except ValueError:
        result.config(text="Invalid input !")

def get_exchange_rate():
    response = requests.get("https://api.exchangerate-api.com/v4/latest/EUR", headers={"apikey": "YOUR_API_KEY"})
    data = response.json()
    return data["rates"]["CAD"]

window = tk.Tk()
window.title("EUR-CAD Converter")

entry = tk.Entry(window)
button = tk.Button(window, text="Convert", command=convert)
result = tk.Label(window, text="")

entry.pack()
button.pack()
result.pack()

window.mainloop()

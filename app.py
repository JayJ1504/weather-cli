import tkinter as tk
from weather import get_weather

root = tk.Tk()
root.title("weather APP")
city_entry = tk.Entry(root)
city_entry.pack()

def show_weather():
    city = city_entry.get()
    result = get_weather(city)
    result_label.config(text=result)

search_button = tk.Button(root, text="Get Weather", command=show_weather)
search_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
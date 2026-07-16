import tkinter as tk
from weather import get_weather

root = tk.Tk()
root.title("Weather App")
root.geometry("300x200")  

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

city_label = tk.Label(frame, text="Enter City Name:", font=("Arial", 12))
city_label.pack()

city_entry = tk.Entry(frame, font=("Arial", 12))
city_entry.pack(pady=5)

def show_weather(event=None):
    city = city_entry.get()
    result = get_weather(city)
    result_label.config(text=result)

root.bind('<Return>', show_weather)
search_button = tk.Button(frame, text="Get Weather", command=show_weather, font=("Arial", 12), bg="lightblue")
search_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="left", fg="darkblue")
result_label.pack(pady=10)

root.mainloop()

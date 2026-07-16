import tkinter as tk
from weather import get_weather

root = tk.Tk()
root.title("Weather App")
root.geometry("350x300")  
root.configure(bg="#f4f4f6")  


frame = tk.Frame(root, padx=20, pady=20, bg="#f4f4f6")
frame.pack(expand=True)

city_label = tk.Label(frame, text="Enter City Name:", font=("Arial", 12, "bold"), bg="#f4f4f6", fg="#333333")
city_label.pack(pady=5)

city_entry = tk.Entry(frame, font=("Arial", 12), bd=1, relief="solid", justify="center")
city_entry.pack(pady=8, ipady=4) 
city_entry.focus()  

def show_weather(event=None):
    city = city_entry.get()
    if city.strip():  
        result = get_weather(city)
        result_label.config(text=result)

root.bind('<Return>', show_weather)

search_button = tk.Button(
    frame, 
    text="Get Weather", 
    command=show_weather, 
    font=("Arial", 11, "bold"), 
    bg="#007acc", 
    fg="white", 
    activebackground="#005999", 
    activeforeground="white",
    bd=0, 
    padx=10, 
    pady=5
)
search_button.pack(pady=10)

result_label = tk.Label(
    frame, 
    text="", 
    font=("Arial", 11), 
    justify="center", 
    fg="#2c3e50", 
    bg="#f4f4f6", 
    wraplength=300  
)
result_label.pack(pady=15)

root.mainloop()
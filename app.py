import tkinter as tk
from weather import get_weather
import random

root = tk.Tk()
root.title("Weather App")
root.geometry("350x450")  
root.configure(bg="#f4f4f6")  

canvas = tk.Canvas(root, width=350, height=150, bg="skyblue", highlightthickness=0)
canvas.pack()

# --- DYNAMIC IMAGE LOADING ---
character_frames = []
frame_idx = 0
while True:
    try:
        # Automatically extracts frames until it hits the end of the GIF file
        img = tk.PhotoImage(file="runner.gif", format=f"gif -index {frame_idx}")
        character_frames.append(img)
        frame_idx += 1
    except tk.TclError:
        break 

# Fallback in case the GIF file is missing or corrupted
if not character_frames:
    character_frames = [tk.PhotoImage()]

runner = canvas.create_image(50, 110, image=character_frames[0])
current_frame = 0

# --- INFINITE ANIMATION LOOP ---
def animate_runner():
    global current_frame
    
    canvas.itemconfig(runner, image=character_frames[current_frame])
    current_frame = (current_frame + 1) % len(character_frames)
    
    canvas.move(runner, 4, 0)
    pos = canvas.coords(runner)
    
    # Loop character back to the left edge smoothly
    if pos[0] > 380:
        canvas.coords(runner, -30, pos[1]) 
        
    root.after(80, animate_runner)

# --- ENVIRONMENT CYCLES ---
colors = ["#87CEEB", "#FFD700", "#FF8C00", "#191970"] 
bg_index = 0

def cycle_day_night():
    global bg_index
    canvas.config(bg=colors[bg_index])
    bg_index = (bg_index + 1) % len(colors)
    root.after(5000, cycle_day_night)

# --- WEATHER EFFECTS ---
flakes = []
for _ in range(25):
    x = random.randint(0, 350)
    y = random.randint(0, 150)
    r = random.randint(1, 3) 
    flake = canvas.create_oval(x, y, x+r, y+r, fill="white", outline="")
    flakes.append((flake, r)) 

def animate_snow():
    for flake, r in flakes:
        canvas.move(flake, 0, r) 
        pos = canvas.coords(flake)
        if pos[1] > 150:
            canvas.coords(flake, random.randint(0, 350), 0, random.randint(0, 350)+r, r)
    root.after(50, animate_snow)

# Initialize all infinite loops
animate_runner()
cycle_day_night()
animate_snow()

# --- INPUT & INTERFACE ---
frame = tk.Frame(root, padx=20, pady=20, bg="#f4f4f6")
frame.pack(expand=True, fill="both")

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
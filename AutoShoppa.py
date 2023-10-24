import tkinter as tk
import pygetwindow as gw
import pyautogui
import time
import json
import subprocess
from PIL import Image, ImageTk
from tkinter import ttk

# Read the configuration file
with open('./data/config.json', 'r') as config_file:
    config = json.load(config_file)

# Access individual configuration values
target_program_title = config["target_program_title"]
power_butikk = config["power_butikk"]
logo_path = config["logo_path"]
file_path = config["file_path"]
ico_path = config["ico_path"]
search_bar_path = config["search_bar_path"]
info_bar_path = config["info_bar_path"]
maler_path = config["maler_path"]
delay_start = config["delay_start"]
pause_autogui = config["pause_autogui"]
x_width = config["x_width"]
y_height = config["y_height"]
search_plus_x = config["search_plus_x"]
search_plus_y = config["search_plus_y"]
info_plus_x = config["info_plus_x"]
info_plus_y = config["info_plus_y"]

pyautogui.PAUSE = pause_autogui
background_color = "#2a2f32"
root_font = "Roboto"

def Open_txt():
    global file_path, text_widget, root1, root  
    with open(file_path, 'r') as file:
        file_content = file.read()
    root1 = tk.Toplevel(root)
    root1.title("Skann varer her")
    root1.iconbitmap(ico_path)
    root1.attributes("-alpha", 0.98)
    root.attributes("-alpha", 0.93)
    center_window(root1, x_width, y_height)
    root1.update_idletasks()  
    x_offset = root.winfo_x() + root.winfo_width() + 0  
    y_offset = root.winfo_y()
    root1.geometry(f"{x_width}x{y_height}+{x_offset}+{y_offset}")
    text_widget = tk.Text(root1, wrap=tk.WORD)
    text_widget.pack(fill=tk.BOTH, expand=True)
    # Insert the file content into the Text widget
    text_widget.insert(tk.END, file_content)
    text_widget.mark_set(tk.INSERT, "1.0")
    root1.focus_force()
    root1.protocol("WM_DELETE_WINDOW", enable_button1)
    open_button.config(state=tk.DISABLED)
    button1_var.set(True)
    enable_button2()
    button2_var.set(False)
    run_button.config(state=tk.DISABLED)
    text_widget.focus_set()

def save_txt():
    global file_path, text_widget, success_label, root1, counter 
    text_to_save = text_widget.get("1.0", tk.END)
    with open(file_path, 'w') as file:
        file.write(text_to_save)
    counter = 0
    for line in text_to_save.splitlines():
        if line.strip():
            counter += 1
    success_label.config(text=f"{counter} items saved successfully!")
    root.attributes("-alpha", 0.97)
    root1.destroy()
    enable_button3()
    open_button.config(state=tk.NORMAL)

screen_width, screen_height = pyautogui.size()
try:
    maler_button = pyautogui.locateOnScreen(maler_path)
except:
    print("maler png")

def main():
    global counter
    reset_button1_and_2()
    window_title = target_program_title 
    window = gw.getWindowsWithTitle(window_title)
    if counter < 1:
        status_label.config(text="Nothing to print !", fg="#d51f2f")

    if window:
        window = window[0]
        window.activate()  
        window.maximize()  

    active_window = gw.getActiveWindow()

    if active_window is None or active_window.title != target_program_title:
        status_label.config(text="Start Shoppa !", fg="#d51f2f", font=11,)
        root.after(4000, hide_status_message)

    else:
        time.sleep(delay_start)
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip():
                    
                    if maler_button is not None:
                        pyautogui.click(maler_button)
                    else:
                        pyautogui.click(26,57)

                    pyautogui.click(80,95)
                    if bilde == "ja":
                        pyautogui.typewrite("pris og bilde")
                    elif bilde == "nei":
                        pyautogui.typewrite("uten bilde")
                    pyautogui.click(90,150)
                    time.sleep(delay_start)
                    pyautogui.moveTo(100,777)
                    if selected_value==options[0]:
                        pyautogui.scroll(-5000)
                        pyautogui.click(110,933)
                    elif selected_value == options[1]:
                        pyautogui.scroll(-5000)    
                        pyautogui.click(111,861)
                    elif selected_value == options[2]:
                        pyautogui.scroll(-5000)
                        pyautogui.click(106,791)
                    elif selected_value == options[3]:
                        pyautogui.scroll(5000)
                        pyautogui.click(107,861)
                    elif selected_value == options[4]:
                        pyautogui.scroll(5000)
                        pyautogui.click(104,601)
                    elif selected_value == options[5]:
                        pyautogui.scroll(5000)
                        pyautogui.click(99,812)   
                    time.sleep(delay_start)
                    search_bar = pyautogui.locateOnScreen(search_bar_path)
                    if search_bar is not None:
                        center_x = search_bar.left + (search_bar.width / 2)
                        center_y = search_bar.top + (search_bar.height / 2)
                        pyautogui.moveTo(center_x + search_plus_x, center_y - search_plus_y)
                    else:
                        pyautogui.moveTo(x=1043, y=56)
                    time.sleep(delay_start)  
                    pyautogui.doubleClick()
                    pyautogui.typewrite(line.strip())
                    pyautogui.hotkey("enter")
                    time.sleep(delay_start)

                    x_pixel = int(screen_width * 0.900)
                    y_pixel = int(screen_height * 0.275)
                    pixel_color = pyautogui.pixel(x_pixel, y_pixel)

                    time.sleep(delay_start)

                    reference_color = (255, 255, 255)  
                    if pixel_color == reference_color:
                        pyautogui.moveTo(screen_width * 0.945, screen_height * 0.275)
                    else:
                        pyautogui.moveTo(screen_width * 0.945, screen_height * 0.175)

                    pyautogui.mouseDown(button='left')
                    pyautogui.mouseDown(button='right')
                    pyautogui.moveTo(screen_width / 2, screen_height / 2)
                    pyautogui.mouseUp(button='left')
                    pyautogui.mouseUp(button='right')
                            
                    pyautogui.hotkey('ctrl', 'q')
                    
        pyautogui.hotkey('ctrl', 'p')

        file_to_delete = open(file_path,'w')
        file_to_delete.close()
        
        root.after(500, hide_success_message)
        status_label.config(text=f"{counter} items are printing!", fg="#24db4f")
        root.after(5000, hide_status_message)

        window2 = gw.getWindowsWithTitle(power_butikk)
        window2 = window2[0]  
        window2.activate()  

def hide_status_message():
    status_label.config(text="")   

def hide_success_message():
    success_label.config(text="")  

def enable_button1():
    open_button.config(state=tk.NORMAL)
    root1.destroy()
    root.attributes("-alpha", 0.98)
    reset_button1_and_2()
    enable_button2()
    
def enable_button2():
    if button1_var.get():
        save_button.config(state=tk.NORMAL)
    else:
        button2_var.set(False)  
        save_button.config(state=tk.DISABLED)
    enable_button3() 

def enable_button3():
    if  button2_var.get():
        run_button.config(state=tk.NORMAL)
    else:
        run_button.config(state=tk.DISABLED)

def reset_button1_and_2():
    button1_var.set(False) 
    button2_var.set(False)  
    save_button.config(state=tk.DISABLED)
    enable_button3() 

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def on_enter(event):
    widget = event.widget  
    if widget['state'] == tk.NORMAL:
        widget.configure(
            background="#e3e3e3",fg="black"
        )

def on_leave(event):
    widget = event.widget  
    widget.configure(
        background="#f15c25", fg="black"
    )

def on_enter2(event):
    widget = event.widget  
    if widget['state'] == tk.NORMAL:
        widget.configure(
            fg="#f15c25"
        )

def on_leave2(event):
    widget = event.widget  
    widget.configure(
            fg="white"
    )

def have_common_word(str1, str2):
    words1 = set(str1.lower().split())
    words2 = set(str2.lower().split()) 
    return bool(words1.intersection(words2))

def on_combobox_select(event):
    global selected_value
    selected_value = select_box.get()
    print(selected_value)

def update_checkbox_label():
    if checkbox_var.get():
        bilde.set("ja")
        checkbox_label.config(text="Med bilde", fg="white")
    else:
        bilde.set("nei")
        checkbox_label.config(text="Uten bilde", fg="#d6d6d6")

def open_config_app():
    try:
        process = subprocess.Popen(["config.exe"])
        root.withdraw()
        process.wait()  
        root.deiconify() 

    except FileNotFoundError:
        print("Configuration application not found")

text_widget = None
reference_color = (42, 61, 73)

# Create the main window
root = tk.Tk()
root.title(power_butikk)
center_window(root, x_width, y_height)
root.iconbitmap(ico_path)
root.configure(bg = background_color)
root.attributes("-alpha", 0.98)
root.resizable(False,True)
#root.protocol("WM_DELETE_WINDOW", on_closing)

button_style = {
    "font": (root_font, 10,"bold"),  
    "bg": "#f15c25", 
    "fg":"black",
    "activebackground": background_color,
    "activeforeground": "#f15c25",
    "borderwidth": 4,  
    "border": 10, 
    "width": 7,
    "height":1, 
}
label_style = {
    "bg":background_color, 
    "font":(root_font, 9),
}

button1_var = tk.BooleanVar()
button2_var = tk.BooleanVar()

open_insx = tk.Label(root,bg=background_color, font=(root_font, 7))
if have_common_word(target_program_title, power_butikk):
    open_insx.configure(text="✔️", fg= "green")
else:
    open_insx.configure(text="❌",fg= "red")
open_insx.pack(pady=0, anchor="nw", padx=2)
open_insx.bind("<Button-1>", lambda event: open_config_app())

logo_image = Image.open(logo_path)
logo_image = logo_image.resize((260, 75))
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(root, image=logo_photo, bg=background_color)
logo_label.image = logo_photo  
logo_label.pack(pady = 0) 

auto_shoppa = tk.Label(root, text="Auto Shoppa", fg= "white",
     bg=background_color, font=("arial", 9,"bold italic"),)
auto_shoppa.pack(side="top", pady=(0,25))
auto_shoppa.bind("<Enter>",on_enter2)
auto_shoppa.bind("<Leave>",on_leave2)


#open_ins = tk.Label(root, text="Sørg for at du har valgt riktig mal i Shoppa!",
#                     fg= "white", **label_style).pack(pady=10)


open_button = tk.Checkbutton(root, text="Open",variable=button1_var,
                             state=tk.NORMAL, command=Open_txt, **button_style)
open_button.configure(cursor="hand2",relief=tk.FLAT,)
open_button.pack(pady = (0,15))
open_button.bind("<Enter>", on_enter)
open_button.bind("<Leave>", on_leave)

save_button = tk.Checkbutton(root, text="Save",variable=button2_var,
                              state=tk.DISABLED, command=save_txt, **button_style)
save_button.configure(cursor="hand2",relief=tk.FLAT,)
save_button.pack(pady = (15,0))
save_button.bind("<Enter>", on_enter)
save_button.bind("<Leave>", on_leave)

success_label = tk.Label(root, text="", fg="#24db4f", **label_style)
success_label.configure(cursor="hand2",relief=tk.FLAT,)
success_label.pack(pady = 10)

frame_mal = tk.Frame(root,bg="#373d41")
frame_mal.pack(pady=5, padx=1)

checkbox_var = tk.BooleanVar()
checkbox_var.set(False) 
checkbox = tk.Checkbutton(frame_mal, variable=checkbox_var,bg="#373d41", command=update_checkbox_label)
checkbox.grid(row=0, column=1, padx=0,pady=5)

checkbox_label = tk.Label(frame_mal, text="Uten bilde", fg="#d6d6d6", bg="#373d41")
checkbox_label.grid(row=0, column=2, padx=0)

bilde = tk.StringVar()
bilde.set("ja")

custom_style = ttk.Style()
custom_style.theme_use('alt')
custom_style.configure("Custom.TCombobox",
    font=("Roboto"),
    background="#495783",
    selectbackground="#d7d6d6",
    selectforeground="black",
    padding=(5, 1, 5, 1)
)

options = ["Piggetikett", "Hyllekant", "Stor hyllekant", "Halv A4", "Stående A4", "Liggende A4"]
selected_option = tk.StringVar()
select_box = ttk.Combobox(frame_mal, textvariable=selected_option, values=options, state="readonly", style="Custom.TCombobox")
select_box.grid(row=0, column=3, padx=5)
select_box.set(options[0])
selected_value=select_box.get()
print(selected_value)
select_box.bind("<<ComboboxSelected>>", on_combobox_select)


run_button = tk.Button(
    root,
    text="Start Auto Shoppa",
    bg="#f15c25",
    fg="black",
    font=(root_font,10,"bold"),
    cursor="hand2",
    command=main,
    relief=tk.FLAT,  
    borderwidth=2,
    width=22,
    height=3,  
    state=tk.DISABLED,
)

run_button.configure(cursor="hand2")
run_button.pack(pady = 15)
run_button.bind("<Enter>", on_enter)
run_button.bind("<Leave>", on_leave)

status_label = tk.Label(root, text="")
status_label.configure(cursor="dot", fg= "#f15c25", **label_style)
status_label.pack(pady = 5)

signature_label = tk.Label(root, text="Made with 🖤 by Wael for Power")
signature_label.configure(cursor="heart", bg=background_color, fg="white", font=(root_font, 10))
signature_label.pack(side="bottom", pady = 5)
signature_label.bind("<Enter>", on_enter2)
signature_label.bind("<Leave>", on_leave2)

root.mainloop()
import tkinter as tk
from button_info_details import button_info
from tkinter.font import Font
from functools import partial
from time import sleep


window = tk.Tk()
window.title("Calculator")
window.geometry("314x422")
window.resizable(False, False)

window.iconbitmap("C:\\Users\\ASHWIN\\Desktop\\python\\project1\\Calculator_30001.ico")
#window.overrideredirect(True)
#title_bar=tk.Frame(window, bg="blue", relief="raised", bd=0)
#title_bar.pack(fill="x")

max_length = 26
def validate_text(*args):
    current_text = text_area.get("1.0", "end-1c")  # Get the current text in the text box
    if len(current_text) >= max_length:
        text_area.delete("end-2c", "end-1c")  # Delete the last character if the limit is reached
    if text_area.get("end-2c", "end-1c") == "=":
        text_area.delete("end-2c", "end-1c") 
        cal_exp = text_area.get("1.0", "end-1c")
        try:
            text_area.delete("1.0", "end")
            text_area.insert("end",eval(cal_exp))
        except:
            text_area.delete("1.0", "end")
            text_area.insert("end","Invalid Input!!!")

    if text_area.get("end-2c", "end-1c") not in "1234567890+-%/*().":
        text_area.delete("end-2c", "end-1c")

def button_click_info(button_value):
    if button_value in "1234567890().+-/*%":
        text_area.insert("end",button_value)
        pass
    elif button_value == "=":
        cal_exp = text_area.get("1.0", "end-1c")
        try:
            text_area.delete("1.0", "end")
            text_area.insert("end",eval(cal_exp))
        except:
            text_area.delete("1.0", "end")
            text_area.insert("end","Invalid Input!!!")
    elif button_value == "D":
        text_area.delete("end-2c", "end-1c")
    elif button_value == "C":
        text_area.delete("1.0", "end")
    else:
        pass




text_area = tk.Text(window, width=33, height=2, bg="white",fg="black", font=("Arial",20))
text_area.place(x=0,y=0)
text_area.pack()

# Bind a validation function to the text box
text_area.bind("<KeyRelease>", validate_text)



x_axis_button = 2
y_axis_button = 76
button_number = 0

for x_axis in range(5): 
    for y_axis in range(4):
        button_number +=1
        button = tk.Button(window, text=button_info[str(button_number)]["text"],
                   relief="raised",   # Set the button relief to "raised"
                   bg=button_info[str(button_number)]["bg"],      # Set the background color to a blue shade
                   fg=button_info[str(button_number)]["fg"],        # Set the text color to white
                   font=Font(size="12",weight="bold"),
                   anchor="center",
                   width=7,          # Set the button width
                   height=3,          # Set the button height
                   bd=4,
                   command=partial(button_click_info, button_info[str(button_number)]["text"])
        )
        button.place(x = x_axis_button, y=y_axis_button)
        x_axis_button +=75
    y_axis_button += 67
    x_axis_button = 2

window.mainloop()
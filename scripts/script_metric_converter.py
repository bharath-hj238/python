import tkinter

factors_dict = {
    "km_miles": ["km", "miles", "KM-to-Miles"],
    "kg_pound": ["kg", "pounds", "KG-to-Pounds"],
    "cel_far": ["celsius", "fahrenheit", "Celsius-to-Fahrenheit"],
    "feet_cm": ["feet", "cm", "Feet-to-Centimeter"]
}


def km_miles():
    from_label.config(text="km")
    to_label.config(text="miles")
    result_label.config(text="...")


def kg_pound():
    from_label.config(text="kg")
    to_label.config(text="pound")
    result_label.config(text="...")


def cel_far():
    from_label.config(text="celsius")
    to_label.config(text="fahrenheit")
    result_label.config(text="...")


def feet_cm():
    from_label.config(text="feet")
    to_label.config(text="cm")
    result_label.config(text="...")


def converter():
    user_data = float(data_input.get())
    if radio_state.get() == 1:
        converted_data = round(user_data * 1.609, 3)
    elif radio_state.get() == 2:
        converted_data = round(user_data * 2.205, 3)
    elif radio_state.get() == 3:
        converted_data = round((user_data * 1.8) + 32, 3)
    elif radio_state.get() == 4:
        converted_data = round(user_data * 30.48, 3)
    else:
        print("Error")
        exit(0)
    result_label.config(text=f"{converted_data}", font=("Arial", 14, "bold"))


def radio_used():
    if radio_state.get() == 1:
        km_miles()
    elif radio_state.get() == 2:
        kg_pound()
    elif radio_state.get() == 3:
        cel_far()
    elif radio_state.get() == 4:
        feet_cm()
    else:
        print("Error")
        exit(0)


window = tkinter.Tk()
window.title("Converter")
window.config(pady=25)
window.minsize(width=350, height=250)

radio_index = 0
row = 0
radio_state = tkinter.IntVar()
for key, value in factors_dict.items():
    radio_index += 1
    row += 1
    select_data = tkinter.Radiobutton(text=factors_dict[key][2], value=radio_index, variable=radio_state,
                                      command=radio_used)
    select_data.grid(column=0, row=row)

data_input = tkinter.Entry(width=7)
data_input.grid(column=0, row=row + 4, padx=10)

from_label = tkinter.Label(text="...")
from_label.grid(column=1, row=row + 4)

result_label = tkinter.Label(text="0")
result_label.grid(column=0, row=row + 6)

to_label = tkinter.Label(text="...")
to_label.grid(column=1, row=row + 6)

calculate_button = tkinter.Button(text="Calculate", fg="blue", command=converter)
calculate_button.grid(column=1, row=row + 8)

window.mainloop()

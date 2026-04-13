import tkinter as tk
from tkinter import ttk
import time

# ---------- GLOBAL ----------
credits = "Created by @Dhruvjangid"

Unit_Tuple = ("Mili", "Centi", "Deci", "", "Deca", "Hecto", "Kilo")
Unit_Number_Tuple = (1, 2, 3, 4, 5, 6, 7)
Unit_Dictionary = dict(zip(Unit_Tuple, Unit_Number_Tuple))


# ---------- MAIN PREFIX CONVERTER ----------
def main_converter(unit_name, window, p, q):

    def unit_names():
        return tuple(i + unit_name for i in Unit_Tuple)

    frame = tk.Frame(window, bg="#f5f7fa")
    frame.pack(pady=40)

    value1 = tk.DoubleVar()
    value2 = tk.DoubleVar()
    unit1 = tk.StringVar()
    unit2 = tk.StringVar()

    def convert(*args):
        try:
            a = Unit_Dictionary.get((unit1.get())[p:q])
            b = Unit_Dictionary.get((unit2.get())[p:q])
            value2.set(value1.get() * (10 ** (a - b)))
        except:
            value2.set(0)

    tk.Entry(frame, textvariable=value1, font=("Segoe UI", 12)).grid(row=0, column=0, padx=10, pady=10)

    combo1 = ttk.Combobox(frame, textvariable=unit1, values=unit_names(), state="readonly")
    combo1.grid(row=0, column=1)

    combo2 = ttk.Combobox(frame, textvariable=unit2, values=unit_names(), state="readonly")
    combo2.grid(row=1, column=1)

    tk.Label(frame, textvariable=value2, bg="#e3f2fd", width=15).grid(row=1, column=0)

    combo1.current(3)
    combo2.current(6)
    value1.set(1)

    value1.trace_add("write", convert)
    unit1.trace_add("write", convert)
    unit2.trace_add("write", convert)


# ---------- WINDOW ----------
def create_window(title):
    win = tk.Toplevel()
    win.geometry("420x420")
    win.title(title)
    win.configure(bg="#f5f7fa")

    tk.Label(win, text=title, font=("Segoe UI", 18, "bold"),
             bg="#f5f7fa").pack(pady=20)

    status = tk.Label(win, bg="#222", fg="white")
    status.pack(side="bottom", fill="x")

    def clock():
        status.config(text=time.strftime("%I:%M:%S %p"))
        win.after(1000, clock)

    clock()
    return win


# ---------- BASIC ----------
def Weight():
    win = create_window("Weight Converter")
    main_converter("Gram", win, 0, -4)

def Length():
    win = create_window("Length Converter")
    main_converter("Metre", win, 0, -5)

def Volume():
    win = create_window("Volume Converter")
    main_converter("Litre", win, 0, -5)


# ---------- ANGLE ----------
def Circle():
    win = create_window("Angle Converter")

    val1 = tk.DoubleVar()
    val2 = tk.DoubleVar()
    unit1 = tk.StringVar()
    unit2 = tk.StringVar()

    units = ["Degrees", "Radians"]

    def convert(*args):
        try:
            v = val1.get()
            if unit1.get() == "Degrees" and unit2.get() == "Radians":
                val2.set(v * 3.14159 / 180)
            elif unit1.get() == "Radians" and unit2.get() == "Degrees":
                val2.set(v * 180 / 3.14159)
            else:
                val2.set(v)
        except:
            val2.set(0)

    frame = tk.Frame(win, bg="#f5f7fa")
    frame.pack(pady=40)

    tk.Entry(frame, textvariable=val1).grid(row=0, column=0, padx=10)
    ttk.Combobox(frame, textvariable=unit1, values=units, state="readonly").grid(row=0, column=1)
    ttk.Combobox(frame, textvariable=unit2, values=units, state="readonly").grid(row=1, column=1)
    tk.Label(frame, textvariable=val2, bg="#e3f2fd", width=15).grid(row=1, column=0)

    unit1.set(units[0])
    unit2.set(units[1])

    val1.trace_add("write", convert)
    unit1.trace_add("write", convert)
    unit2.trace_add("write", convert)


# ---------- TEMPERATURE ----------
def Temperature():
    win = create_window("Temperature Converter")

    val1 = tk.DoubleVar()
    val2 = tk.DoubleVar()
    unit1 = tk.StringVar()
    unit2 = tk.StringVar()

    units = ["Celsius", "Fahrenheit", "Kelvin"]

    def convert(*args):
        try:
            v = val1.get()

            if unit1.get() == "Celsius":
                if unit2.get() == "Fahrenheit":
                    val2.set((v * 9/5) + 32)
                elif unit2.get() == "Kelvin":
                    val2.set(v + 273.15)

            elif unit1.get() == "Fahrenheit":
                if unit2.get() == "Celsius":
                    val2.set((v - 32) * 5/9)
                elif unit2.get() == "Kelvin":
                    val2.set((v - 32) * 5/9 + 273.15)

            elif unit1.get() == "Kelvin":
                if unit2.get() == "Celsius":
                    val2.set(v - 273.15)
                elif unit2.get() == "Fahrenheit":
                    val2.set((v - 273.15) * 9/5 + 32)
            else:
                val2.set(v)

        except:
            val2.set(0)

    frame = tk.Frame(win, bg="#f5f7fa")
    frame.pack(pady=40)

    tk.Entry(frame, textvariable=val1).grid(row=0, column=0)
    ttk.Combobox(frame, textvariable=unit1, values=units, state="readonly").grid(row=0, column=1)
    ttk.Combobox(frame, textvariable=unit2, values=units, state="readonly").grid(row=1, column=1)
    tk.Label(frame, textvariable=val2, bg="#e3f2fd", width=15).grid(row=1, column=0)

    unit1.set(units[0])
    unit2.set(units[1])

    val1.trace_add("write", convert)
    unit1.trace_add("write", convert)
    unit2.trace_add("write", convert)


# ---------- SPEED ----------
def Speed():
    win = create_window("Speed Converter")

    val1 = tk.DoubleVar()
    val2 = tk.DoubleVar()
    unit1 = tk.StringVar()
    unit2 = tk.StringVar()

    units = ["kph", "mph", "kt"]

    def convert(*args):
        try:
            v = val1.get()

            if unit1.get() == "mph":
                v *= 1.60934
            elif unit1.get() == "kt":
                v *= 1.852

            if unit2.get() == "mph":
                val2.set(v / 1.60934)
            elif unit2.get() == "kt":
                val2.set(v / 1.852)
            else:
                val2.set(v)

        except:
            val2.set(0)

    frame = tk.Frame(win, bg="#f5f7fa")
    frame.pack(pady=40)

    tk.Entry(frame, textvariable=val1).grid(row=0, column=0)
    ttk.Combobox(frame, textvariable=unit1, values=units, state="readonly").grid(row=0, column=1)
    ttk.Combobox(frame, textvariable=unit2, values=units, state="readonly").grid(row=1, column=1)
    tk.Label(frame, textvariable=val2, bg="#e3f2fd", width=15).grid(row=1, column=0)

    unit1.set(units[0])
    unit2.set(units[1])

    val1.trace_add("write", convert)
    unit1.trace_add("write", convert)
    unit2.trace_add("write", convert)


# ---------- MAIN WINDOW ----------
root = tk.Tk()
root.geometry("420x500")
root.title("Unit Converter")
root.configure(bg="#f5f7fa")

tk.Label(root, text="Unit Converter", font=("Segoe UI", 22, "bold"),
         bg="#f5f7fa").pack(pady=30)

tk.Label(root, text="Select Conversion Type",
         font=("Segoe UI", 12), bg="#f5f7fa").pack(pady=10)

btn_frame = tk.Frame(root, bg="#f5f7fa")
btn_frame.pack(pady=20)

def btn(text, cmd):
    tk.Button(btn_frame, text=text, command=cmd,
              font=("Segoe UI", 11, "bold"),
              bg="#4CAF50", fg="white",
              width=20, height=2).pack(pady=3)

btn("Weight", Weight)
btn("Length", Length)
btn("Volume", Volume)
btn("Angle", Circle)
btn("Temperature", Temperature)
btn("Speed", Speed)

tk.Label(root, text=credits, bg="#f5f7fa",
         fg="gray").pack(side="bottom", pady=10)

root.mainloop()
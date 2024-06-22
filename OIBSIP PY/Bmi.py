import tkinter as tk

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get()) / 100  
    bmi = weight / (height ** 2)
    bmi = round(bmi, 2)  

    if bmi < 18.5:
        category = 'Underweight'
    elif 18.5 <= bmi < 25:
        category = 'Normal weight'
    elif 25 <= bmi < 30:
        category = 'Overweight'
    else:
        category = 'Obesity'

    result_label.config(text=f"BMI: {bmi} ({category})")

root = tk.Tk()
root.title("BMI Calculator")


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

tk.Label(root, text="Enter your weight (kg):").grid(row=0, column=0)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1)

tk.Label(root, text="Enter your height (cm):").grid(row=1, column=0)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1)

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2)


result_label = tk.Label(root, text="", font=('Helvetica', 12, 'bold'))
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()

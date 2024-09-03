import tkinter as tk

def calculate_bmi():
    # Get values from the entries
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    # Calculate BMI: BMI = weight (kg) / (height (m))^2
    bmi = weight / (height / 100) ** 2
    # Update the result label
    result_label.config(text=f"BMI: {bmi:.2f}")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create and pack the widgets
weight_label = tk.Label(root, text="Enter your weight (in kg):")
weight_label.pack()

weight_entry = tk.Entry(root)
weight_entry.pack()

height_label = tk.Label(root, text="Enter your height (in cm):")
height_label.pack()

height_entry = tk.Entry(root)
height_entry.pack()

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

result_label = tk.Label(root, text="BMI: ")
result_label.pack()

# Start the GUI event loop
root.mainloop()

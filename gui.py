import tkinter as tk
import threading

def fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

def calculate_fib():
    try:
        n = int(entry.get())
        if n < 0:
            result_label.config(text="Zadejte kladné číslo!", fg="red")
            return
    except ValueError:
        result_label.config(text="Neplatný vstup!", fg="red")
        return

    def worker():
        result = fib(n)
        result_label.after(0, lambda: result_label.config(text=f"{n}. Fibonacci: {result}", fg="black"))

    threading.Thread(target=worker).start()

# Vytvoření hlavního okna
root = tk.Tk()
root.title("Fibonacci Calculator")

# Hlavní rámec
main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack()

# Rámeček pro vstup
input_frame = tk.Frame(main_frame)
input_frame.grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(input_frame, text="Zadejte číslo n:").grid(row=0, column=0, padx=5)
entry = tk.Entry(input_frame, width=10)
entry.grid(row=0, column=1, padx=5)

# Rámeček pro tlačítka
button_frame = tk.Frame(main_frame)
button_frame.grid(row=1, column=0, columnspan=2, pady=10)

button_compute = tk.Button(button_frame, text="Spočítej Fibonacciho číslo", command=calculate_fib)
button_compute.grid(row=0, column=0, padx=5)

button_quit = tk.Button(button_frame, text="Ukončit", command=root.quit)
button_quit.grid(row=0, column=1, padx=5)

# Výsledek
result_label = tk.Label(main_frame, text="Výsledek se zobrazí zde", font=("Arial", 12))
result_label.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()

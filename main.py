import random
import tkinter as tk
from tkinter import messagebox


def check_guess():
    try:
        guess = int(entry.get())
        global attempts
        attempts += 1

        if guess < number_to_guess:
            result_label.config(text="Too low! Try again.")
        elif guess > number_to_guess:
            result_label.config(text="Too high! Try again.")
        else:
            messagebox.showinfo("Congratulations!", f"You guessed the number in {attempts} attempts.")
            root.quit()
    except ValueError:
        result_label.config(text="Invalid input! Please enter a number.")


def number_guessing_game():
    global number_to_guess, attempts, root, entry, result_label
    number_to_guess = random.randint(1, 100)
    attempts = 0

    root = tk.Tk()
    root.title("Number Guessing Game")

    tk.Label(root, text="Guess the number (between 1 and 100):").pack(pady=10)
    entry = tk.Entry(root)
    entry.pack(pady=5)

    tk.Button(root, text="Submit", command=check_guess).pack(pady=5)
    result_label = tk.Label(root, text="")
    result_label.pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    number_guessing_game()

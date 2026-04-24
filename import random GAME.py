import tkinter as tk
from tkinter import messagebox
import random


class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x300")

        self.min_num = 1
        self.max_num = 100
        self.attempts = 7

        self.start_new_game()

        # Title
        self.title_label = tk.Label(
            root,
            text="Number Guessing Game",
            font=("Arial", 16, "bold")
        )
        self.title_label.pack(pady=10)

        # Info label
        self.info_label = tk.Label(
            root,
            text=f"Guess a number between {self.min_num} and {self.max_num}",
            font=("Arial", 12)
        )
        self.info_label.pack(pady=5)

        # Attempts label
        self.attempts_label = tk.Label(
            root,
            text=f"Attempts Left: {self.attempts_left}",
            font=("Arial", 11)
        )
        self.attempts_label.pack(pady=5)

        # Entry box
        self.guess_entry = tk.Entry(root, font=("Arial", 12))
        self.guess_entry.pack(pady=10)

        # Submit button
        self.submit_button = tk.Button(
            root,
            text="Submit Guess",
            command=self.check_guess,
            font=("Arial", 11)
        )
        self.submit_button.pack(pady=5)

        # Result label
        self.result_label = tk.Label(
            root,
            text="",
            font=("Arial", 12),
            fg="blue"
        )
        self.result_label.pack(pady=10)

        # Restart button
        self.restart_button = tk.Button(
            root,
            text="Play Again",
            command=self.restart_game,
            font=("Arial", 11)
        )
        self.restart_button.pack(pady=5)

    def start_new_game(self):
        self.number = random.randint(self.min_num, self.max_num)
        self.attempts_left = self.attempts

    def check_guess(self):
        guess = self.guess_entry.get()

        # Validate input
        if not guess.isdigit():
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return

        guess = int(guess)

        # Check range
        if guess < self.min_num or guess > self.max_num:
            messagebox.showwarning(
                "Out of Range",
                f"Enter a number between {self.min_num} and {self.max_num}."
            )
            return

        self.attempts_left -= 1
        self.attempts_label.config(
            text=f"Attempts Left: {self.attempts_left}"
        )

        # Compare guess
        if guess < self.number:
            self.result_label.config(text="Too low!")
        elif guess > self.number:
            self.result_label.config(text="Too high!")
        else:
            messagebox.showinfo(
                "Congratulations",
                f"You guessed the number correctly!"
            )

            # Increase difficulty
            self.max_num += 50
            self.restart_game()
            return

        # Game over
        if self.attempts_left == 0:
            messagebox.showinfo(
                "Game Over",
                f"You lost! The number was {self.number}"
            )

            self.restart_game()

        self.guess_entry.delete(0, tk.END)

    def restart_game(self):
        self.start_new_game()

        self.info_label.config(
            text=f"Guess a number between {self.min_num} and {self.max_num}"
        )

        self.attempts_label.config(
            text=f"Attempts Left: {self.attempts_left}"
        )

        self.result_label.config(text="")
        self.guess_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
import tkinter as tk
from tkinter import messagebox
import random

def guess_the_number(difficulty):
    number_of_tries = 3
    number_to_find = random.randint(1, difficulty + 5)

    def check_guess():
        nonlocal number_of_tries
        chosen_number = int(entry.get())
        if chosen_number == number_to_find:
            messagebox.showinfo("Congratulations", "Chosen number is correct, you win!")
            reset = messagebox.askyesno("Play Again", "Wanna play again?")
            if reset:
                window.destroy()
                start_game()
            else:
                window.destroy()
        else:
            messagebox.showinfo("Incorrect", "Entered number is incorrect, try again.")
            number_of_tries -= 1
            tries_label.config(text=f"You have {number_of_tries} tries left.")
            entry.delete(0, tk.END)
            if number_of_tries == 0:
                messagebox.showinfo("Game Over", "Oops, it seems that you lose.")
                again = messagebox.askyesno("Play Again", "Wanna play again?")
                if again:
                    window.destroy()
                    start_game()
                else:
                    window.destroy()

    window = tk.Tk()
    window.title("Guess The Number")

    label = tk.Label(window, text=f"Choose a number between 1 and {difficulty + 5}")
    label.pack(pady=10)

    entry = tk.Entry(window)
    entry.pack(pady=10)

    submit_button = tk.Button(window, text="Submit", command=check_guess)
    submit_button.pack(pady=10)

    tries_label = tk.Label(window, text=f"You have {number_of_tries} tries left.")
    tries_label.pack(pady=10)

    window.mainloop()

def start_game():
    main_window = tk.Tk()
    main_window.title("Guess The Number")

    label = tk.Label(main_window, text="Hello mate, wanna play a Guess the number game?")
    label.pack(pady=10)

    play_button = tk.Button(main_window, text="Yes", command=lambda: guess_the_number(difficulty_var.get()))
    play_button.pack(pady=10)

    exit_button = tk.Button(main_window, text="No", command=main_window.destroy)
    exit_button.pack(pady=10)

    difficulty_var = tk.IntVar()
    difficulty_var.set(1)

    difficulty_label = tk.Label(main_window, text="Choose the difficulty:")
    difficulty_label.pack()

    easy_radio = tk.Radiobutton(main_window, text="Easy", variable=difficulty_var, value=1)
    easy_radio.pack()

    medium_radio = tk.Radiobutton(main_window, text="Medium", variable=difficulty_var, value=2)
    medium_radio.pack()

    hard_radio = tk.Radiobutton(main_window, text="Hard", variable=difficulty_var, value=3)
    hard_radio.pack()

    impossible_radio = tk.Radiobutton(main_window, text="Impossible", variable=difficulty_var, value=4)
    impossible_radio.pack()

    main_window.mainloop()

if __name__ == "__main__":
    start_game()

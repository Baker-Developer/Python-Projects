import random
import tkinter as tk

class GuessingGame(tk.Tk):
    def __init__(self):
        super().__init__()

        # Generate a random number to be guessed
        self.secret_num = random.randint(1, 10)

        # Create the user interface
        self.name_label = tk.Label(self, text="Name:")
        self.name_input = tk.Entry(self)
        self.guess_label = tk.Label(self, text="Guess:")
        self.guess_input = tk.Entry(self)
        self.submit_button = tk.Button(self, text="Submit", command=self.check_guess)
        self.output_label = tk.Label(self, text="")

        # Set up the layout
        self.name_label.pack()
        self.name_input.pack()
        self.guess_label.pack()
        self.guess_input.pack()
        self.submit_button.pack()
        self.output_label.pack()

    def check_guess(self):
        # Get the user's name and guess
        name = self.name_input.get()
        guess = int(self.guess_input.get())

        # Check if the guess is correct
        if guess == self.secret_num:
            result = f"Congratulations, {name}! You guessed the correct number: {guess}"
        else:
            result = f"Sorry, {name}. Your guess of {guess} is incorrect. Please try again."

        # Display the result
        self.output_label.config(text=result)

if __name__ == "__main__":
    app = GuessingGame()
    app.mainloop()

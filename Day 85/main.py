import tkinter as tk
from datetime import datetime

class TypingSpeedTester(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Typing Speed Tester")

        self.sample_text = "The quick brown fox jumps over the lazy dog"
        self.start_time = None
        self.input_text = None

        self.create_widgets()

    def create_widgets(self):
        # Sample text
        self.sample_label = tk.Label(self.master, text=self.sample_text)
        self.sample_label.pack()

        # Input text
        self.input_text = tk.Text(self.master, height=5)
        self.input_text.pack()

        # Start button
        self.start_button = tk.Button(self.master, text="Start", command=self.start_timer)
        self.start_button.pack()

        # Result label
        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack()

    def start_timer(self):
        self.start_time = datetime.now()
        self.start_button.config(state="disabled")

    def calculate_speed(self):
        input_text = self.input_text.get("1.0", tk.END)
        input_words = input_text.split()
        elapsed_time = datetime.now() - self.start_time
        minutes = elapsed_time.seconds / 60
        wpm = len(input_words) / minutes
        return wpm

    def show_result(self):
        wpm = self.calculate_speed()
        result_text = f"You typed {round(wpm, 2)} words per minute"
        self.result_label.config(text=result_text)

    def on_enter(self, event):
        self.show_result()
        self.input_text.config(state="disabled")

root = tk.Tk()
app = TypingSpeedTester(master=root)
app.input_text.bind("<Return>", app.on_enter)
app.mainloop()

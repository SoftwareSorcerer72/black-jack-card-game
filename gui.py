import tkinter as tk

class BlackjackGui:
    def __init__(self, root):
        self.root = root
        root.title("Blackjack")

        self.player_label = tk.Label(root, text="Your hand:")
        self.player_label.pack()

        
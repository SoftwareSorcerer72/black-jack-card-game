import tkinter as tk

class BlackjackGui:
    def __init__(self, root):
        self.root = root
        root.title("Blackjack")

        # sets window size
        root.geometry("800x600")

        # sets background color
        root.configure(bg='green')

        self.player_label = tk.Label(root, text="Your hand:")
        self.player_label.pack()

        self.dealer_label = tk.Label(root, text="Dealer's hand:")
        self.dealer_label.pack()

        self.hit_button = tk.Button(root, text="Hit", command=self.hit)
        self.hit_button.pack()

        self.stand_button = tk.Button(root, text="Stand", command=self.stand)
        self.stand_button.pack()

    def hit(self):
        pass

    def stand(self):
        pass

root = tk.Tk()
gui = BlackjackGui(root)
root.mainloop()

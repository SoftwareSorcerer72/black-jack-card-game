# import tkinter as tk
# import random
# from main import Card, Deck, Player, Dealer
# class BlackjackGui:
#     def __init__(self, root):
#         self.root = root
#         root.title("Blackjack")

#         # sets window size
#         root.geometry("800x600")

#         # sets background color
#         root.configure(bg='green')

#         self.player_label = tk.Label(root, text="Your hand:", bg='green', fg='white')
#         self.player_label.pack()

#         self.dealer_label = tk.Label(root, text="Dealer's hand:", bg='green', fg='white')
#         self.dealer_label.pack()

#         self.hit_button = tk.Button(root, text="Hit", command=self.hit)
#         self.hit_button.pack()

#         self.stand_button = tk.Button(root, text="Stand", command=self.stand)
#         self.stand_button.pack()

#         #creating game objects
        
#         #shuffles the deck    
#         self.deck = Deck()
#         random.shuffle(self.deck.cards)
#         self.player = Player()
#         self.dealer = Dealer()
#         for _ in range(2):
#             self.deck.deal(self.player)
#             self.deck.deal(self.dealer)

#         self.update_labels()
#     def update_labels(self):
#         self.

        
#     def hit(self):
#         pass

#     def stand(self):
#         pass



# # player turn (from main)
# while True:
#     print(f"Your hand: {[card.rank for card in player.hand]} with a total of {player.calculate_hand()}")
#     if player.calculate_hand() > 21:
#         print("You bust! The dealer wins.")
#         break
#     should_continue = input("Would you like to hit or stand? (h/s): ")
#     if should_continue.lower().strip() == "h":
#         deck.deal(player)
#     else:
#         break

# # dealers turn (from main)
# if player.calculate_hand() <= 21:
#     while dealer.should_hit():
#         deck.deal(dealer)
#     print(f"Dealer's hand: {[card.rank for card in dealer.hand]} with a total of {dealer.calculate_hand()}")
#     if dealer.calculate_hand() > 21 or dealer.calculate_hand() < player.calculate_hand():
#         print("The Dealer Busts! You Win!")
#     elif dealer.calculate_hand() > player.calculate_hand():
#         print("The Dealer wins!")
#     else:
#         print("It's a tie")
    
    







# root = tk.Tk()
# gui = BlackjackGui(root)
# root.mainloop()

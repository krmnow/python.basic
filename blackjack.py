import random

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']

    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppn'
        
    for suit in suits:
        
        for card in range(1, 11):
            name = "cards{}_{}_{}".format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))

        for card in face_cards:
            name = "cards{}_{}_{}".format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10,image,))

def deal_card(frame):
    #pop next cart on top
    next_card = deck.pop(0)
    deck.append(next_card)
    # add image
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    return next_card

def score_hand(hand):
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        if score > 21 and ace:
            score -= 10
            ace = False
    return score

def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_score = score_hand(dealer_hand)
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score_label.set(dealer_score)
    
    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer wins")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.srt("Player wins")
    elif dealer_score > player_score:
        result_text.set("Dealer wins")
    else:
        result_text.set("Dealer wins")

def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)
    
    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer wins")
    

def new_game():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand
   #embaded frame on hold card images
   dealer_card_frame.destroy()
   dealer_card_frame = tkinter.Frame(card_frame, background-"green")
   dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)
   #embede frame to hold the card images
   dealer_card_frame = tkinter.Frame(card_frame, background="green")
   dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

    result_text.set("")

    dealer_hand = []
    player_hand = []

    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()
    
# Set up the screen

def shuffle():
    random.shuffle(deck)


mainWindow = tkinter.Tk()

mainWindow.title("Black jack")
mainWindow.geometry("640x480")
mainWindow.configure(background="green")


result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)
card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)
 
dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

#embedded frame hold the card image
 
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

player_score_label = tkinter.IntVar()



tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)

#embeded frame to holf the card images

player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, sticky="w", text="dealer")

dealer_button = tkinter.Button(button_frame, text="deaaler", command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="Player", command=deal_player)
player_button.grid(row=0, column=1)

new_game_buttton = tkinter.Button(button_frame, text="new game", command=new_game)
new_game_buttton.grid(row=0, column=2)

shuffle_button = tkinter.Button(button_frame, text="shuffle", command=shuffle)
shuffle_button.grid(row=0, column=3)
cards = []
load_images(cards)
deck = list(cards)
shuffle()

dealer_hand = []
player_hand = []

 
mainWindow.mainloop()




import tkinter as tk
from PIL import Image, ImageTk

#List of Options for user to choose from
strikers = [
    {"name": "Cristiano Ronaldo", "goals": 873, "img":"Photos/Ronaldo.png"},
    {"name": "Lionel Messi", "goals": 819, "img": "Photos/Messi.png"},
    {"name": "Robert Lewandowski", "goals": 630, "img":"Photos/Lewandowski.png"},
    {"name": "Zlatan Ibrahimović", "goals": 570, "img": "Photos/Ibrahimovic.png"},
    {"name": "Johan Cruyff", "goals": 258, "img": "Photos/Cruyff.png"},
    {"name": "Pelé", "goals": 767, "img": "Photos/Pele.png"},
]

#Function
def faceOff():
    p1 = player_var.get()
    p2 = opponent_var.get()

    if p1 == p2:
        result_label.config(text="It's a tie! You chose the same player!.")
        return 
    
    #Find Player Dictionaries
    player1 = next(item for item in strikers if item["name"] == p1)
    player2 = next(item for item in strikers if item["name"] == p2)

    # Load and resize player1 image
    img1 = Image.open(player1["img"])
    img1 = img1.resize((250, 250)) 
    photo1 = ImageTk.PhotoImage(img1)

    # Load and resize player2 image
    img2 = Image.open(player2["img"])
    img2 = img2.resize((250, 250))
    photo2 = ImageTk.PhotoImage(img2)

    # Update Labels
    player1_label.config(image=photo1)
    player1_label.image = photo1

    player2_label.config(image=photo2)
    player2_label.image = photo2

    #If statements to determine the winner of the faceoff
    if player1["goals"] > player2 ["goals"]:
        result  = f"{player1["name"]} wins with {player1["goals"]} goals!"
    elif player1["goals"] < player2 ["goals"]:
        result  = f"{player2["name"]} wins with {player2["goals"]} goals!"
    else:
        result =  f"It's a tie! Both scored {player1["goals"]} goals!"

    result_label.config(text=result)

root = tk.Tk()
root.title("Striker Faceoff")


#Variables
player_var = tk.StringVar(root)
player_var.set(strikers[0]["name"]) #Default Value

opponent_var = tk.StringVar(root)
opponent_var.set(strikers[1]["name"]) #Default Value

#Player Dropdown 
tk.Label(root,text="Choose your player:").pack()
player_menu = tk.OptionMenu(root, player_var, * [s["name"]for s in strikers])
player_menu.pack()

#Opponent Dropdown
tk.Label(root,text="Choose your opponent:").pack()
opponent_menu = tk.OptionMenu(root, opponent_var, * [s["name"]for s in strikers])
opponent_menu.pack()

#Faceoff Option
faceoff_button = tk.Button(root, text="Face Off!", command=faceOff)
faceoff_button.pack()

#Creating Labels for player images
player1_label = tk.Label(root)
player1_label.pack(side = "left", padx=10)

player2_label = tk.Label(root)
player2_label.pack(side = "right", padx=10)

#Label for result
result_label=tk.Label(root, text = "", font = ("Comic Sans MS",20))
result_label.pack(pady=20)

root.mainloop()
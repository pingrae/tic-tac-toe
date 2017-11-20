from tkinter import *

def checked(i) :
      global player
      button = list[i]

      if button["text"] != "     " :
            return
      button["text"] = player 
      button["bg"] = "yellow"

      if player == "X" :
            player = "O"
            button["bg"] = "yellow"
      else :
            player = "X"
            button["bg"] = "lightgreen"

      if list[0]["text"] == list[1]["text"] == list[2]["text"] != "     ":
            winner()
      if list[3]["text"] == list[4]["text"] == list[5]["text"] != "     ":
            winner()
      if list[6]["text"] == list[7]["text"] == list[8]["text"] != "     ":
            winner()
      if list[0]["text"] == list[3]["text"] == list[6]["text"] != "     ":
            winner()
      if list[1]["text"] == list[4]["text"] == list[7]["text"] != "     ":
            winner()
      if list[2]["text"] == list[5]["text"] == list[8]["text"] != "     ":
            winner()
      if list[0]["text"] == list[4]["text"] == list[8]["text"] != "     ":
            winner()
      if list[2]["text"] == list[4]["text"] == list[6]["text"] != "     ":
            winner()

def winner() :
      global  player, winner_flag
      if winner_flag == False:
            if player == "X":
                  text = Message(window, text="O is the Winner!")
                  text.grid(row=3,column=0)
            else:
                  text = Message(window, text="X is the Winner!")
                  text.grid(row=3,column=0)
      winner_flag = True

window = Tk()
player = "X"
list= []

# winner()를 한번만 사용하기 위해서 만든 flag
winner_flag = False

for i in range(9) :
      b = Button(window, text="     ", command=lambda k=i: checked(k))
      b.grid(row=i//3, column=i%3)
      list.append(b)

window.mainloop()

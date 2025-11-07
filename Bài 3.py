from guizero import App, Text, Box, Picture, PushButton
from random import choice
lst_choices = ["normal.png", "normal.png", "normal.png", "normal.png", "normal.png", "normal.png", "rare.png", "rare.png", "rare.png", "epic.png"]
def open_present():
    present_choice = choice(lst_choices)
    if present_choice == "normal.png":
        introduce_text.text_color = "green"
        text_congratulate.text_color = "green"
        text_congratulate.value = "Bạn đã được: Normal!"
    elif present_choice == "rare.png":
        introduce_text.text_color = "blue"
        text_congratulate.text_color = "blue"
        text_congratulate.value = "Bạn đã được: Rare!!!"
    else:
        introduce_text.text_color = "purple"
        text_congratulate.text_color = "purple"
        text_congratulate.value = "Bạn đã được: Epic!!!!!"
    present.image = present_choice
app = App(title = "Mở quà", width = 700, height = 700)
introduce_text = Text(app, text = "Chạm để mở hộp quà:", size = 20, color = "black")
box_present = Box(app, width = 450, height = 450)
present = Picture(box_present, image = "Hộp quà.png")
button_open = PushButton(app, text = "MỞ HỘP", command = open_present)
text_congratulate = Text(app, text = "", size = 20, color = "black")

app.display()
from guizero import App, Text, PushButton
app = App(title = "Đèn giao thông", width = 200, height = 480)
state = "red"
count_down = 11
def change_light():
    global state, count_down
    if state == "red":
        traffic_light_1.bg = "red"
        traffic_light_2.bg = "gray"
        traffic_light_3.bg = "gray"
        state = "green"
    elif state == "green":
        traffic_light_1.bg = "gray"
        traffic_light_2.bg = "gray"
        traffic_light_3.bg = "green"
        state = "yellow"
    else:
        traffic_light_1.bg = "gray"
        traffic_light_2.bg = "yellow"
        traffic_light_3.bg = "gray"
        state = "red"
def update_time():
    global count_down
    count_down -= 1
    clock.value = "Còn lại: " + str(count_down) + " giây"
    app.after(1000, update_time) # Giúp lặp lại lệnh update_time() sau 1000 mi-li giây(1 giây)
    if count_down == 0:
        count_down = 11
        change_light()
Text(app, text = "Trụ đèn giao thông", size = 15, color = "black")
traffic_light_1 = PushButton(app, text = "", height = 5, width = 20)
traffic_light_2 = PushButton(app, text = "", height = 5, width = 20)
traffic_light_3 = PushButton(app, text = "", height = 5, width = 20)
traffic_light_1.disable()
traffic_light_1.bg = "gray"
traffic_light_2.disable()
traffic_light_2.bg = "gray"
traffic_light_3.disable()
traffic_light_3.bg = "gray"
clock = Text(app, text = None, size = 10, color = "black")
change_light()
update_time()
app.display()
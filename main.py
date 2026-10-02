on = False
time = 0

def on_button_pressed_a():
    global on
    on = True
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global time
    time = 0
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    global on
    on = False
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    global time
    basic.show_number(time)
    if on == True:
        time = time + 1
basic.forever(on_forever)

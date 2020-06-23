def on_button_pressed_a():
    global Var1
    Var1 = randint(1, 5)
    basic.show_string("" + str((Var1)))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Var2
    Var2 = randint(1, 9)
    basic.show_string("" + str((Var2)))
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_number(Var1)
    basic.show_icon(IconNames.NO)
    basic.show_number(Var2)
    basic.show_string("=")
    basic.show_string("" + str((Var1 * Var2)))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

Var2 = 0
Var1 = 0
Var1 = 0
Var2 = 0
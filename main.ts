input.onButtonPressed(Button.A, function () {
    Var1 = randint(1, 5)
    basic.showString("" + Var1)
})
input.onButtonPressed(Button.B, function () {
    Var2 = randint(1, 9)
    basic.showString("" + Var2)
})
input.onGesture(Gesture.Shake, function () {
    basic.showNumber(Var1)
    basic.showIcon(IconNames.No)
    basic.showNumber(Var2)
    basic.showString("=")
    basic.showString("" + Var1 * Var2)
})
let Var2 = 0
let Var1 = 0
Var1 = 0
Var2 = 0

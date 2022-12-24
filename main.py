basic.show_string("Hello Julek!")
music.play_melody("B A G F E F E C5 ", 120)

def on_forever():
    basic.show_icon(IconNames.SMALL_HEART)
    basic.show_icon(IconNames.HEART)
basic.forever(on_forever)

def on_logo_touched():
    basic.show_icon(IconNames.HAPPY)
    music._play_default_background(music.built_in_playable_melody(Melodies.NYAN),
        music.PlaybackMode.IN_BACKGROUND)
    basic.show_icon(IconNames.ASLEEP)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def on_gesture_shake():
    basic.show_icon(IconNames.CONFUSED)
    music._play_default_background(music.built_in_playable_melody(Melodies.DADADADUM),
        music.PlaybackMode.IN_BACKGROUND)
    basic.show_icon(IconNames.ASLEEP)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

basic.show_icon(IconNames.ASLEEP)
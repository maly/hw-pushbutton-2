pins.onPulsed(DigitalPin.P0, PulseValue.High, function () {
    music.playTone(262, music.beat(BeatFraction.Sixteenth))
})
pins.setPull(DigitalPin.P0, PinPullMode.PullUp)

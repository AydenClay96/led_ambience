# led_ambience

This project aims to take in HDMI source and output coordinates or in some way light up a programmable LED strip with the correct lighting effect based on the HDMI screen.

# Objective

- [x] To have a basic testing facility for the above.
This includes:
- [x] Generateable "screen" that plots out and is a `length` x `height` rectangle made up of `x` x `y` pixels of the appropriate size.
- [x] Generateable "strip" that plots around the edge of the above screen a configurable number of `n` LED's (colored dots).
- [x] The color of the dots will be in some way selected from the colour of the pixels around it.
This could be by:
- [x] Nearest neighbour (match the colour of the nearest pixel).
- [x] N-nearest neighbour (average the colours of the nearest `N` pixels).

# Future

In the future the following are necessary steps to incorporate this into a real system.
- [ ] Incorporate and extract the real pixels from a video feed.
- [ ] Incorporate a real LED strip and allow for adjustment of the locations to align the test with the real screen.
- [ ] Incorporate this into an embedded device such as a Raspberry PI to allow this to happen in proximity to the screen (Likely performance considerations to do real-time).

In the future the following are attractive steps to make the real system more functional.
- [ ] More sophisticated mechanisms for determining the light that an LED ought to emit (bright or dark, smooth large color differences between frames, etc.)

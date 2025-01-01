import matplotlib.pyplot as plt
from led_ambience.generate_screen import Screen
from led_ambience.generate_strip import LEDStrip


def main() -> None:
    screen_size = [16, 10]
    screen_resolution = [50, 50]
    n_led = 300
    neighbours = 15

    screen = Screen(size=screen_size, resolution=screen_resolution)
    strip = LEDStrip(number=n_led, size=screen_size)
    strip.average_of_neighbours(screen.pixels, neighbours)

    screen.plot()
    strip.plot()

    # ax = plt.gca()
    # ax.set_xlim((-10, screen_size[0] + 10))
    # ax.set_ylim((-10, screen_size[1] + 10))
    plt.show()


if __name__ == "__main__":
    main()

import matplotlib.pyplot as plt
from generate_screen import Screen
from generate_strip import LEDStrip


def main() -> None:
    screen_size = [60, 45]
    screen_resolution = [30, 30]
    n_led = 1000
    neighbours = 50

    screen = Screen(size=screen_size, resolution=screen_resolution)
    strip = LEDStrip(number=n_led, size=screen_size)
    strip.average_of_neighbours(screen.pixels, neighbours)

    screen.plot()
    strip.plot()

    ax = plt.gca()
    ax.set_xlim((-10, screen_size[0] + 10))
    ax.set_ylim((-10, screen_size[1] + 10))
    plt.show()


if __name__ == "__main__":
    main()

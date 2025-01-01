# Generates a strip of LED's around a screen.

import random
from typing import List

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from led_ambience.generate_screen import Pixel


class LEDStrip():
    """Class of LED's that form the strip."""
    def __init__(self, number: int, size: List[float]) -> None:
        self.number = number
        self.size = size
        self._initialize_locs()
        self._initialize_color()

    def _initialize_locs(self) -> None:
        """Initialize the locations of the LED's"""
        self.locs: List[list] = self._half_dubbed(self.number, self.size)

    def _half_dubbed(self, number: int, rect: List[float]) -> List[List[float]]:
        """Calculates the coordinates along the vertical and horizontal, then mirrors."""
        half_number = int(number / 2)
        vertical = int((rect[1] / (rect[0] + rect[1])) * half_number)
        horizontal = half_number - vertical

        # Vertical Placement of LEDs
        vertical_locs = []
        vertical_dist = rect[1] / vertical
        for i in range(vertical):
            vertical_locs.append([0, i * vertical_dist])
            vertical_locs.append([rect[0], i * vertical_dist])

        # horizontal Placement of LEDs
        horizontal_locs = []
        horizontal_dist = rect[0] / horizontal
        for i in range(horizontal):
            horizontal_locs.append([i * horizontal_dist, 0])
            horizontal_locs.append([i * horizontal_dist, rect[1]])

        locs = [[rect[0], rect[1]]]
        locs.extend(horizontal_locs)
        locs.extend(vertical_locs)
        self.number = len(locs)
        return locs

    def _initialize_color(self) -> None:
        colors = ["k", "r", "g", "b"]
        self.color = [random.choice(colors) for _ in range(self.number)]

    def plot(self) -> None:
        ax = plt.gca()
        ax.scatter(*zip(*self.locs), c=self.color)

    def nearest_neighbour(self, pixels: List[Pixel]) -> None:
        """Finds the nearest neighbour to each LED and matches the colour."""

        pixel_locs = []
        for pixel in pixels:
            pixel_locs.append(pixel.center)
        np_pixel_locs = np.array(pixel_locs)

        for index, led_loc in enumerate(self.locs):
            np_led_loc = np.array(led_loc)
            distances = np.linalg.norm(np_pixel_locs - np_led_loc, axis=1)
            min_index = np.argmin(distances)
            self.color[index] = pixels[min_index].color

    def average_of_neighbours(self, pixels: List[Pixel], neighbours: int = 1) -> None:
        """Finds the nearest n neighbours to each LED and averages the colour."""

        pixel_locs = []
        for pixel in pixels:
            pixel_locs.append(pixel.center)
        np_pixel_locs = np.array(pixel_locs)

        for index, led_loc in enumerate(self.locs):
            np_led_loc = np.array(led_loc)
            colors = []
            distances = np.linalg.norm(np_pixel_locs - np_led_loc, axis=1)
            for _ in range(neighbours):
                min_index = np.argmin(distances)
                colors.append(matplotlib.colors.to_rgb(pixels[min_index].color))
                distances[min_index] = np.inf
            self.color[index] = np.mean(colors, axis=0)


def main():
    sq = [40, 30]
    n = 120
    strip = LEDStrip(n, sq)
    strip.plot()
    plt.show()


if __name__ == "__main__":
    main()

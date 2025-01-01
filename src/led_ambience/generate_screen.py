# Generates a screen with pixels of a given colour.

from typing import List, Tuple

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


class Pixel():
    def __init__(self, coord: Tuple[float, float], color: str, size: Tuple[float, float]) -> None:
        self.coord = coord
        self.color = color
        self.size = size
        self.center = [self.coord[0] + self.size[0]/2, self.coord[1] + self.size[1]/2]

    def show(self) -> None:
        ps = self.coord
        sz = self.size
        cl = self.color
        pix = Rectangle((ps[0], ps[1]), sz[0], sz[1], linewidth=2, edgecolor="none", facecolor=cl)
        ax = plt.gca()
        ax.add_patch(pix)


class Screen():
    def __init__(self, size: List[float], resolution: List[int]) -> None:
        self.size = size
        self.resolution = resolution
        self.initialize_pixels()

    def initialize_pixels(self) -> None:
        """Initialize the pixel locations"""
        a, b = self.size
        x, y = self.resolution
        self.pixels: List[Pixel] = []
        sz_row = a / x
        sz_col = b / y
        for i in range(x):
            for j in range(y):
                if i < x/2 and j < y/2:
                    color = "r"
                elif i > x/2 and j < y/2:
                    color = "b"
                elif i > x/2 and j > y / 2:
                    color = "g"
                elif i < x/2 and j > y / 2:
                    color = "w"
                else:
                    color = "k"
                new_pixel = Pixel((i * sz_row, j * sz_col), color, (sz_row, sz_col))
                self.pixels.append(new_pixel)

    def plot(self) -> None:
        sq = self.size
        rect = Rectangle((0, 0), sq[0], sq[1], linewidth=4, edgecolor='k', facecolor='none')
        ax = plt.gca()
        ax.add_patch(rect)
        for pixel in self.pixels:
            pixel.show()


def main():
    sz = [100, 70]
    screen = Screen(sz, [5, 5])
    screen.plot()
    ax = plt.gca()
    ax.set_xlim([-10, sz[0] + 10])
    ax.set_ylim([-10, sz[1] + 10])
    plt.show()


if __name__ == "__main__":
    main()

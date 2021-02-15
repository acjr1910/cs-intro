import math


def polysum(n, s):
    """
    n: Number of sides
    s: Each side length

    Write a function called polysum that takes 2 arguments, n and s. This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.
    """

    polygon_area = (0.25 * n * s**2) / (math.tan(math.pi / n))
    polygon_perimeter = n * s

    return round(polygon_area + polygon_perimeter ** 2, 4)

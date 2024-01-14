class Derivatives:
    def __init__(self) -> None:
        pass

    def calculate_slope(self, point_a, point_b):
        return (point_b[1] - point_a[1]) / (point_b[0] - point_a[0])


if __name__ == "__main__":
    point_a = [3, 5]
    point_b = [7, 20]
    print(Derivatives().calculate_slope(point_a, point_b))

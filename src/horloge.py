
import matplotlib.pyplot as plt

def render(pointCloud: list[tuple[int,int]]) -> None:
    X = [x[0] for x in pointCloud]
    Y = [y[1] for y in pointCloud]
    plt.plot(X, Y,"ob")
    plt.show()

def main():
    pointCloud = [(x, x**2) for x in range(-10, 11)]
    render(pointCloud)
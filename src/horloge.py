import cv2
import numpy as np
from src.date import Date
from math import pi, cos, sin

def distance2(position1: tuple[int,int], position2: tuple[int, int]) -> int:
    return (position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2

def circle(center: tuple[int,int], radius: int, num_points: int = 100) -> list[tuple[float,float]]:
    positions = []
    for i in range(num_points):
        theta = 2 * pi * i / num_points
        x = center[0] + radius * cos(theta)
        y = center[1] + radius * sin(theta)
        positions.append((x, y))
    return positions

def updatePointCloud(currentCircle: list[tuple[float,float]]) -> list[tuple[float,float]]:
    return


def render(pointCloud: list[tuple[int,int]]) -> None:
    max_x = int(max(abs(point[0]) for point in pointCloud) * 1.2)
    max_y = int(max(abs(point[1]) for point in pointCloud) * 1.2)
    
    while True:
        img = np.zeros((max_y * 2, max_x * 2, 3), dtype="uint8")
        for point in pointCloud:
            x = int(point[0] + max_x)
            y = int(point[1] + max_y)
            cv2.circle(img, (x, y), 1, (255, 255, 255), -1)
        cv2.imshow('Points', img)
        key = cv2.waitKey(30) & 0xFF
        if key == 27 or key == ord('q'):
            break
        updatePointCloud(pointCloud)
    cv2.destroyAllWindows()


def showCurrentDate(myDate):
    print(myDate, end="\r")

def main():
    # currentDate = Date()
    # while(True):
    #     showCurrentDate(currentDate)
    #     currentDate.update()
    position_circle = circle((0,0), 1000, 1000000)
    render(position_circle)
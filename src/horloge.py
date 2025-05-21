import cv2
import numpy as np
from src.date import Date
from math import pi, cos, sin

NUMBER_HOUR = 12
NUMBER_MINUTE = 60
COLOR_CIRCLE = 100 
COLOR_LINE = 200
THICKNESS = 2

def circle(center: tuple[int,int], radius: int, num_points: int = 100) -> np.ndarray:
    theta = np.linspace(0, 2 * pi, num_points, endpoint=False)
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)
    return np.column_stack((x, y))

def draw_clock(img, center_x, center_y, radius, current_time):
    cv2.circle(img, (center_x, center_y), radius, (COLOR_CIRCLE, COLOR_CIRCLE, COLOR_CIRCLE), THICKNESS)
    
    for hour in range(NUMBER_HOUR):
        angle = hour * (2 * pi / NUMBER_HOUR) - pi/2
        start_point_hour_line = (
            int(center_x + (radius - 20) * cos(angle)),
            int(center_y + (radius - 20) * sin(angle))
        )
        end_point_hour_line = (
            int(center_x + radius * cos(angle)),
            int(center_y + radius * sin(angle))
        )
        cv2.line(img, start_point_hour_line, end_point_hour_line, (COLOR_LINE, COLOR_LINE, COLOR_LINE), THICKNESS)
        
        text_point = (
            int(center_x + (radius - 40) * cos(angle)),
            int(center_y + (radius - 40) * sin(angle))
        )
        hour_text = str(hour if hour > 0 else NUMBER_HOUR)
        text_size = cv2.getTextSize(hour_text, cv2.FONT_HERSHEY_SIMPLEX, 0.6, THICKNESS)[0]
        text_x = text_point[0] - text_size[0] // 2
        text_y = text_point[1] + text_size[1] // 2
        cv2.putText(img, hour_text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (220, 220, 220), 2)
    
    hour_angle = (current_time.hour % NUMBER_HOUR + current_time.minute / NUMBER_MINUTE) * (2 * pi / NUMBER_HOUR) - pi/2
    minute_angle = (current_time.minute + current_time.second / NUMBER_MINUTE) * (2 * pi / NUMBER_MINUTE) - pi/2
    second_angle = current_time.second * (2 * pi / NUMBER_MINUTE) - pi/2
    
    hour_length = radius * 0.5
    hour_end = (
        int(center_x + hour_length * cos(hour_angle)),
        int(center_y + hour_length * sin(hour_angle))
    )
    cv2.line(img, (center_x, center_y), hour_end, (0, 140, 255), 6)
    
    minute_length = radius * 0.7
    minute_end = (
        int(center_x + minute_length * cos(minute_angle)),
        int(center_y + minute_length * sin(minute_angle))
    )
    cv2.line(img, (center_x, center_y), minute_end, (0, 255, 255), 4)
    
    second_length = radius * 0.9
    second_end = (
        int(center_x + second_length * cos(second_angle)),
        int(center_y + second_length * sin(second_angle))
    )
    cv2.line(img, (center_x, center_y), second_end, (0, 255, 0), 2)
    
    cv2.circle(img, (center_x, center_y), 8, (0, 140, 255), -1)
    cv2.circle(img, (center_x, center_y), 3, (0, 0, 0), -1)
    
    time_str = f"{current_time.hour:02d}:{current_time.minute:02d}:{current_time.second:02d}"
    cv2.putText(img, time_str, (center_x - 60, center_y + radius + 30), 
              cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

def render(pointCloud: np.ndarray) -> None:
    max_x = int(np.max(np.abs(pointCloud[:, 0])) * 1.2)
    max_y = int(np.max(np.abs(pointCloud[:, 1])) * 1.2)
    
    img_shape = (max_y * 2, max_x * 2, 3)
    clock_date = Date()
    clock_radius = min(max_x, max_y) // 3
    while True:
        img = np.zeros(img_shape, dtype="uint8")
        
        clock_date.update()
        
        draw_clock(img, max_x, max_y, clock_radius, clock_date)
        
        cv2.imshow('Points', img)
        
        key = cv2.waitKey(1) & 0xFF
        if cv2.getWindowProperty('Points', cv2.WND_PROP_VISIBLE) < 1 or key == 27 or key == ord('q'):
            break
    
    cv2.destroyAllWindows()

def main():
    position_circle = circle((0,0), 1000, 100000)
    render(position_circle)
from datetime import datetime

class Date:
    def __init__(self) -> None:
        self.update()
    
    def __str__(self) -> str:
        return str(self.current_time)
    
    def update(self) -> None:
        self.current_time = self.get_current_time()
        self.year = self.current_time.year
        self.month = self.current_time.month
        self.day = self.current_time.day
        self.hour = self.current_time.hour
        self.minute = self.current_time.minute
        self.second = self.current_time.second
    
    def get_current_time(self) -> datetime:
        return datetime.now()

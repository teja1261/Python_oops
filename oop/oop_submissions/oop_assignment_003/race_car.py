from car import Car

import math

class RaceCar(Car):
    
    horn = "Peep Peep\nBeep Beep"
    
    def __init__(self, color = None , max_speed =0, acceleration=0, tyre_friction=0):
        super().__init__(color, max_speed, acceleration, tyre_friction)
        self._nitro = 0
            
        
    def accelerate(self):
        speed = 0
        if self._is_engine_started:
            if self._nitro > 0:
                speed = math.ceil(self._acceleration * 30 / 100)
                self._nitro -= 10
            if self._current_speed + self._acceleration + speed <= self._max_speed:
                self._current_speed += self._acceleration + speed
            else:
                self._current_speed = self._max_speed
        else:
            print("Start the engine to accelerate")
            
    def apply_brakes(self):
        if self.current_speed > self._max_speed // 2 :
            self._nitro += 10
            
        super().apply_brakes()
        
        
    @property
    def nitro(self):
        return self._nitro
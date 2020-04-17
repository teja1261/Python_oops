#Python OOPS

Car.py file 


class Car:
    
    def __init__(self, color = None , max_speed =0, acceleration=0, tyre_friction=0):
        self._color = color
        self._max_speed = 0
        self._acceleration = 0
        self._tyre_friction = 0
        if max_speed > 0:
            self._max_speed = max_speed
        else:
            raise ValueError('Invalid value for max_speed')
        
        if acceleration > 0:
            self._acceleration = acceleration
        else:
            raise ValueError('Invalid value for acceleration')
            
        if tyre_friction > 0:
            self._tyre_friction = tyre_friction
        else:
            raise ValueError('Invalid value for tyre_friction')    
        
        self._is_engine_started = False
        self._current_speed = 0
            
        
    def start_engine(self):
        self._is_engine_started = True
        
    def accelerate(self):
        if self._is_engine_started:
            if self._current_speed + self._acceleration <= self._max_speed:
                self._current_speed += self._acceleration
            else:
                self._current_speed = self._max_speed
        else:
            print("Start the engine to accelerate")
            
    def apply_brakes(self):
        self._current_speed -= self._tyre_friction
        if self._current_speed < 0:
            self._current_speed = 0
        
    def sound_horn(self):
        if self._is_engine_started:
            print("Beep Beep")
        else:
            print("Start the engine to sound_horn")
            
    def stop_engine(self):
        self._is_engine_started = False
        
    @property
    def color(self):
        return self._color
        
    @property
    def max_speed(self):
        return self._max_speed
        
    @property
    def acceleration(self):
        return self._acceleration
        
    @property
    def tyre_friction(self):
        return self._tyre_friction
        
    @property
    def current_speed(self):
        return self._current_speed
        
    @property
    def is_engine_started(self):
        return self._is_engine_started

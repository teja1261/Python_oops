#Truck Assignment

Truck.py

class Truck:
    
    def __init__(self, color=None, max_speed=0, acceleration=10, tyre_friction=0, max_cargo_weight=0):
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
        self._loads = 0
        self._max_cargo_weight = max_cargo_weight
    
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
            print("Honk Honk")
        else:
            print("Start the engine to sound_horn")
            
    def stop_engine(self):
        self._is_engine_started = False
        
    def load(self,cargo_weight):
        if cargo_weight < 0:
            raise ValueError('Invalid value for cargo_weight')
        elif self._loads + cargo_weight > self._max_cargo_weight:
            print("Cannot load cargo more than max limit: {}".format(self._max_cargo_weight))
        elif self._current_speed == 0:
            self._loads += cargo_weight
        else:
            print("Cannot load cargo during motion")
            
    def unload(self,cargo_weight):
        if cargo_weight < 0:
            raise ValueError('Invalid value for cargo_weight')
        elif self.current_speed == 0:
            self._loads -= cargo_weight
        else:
            print("Cannot unload cargo during motion")
        
        
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
    
    @property    
    def max_cargo_weight(self):
        return self._max_cargo_weight
        
    @property
    def loads(self):
        return self._loads

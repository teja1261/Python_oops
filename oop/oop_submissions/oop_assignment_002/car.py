class Car:
    
    horn = "Beep Beep"
    
    def __init__(self, color = None , max_speed =0, acceleration=0, tyre_friction=0):
        self._color = color
    
        if max_speed < 0:
            raise ValueError('Invalid value for max_speed')
         
        self._max_speed = max_speed
        
        if acceleration < 0:
            raise ValueError('Invalid value for acceleration')
            
        self._acceleration = acceleration
        
        if tyre_friction < 0:
            raise ValueError('Invalid value for tyre_friction')
            
        self._tyre_friction = tyre_friction
        
        self._is_engine_started = False
        self._current_speed = 0
    
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
        
    def start_engine(self):
        self._is_engine_started = True
        
    def accelerate(self):
        if not self._is_engine_started:
            print("Start the engine to accelerate")
            return 
        
        if self._current_speed + self._acceleration <= self._max_speed:
            self._current_speed += self._acceleration
        else:
            self._current_speed = self._max_speed
            
    def apply_brakes(self):
        self._current_speed -= self._tyre_friction
        if self._current_speed < 0:
            self._current_speed = 0
        
    def sound_horn(self):
        if self._is_engine_started:
            print(self.horn)
        else:
            print("Start the engine to sound_horn")
            
    def stop_engine(self):
        self._is_engine_started = False

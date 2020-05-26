from car import Car

class Truck(Car):
    
    horn = "Honk Honk"
    
    def __init__(self, color=None, max_speed=0, acceleration=0, tyre_friction=0, max_cargo_weight=0):
        super().__init__(color, max_speed, acceleration, tyre_friction )
        self._loads = 0
        if max_cargo_weight < 0:
            raise ValueError('Invalid value for max_cargo_weight')
        self._max_cargo_weight = max_cargo_weight
        
    @property    
    def max_cargo_weight(self):
        return self._max_cargo_weight
        
    @property
    def loads(self):
        return self._loads
        
    def load(self,cargo_weight):
        if cargo_weight < 0:
            raise ValueError('Invalid value for cargo_weight')
        
        if self._loads + cargo_weight > self._max_cargo_weight:
            print("Cannot load cargo more than max limit: {}".format(self._max_cargo_weight))
        elif self._current_speed == 0:
            self._loads += cargo_weight
        else:
            print("Cannot load cargo during motion")
            
    def unload(self,cargo_weight):
        if cargo_weight < 0:
            raise ValueError('Invalid value for cargo_weight')
        
        if self.current_speed == 0:
            self._loads -= cargo_weight
        else:
            print("Cannot unload cargo during motion")
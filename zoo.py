class Deer:
    
    sound = "Buck Buck"
    breath = "Breathe in air"
    
    def __init__(self, age_in_months = 0, breed = None, required_food_in_kgs = 0):
        if age_in_months >= 2:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
            
        self._age_in_months = age_in_months
        
        if required_food_in_kgs <= 0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
            
        self._required_food_in_kgs = required_food_in_kgs
        self._breed = breed
        
        
    @property
    def age_in_months(self):
        return self._age_in_months
        
    @property
    def breed(self):
        return self._breed
        
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
        
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += 2
    
    def make_sound(self):
        print(self.sound)
    
    def breathe(self):
        print(self.breath)
        
class Lion(Deer):
    
    sound = "Roar Roar"
    breath = "Breathe in air"
    
    def __init__(self, age_in_months = 0, breed = None, required_food_in_kgs = 0):
        super().__init__(age_in_months, breed, required_food_in_kgs)
        self._age_in_months = age_in_months
        self._breed = breed
        self._required_food_in_kgs = required_food_in_kgs
        
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += 4
        
class Shark(Deer):
    
    sound = "Shark Sound"
    breath = "Breathe oxygen from water"
    
    def __init__(self, age_in_months = 0, breed = None, required_food_in_kgs = 0):
        super().__init__(age_in_months, breed, required_food_in_kgs)
        self._age_in_months = age_in_months
        self._breed = breed
        self._required_food_in_kgs = required_food_in_kgs
        
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += 8
        
class GoldFish(Deer):
    
    sound = "Hum Hum"
    breath = "Breathe oxygen from water"
    
    def __init__(self, age_in_months = 0, breed = None, required_food_in_kgs = 0):
        super().__init__(age_in_months, breed, required_food_in_kgs)
        self._age_in_months = age_in_months
        self._breed = breed
        self._required_food_in_kgs = required_food_in_kgs
        
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += 0.2

class Snake(Deer):
    
    sound = "Hiss Hiss"
    breath = "Breathe in air"
    
    def __init__(self, age_in_months = 0, breed = None, required_food_in_kgs = 0):
        super().__init__(age_in_months, breed, required_food_in_kgs)
        self._age_in_months = age_in_months
        self._breed = breed
        self._required_food_in_kgs = required_food_in_kgs
        
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += 0.5

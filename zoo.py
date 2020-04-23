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
        
 class Zoo:
    count_animals_in_all = 0
    def __init__(self):
        self._reserved_food_in_kgs = 0
        self.animal_count = 0
        self._animal_list = {'deer': 0,'lion':0,'shark':0,'gold_fish':0,'snake':0}
        
    def add_food_to_reserve(self,weight):
        self._reserved_food_in_kgs += weight
        
    def count_animals(self):
        return self.animal_count
        
    def add_animal(self,animal):
        self.animal_count += 1
        if str(animal) == 'Lion':
            self._animal_list['lion'] += 1
        if str(animal) == 'Deer':
            self._animal_list['deer'] += 1
        if str(animal) == 'Shark':
            self._animal_list['shark'] += 1
        if str(animal) == 'GoldFish':
            self._animal_list['gold_fish'] += 1
        if str(animal) == 'Snake':
            self._animal_list['snake'] += 1
            
        Zoo.count_animals_in_all += 1
     
        
    def feed(self,animal):
        if self._reserved_food_in_kgs == 0:
            return
        self._reserved_food_in_kgs -= animal.required_food_in_kgs
        animal.grow()
        return self._reserved_food_in_kgs
        
    @staticmethod
    def count_animals_in_given_zoos(list):
        count = 0
        for i in list:
            count += i.animal_count
        return count
        
    @classmethod
    def count_animals_in_all_zoos(cls):
        return Zoo.count_animals_in_all
        
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
    
    @property
    def animal_list(self):
        return self._animal_list

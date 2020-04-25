class Pokemon:
    
    def __init__(self, name, level):
        if name == "":
            raise ValueError('name cannot be empty')
            
        self._name = name
        
        if level <=0:
            raise ValueError('level should be > 0')
            
        self._level = level
        self._pokemon_attack = 0 
        
        
    @property
    def name(self):
        return self._name
        
    @property
    def level(self):
        return self._level
        
    @property
    def pokemon_attack(self):
        return self._pokemon_attack
        
    def __str__(self):
        return "{} - Level {}".format(self._name, self._level)
        
class sound:
    
    sounds = ""
    
    @classmethod
    def make_sound(cls):
        print(cls.sounds)
        
class running:
    
    runs = ""
    
    @classmethod
    def run(cls):
        print(cls.runs)
        
class swimming:
    
    swims = ""
    
    @classmethod
    def swim(cls):
        print(cls.swims)
        
class flying:
    
    flys = ""
    
    @classmethod
    def fly(cls):
        print(cls.flys)
        
        
class Pikachu(Pokemon,sound,running):
    
    sounds = "Pika Pika"
    runs = "Pikachu running..."
    
    def __init__(self, name, level):
        super().__init__(name, level)
        self._name = name
        self._level = level
        self._electric_attack = 10 * level
        
    @property 
    def electric_attack(self):
        return self._electric_attack
        
    def attack(self):
        print("Electric attack with {} damage".format(self._electric_attack))
        
class Squirtle(Pokemon,sound,running,swimming):
    
    sounds = "Squirtle...Squirtle"
    runs = "Squirtle running..."
    swims = "Squirtle swimming..."
    
    def __init__(self, name, level):
        super().__init__(name, level)
        self._name = name
        self._level = level
        self._water_attack = 9 * level
        
    @property 
    def water_attack(self):
        return self._water_attack
        
    def attack(self):
        print("Water attack with {} damage".format(self._water_attack))
        
class Pidgey(Pokemon,sound,flying):
    
    sounds = "Pidgey...Pidgey"
    flys = "Pidgey flying..."
    
    def __init__(self, name, level):
        super().__init__(name, level)
        self._name = name
        self._level = level
        self._air_attack = 5 * level
        
    @property 
    def air_attack(self):
        return self._air_attack
        
    def attack(self):
        print("Air attack with {} damage".format(self._air_attack))
        
class Swanna(Pokemon,sound,swimming,flying):
    
    sounds = "Swanna...Swanna"
    swims = "Swanna swimming..."
    flys = "Swanna flying..."
    
    def __init__(self, name, level):
        super().__init__(name, level)
        self._name = name
        self._level = level
        self._water_attack = 9 * level
        self._air_attack = 5 * level
        
    @property 
    def water_attack(self):
        return self._water_attack
        
    @property 
    def air_attack(self):
        return self._air_attack
        
    def attack(self):
        print("Water attack with {} damage".format(self._water_attack))
        print("Air attack with {} damage".format(self._air_attack))
        
class Zapdos(Pokemon,sound,flying):
    
    sounds = "Zap...Zap"
    flys = "Zapdos flying..."
    
    def __init__(self, name, level):
        super().__init__(name, level)
        self._name = name
        self._level = level
        self._electric_attack = 10 * level
        self._air_attack = 5 * level 
        
    def attack(self):
        print("Electric attack with {} damage".format(self._electric_attack))
        print("Air attack with {} damage".format(self._air_attack))
        
class Island:
    
    def __init__(self, name = None, max_no_of_pokemon = 0, total_food_available_in_kgs = 0):
        
        self._name = name
        self._max_no_of_pokemon = max_no_of_pokemon
        self._total_food_available_in_kgs = total_food_available_in_kgs
        self._pokemon_left_to_catch = 0
        self.pokemon_count = 0
        self.pokemon_list = []
        
    @property    
    def name(self):
        return self._name
        
    @property    
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
        
    @property    
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs
        
    @property    
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch
        
        
    def add_pokemon(self,pokemon):
        
        if self.pokemon_count <= self._max_no_of_pokemon:
            self.pokemon_count += 1
            self.pokemon_list.append(pokemon)
        else:
            print("Island at its max pokemon capacity")
            
        
        self._pokemon_left_to_catch += 1
        
    def __str__(self):
        return "{} - {} pokemon - {} food".format(self._name,self._pokemon_left_to_catch,self._total_food_available_in_kgs)
        
class Trainer:
    
    def __init__(self, name = None):
        self._name = name 
        self._experience = 100
        self._max_food_in_bag = self._experience * 10
        self._food_in_bag = 0
        
    @property
    def name(self):
        return self._name
        
    @property
    def experience(self):
        return self._experience
        
    @property
    def max_food_in_bag(self):
        return self._max_food_in_bag
    
    @property
    def food_in_bag(self):
        return self._food_in_bag
        
    def get_all_islands(self):
        return 
    
    def move_to_island(self):
        pass
    
    def collect_food(self):
        pass
    
    def catch(self):
        
        self._experience += 20
    
    def get_my_pokemon(self):
        pass

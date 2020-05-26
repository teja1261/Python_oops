class Pokemon:
    
    def __init__(self, name, level):
        if name == "":
            raise ValueError('name cannot be empty')
            
        self._name = name
        
        if level <=0:
            raise ValueError('level should be > 0')
            
        self._level = level
        self._pokemon_attack = 0
        self._master = None
        
        
    @property
    def name(self):
        return self._name
        
    @property
    def level(self):
        return self._level
        
    @property
    def pokemon_attack(self):
        return self._pokemon_attack
        
    @property 
    def master(self):
        if self._master == None:
            print("No master")
        return self._master
        
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
    
    list_pokemon = []
    
    def __init__(self, name = None, max_no_of_pokemon = 0, total_food_available_in_kgs = 0):
        
        self._name = name
        self._max_no_of_pokemon = max_no_of_pokemon
        self._total_food_available_in_kgs = total_food_available_in_kgs
        self._pokemon_left_to_catch = 0
        self.list_pokemon.append(self)
        
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
        
        if self._pokemon_left_to_catch + 1 <= self._max_no_of_pokemon:
            self._pokemon_left_to_catch += 1
        else:
            print("Island at its max pokemon capacity")
            
        
    def __str__(self):
        return "{} - {} pokemon - {} food".format(self._name,self._pokemon_left_to_catch,self._total_food_available_in_kgs)
       
    @classmethod    
    def get_all_islands(cls):
        return cls.list_pokemon
        
class Trainer(Pokemon, Island):
    
    def __init__(self, name = None):
        self._name = name 
        self._experience = 100
        self._max_food_in_bag = self._experience * 10
        self._food_in_bag = 0
        self.pokemon_list = []
        self._current_island = ""
        
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
        
    @property
    def current_island(self):
        if self._current_island == "":
            print("You are not on any island")
        return self._current_island
        
    
    def move_to_island(self, island):
        self._current_island = island
    
    def collect_food(self):
        if self._current_island != "":
            if self._current_island._total_food_available_in_kgs > self._max_food_in_bag:
                if self._food_in_bag < self._max_food_in_bag:
                    self._food_in_bag += self._max_food_in_bag
                    self._current_island._total_food_available_in_kgs -= self._food_in_bag
                else:
                    self._food_in_bag = self._max_food_in_bag
            else:
                self._food_in_bag = self._current_island._total_food_available_in_kgs
                self._current_island._total_food_available_in_kgs = 0
                
        else:
            print("Move to an island to collect food")
    
    def catch(self,pokemon):
        pokemon._master = self
        self.pokemon_list.append(pokemon)
        if self._experience < pokemon.level*100:
            print("You need more experience to catch {}".format(pokemon.name))
        else:
            print("You caught {}".format(pokemon.name))
            self._experience += pokemon.level*20
    
    def get_my_pokemon(self):
        return self.pokemon_list
        
    def __str__(self):
        return "{}".format(self._name)
        


    
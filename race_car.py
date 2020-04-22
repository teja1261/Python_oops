race_car assignment

race_car.py extension.

import math

class RaceCar:
    
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
        self._nitro = 0
            
        
    def start_engine(self):
        self._is_engine_started = True
        
    def accelerate(self):
        val = 0
        if self._is_engine_started:
            if self._nitro > 0:
                val = math.ceil(self._acceleration * 30 / 100)
                self._nitro -= 10
            if self._current_speed + self._acceleration + val <= self._max_speed:
                self._current_speed += self._acceleration + val
            else:
                self._current_speed = self._max_speed
        else:
            print("Start the engine to accelerate")
            
    def apply_brakes(self):
        if self.current_speed > self._max_speed // 2 :
            self._nitro += 10
            
        self._current_speed -= self._tyre_friction
        if self._current_speed < 0:
            self._current_speed = 0
        
    def sound_horn(self):
        if self._is_engine_started:
            print("Peep Peep\nBeep Beep")
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
        
    @property
    def nitro(self):
        return self._nitro
    
    
    
    
###store assignment###===============================================================================
    class Item:
    def __init__(self,name="Oreo Biscuits",price=0,category="Food"):
        self.name = name
        self.price = price
        self.category=category
        if self.price <= 0:
            raise ValueError(f'Invalid value for price, got {self.price}')
        
    def __str__(self):
        return f"{self.name}@{self.price}-{self.category}"
        
class Query:
    li = ['IN','EQ','GT','GTE','LT','LTE','STARTS_WITH','ENDS_WITH','CONTAINS']
    def __init__(self,field="name", operation="EQ", value="Oreo Biscuits"):
        self.field = field
        self.operation = operation
        self.value = value
        
        if self.operation not in Query.li:
            raise ValueError(f'Invalid value for operation, got {self.operation}')
        
    def __str__(self):
        return f"{self.field} {self.operation} {self.value}"


class Store:
    def __init__(self):
        self.store_item = []
        
    def __str__(self):
        if self.store_item == []:
            return 'No items'
        return '\n'.join(map(str,self.store_item))
        
    def add_item(self,item):
        self.store_item.append(item)
        
        
    def filter(self,query):
        store_obj = Store()
        
        for item in self.store_item:
            filed_value = getattr(item,query.field)
            #print(filed_value)
            if query.operation == "EQ" and filed_value == query.value:
                store_obj.add_item(item)
            elif query.operation == "IN" and filed_value in query.value:
                store_obj.add_item(item)
            elif query.operation == "GT" and filed_value > query.value:
                store_obj.add_item(item)
            elif query.operation == "GTE" and filed_value >= query.value:
                store_obj.add_item(item)
            elif query.operation == "LT" and filed_value < query.value:
                store_obj.add_item(item)
            elif query.operation == "LTE" and filed_value <= query.value:
                store_obj.add_item(item)
            elif query.operation == "STARTS_WITH" and filed_value.startswith(query.value):
                store_obj.add_item(item)
            elif query.operation == "ENDS_WITH" and filed_value.endswith(query.value):
                store_obj.add_item(item)
            elif query.operation == "CONTAINS" and query.value in filed_value:
                store_obj.add_item(item)
                
                
        return store_obj
        
       
    def exclude(self,query):
        exclude_obj = Store()
        res = self.filter(query)

        for item in self.store_item:
            if item not in res.store_item:
                exclude_obj.add_item(item)
                
        return exclude_obj
  
    

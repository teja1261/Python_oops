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
    
    
    
    
###########################store assignment ################################==================

class Store:

    def __init__(self):
        self.store_items = []

    def add_item(self, item):
        self.store_items.append(item)
        
    def count(self):
        return len(self.store_items)
        
    def filter(self, query):

        store = Store()
        for item in self.store_items:
            filter_obj = getattr(item, query.field)
            if query.operation == 'EQ' and  filter_obj == query.value:
                store.add_item(item)
            elif query.operation == 'IN' and filter_obj in query.value:
                store.add_item(item)
            elif query.operation == 'GT' and filter_obj > query.value:
                store.add_item(item)
            elif query.operation == 'GTE' and filter_obj >= query.value:
                store.add_item(item)
            elif query.operation == 'LT' and filter_obj < query.value:
                store.add_item(item)
            elif query.operation == 'LTE' and filter_obj <= query.value:
                store.add_item(item)
            elif query.operation == 'STARTS_WITH' and filter_obj.startswith(query.value):
                store.add_item(item)
            elif query.operation == 'ENDS_WITH'and filter_obj.endswith(query.value):
                store.add_item(item)
            elif query.operation == 'CONTAINS' and filter_obj.__contains__(query.value):
                store.add_item(item)

        return store

    def exclude(self,query):
        store = Store()
        exclude_obj = self.filter(query)

        for item in self.store_items:
            if item not in exclude_obj.store_items:
                store.add_item(item)
                
        return store
        
    def __str__(self):
        if self.store_items == []:
            return 'No items'
        items_in_store = '\n'.join(map(str,self.store_items))
        return items_in_store
        
class Item:
    
    def __init__(self, name=None, price=0, category=None):
        self._name = name 
        if price <= 0:
            raise ValueError("Invalid value for price, got {}".format(price))
            
        self._price = price
        self._category = category
        
    @property    
    def name(self):
        return self._name
    
    @property    
    def price(self):
        return self._price
        
    @property    
    def category(self):
        return self._category    
        
    def __str__(self):
        return "{}@{}-{}".format(self._name,self._price,self._category)
        
class Query:
    
    operations = ["IN", "EQ", "GT", "GTE", "LT", "LTE", "STARTS_WITH", "ENDS_WITH", "CONTAINS"]
    
    def __init__(self, field = None, operation = None, value = None):
        self._field = field
        if operation not in self.operations:
            raise ValueError("Invalid value for operation, got {}".format(operation))
        self._operation = operation
        self._value = value
        
    @property
    def field(self):
        return self._field
    
    @property    
    def operation(self):
        return self._operation
        
    @property    
    def value(self):
        return self._value
            
    def __str__(self):
        return "{} {} {}".format(self._field,self._operation,self._value)

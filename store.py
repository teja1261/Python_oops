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
  

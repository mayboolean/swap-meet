import uuid

class Item:
    # wave 2
    def __init__(self, id=None, condition=0, age=10):
        if id is None:
            self.id = int(uuid.uuid4())
        else:
            if not isinstance(id, int):
                raise TypeError("Expected id to be an int")
            self.id = id
        self.condition = condition
        self.age = age
        
    def get_category(self):
        return self.__class__.__name__
    
    # wave 3
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    #wave5
    def condition_description(self):
        if self.condition == 5:
            return "Mint condition - it's been in a museum"
        elif self.condition == 4:
            return "Almost new - barely touched"
        elif self.condition == 3:
            return "Gentle used, with stories to tell"
        elif self.condition == 2:
            return "Moderated used, but still kickin'!"
        elif self.condition == 1:
            return "Heavily used - but full of character"
        elif self.condition == 0:
            return "This one's a true survivor!"
        else:
            return "Condition must be from 0 to 5"
        

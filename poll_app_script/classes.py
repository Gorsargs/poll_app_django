class Choises():
    def __init__(self,num_of_choises = 2,id_choises = 0):
        self.num_of_choises = num_of_choises
        self.dict_of_choises = {f"name{i+1}": " " for i in range(self.num_of_choises)}
        self.id = id_choises
    def add_dict(self):
        
        self.dict_of_choises = {f"name{i+1}": " " for i in range(self.num_of_choises)}
        
    



    
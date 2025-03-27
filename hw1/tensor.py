import copy

class Tensor :
    def __init__(self, data : list, dimension : int | tuple | None = None) -> None:
        data = copy.deepcopy(data)
        
        shape = self.__get_shape(data)
        self.data = self.__flatten(data, shape)
        
        if dimension is not None:
            user_sz = 1
            for num in dimension:
                user_sz *= num
            
            if len(self.data) != user_sz:
                raise ValueError("Invalid dimension")
        else:
            dimension = shape
            
        self.dimension = dimension
        
    def __get_shape(self, lst: list) -> tuple[int,...]:
        shape = []
        while isinstance(lst, list):
            shape.append(len(lst))
            if lst:  
                lst = lst[0]
            else:
                break
        return tuple(shape)
        
    def __flatten(self, lst, shape):
        if len(shape) == 1:
            return lst
        flattened = []
        while isinstance(lst, list):
            for sublist in lst:
                flattened.extend(self.__flatten(sublist, shape[1:]))
            return flattened

    def __repr__(self):
        return str(self.data)

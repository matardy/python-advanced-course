"""
Estructura de datos para guardar datos infinitos

"""
def first_iterador():
    my_list = [1,2,3,4,5]
    my_iter = iter(my_list)

    while True: 
        try:
            element = next(my_iter)
            print(element)
        except StopIteration: 
            break; 

"""
Quiero construir un iterador desde cero. 
Protocolo de los iteradores: 
    Para construir un iterador debo tener dos metodos
    escenciales __ini__ __iter__ __next__
"""

class EvenNumbers: 
    """
    Clase que implementa un iterador de todos los numeros
    pares, o los numeros pares hasta un maximo.

    """
    def __init__(self,max=None):
        self.max = max 
    
    def __iter__(self): 
        self.num = 0 
        return self 

    def __next__(self): 
        if not self.max or self.num <= self.max:
            result = self.num 
            self.num += 2 
            return result 
        else:
            raise StopIteration


""" 
Puedo tener guardada la succesion de fibonacci en memoria, realmente
lo que puedo es ir accediendo a cada uno de ellos. 
Puedo extraer el siguiente cada vez. 

"""
import time 

class FiboIter(): 
    def __init__(self,max = None): # El comando None me permite que pueda iniciar con un constructor vacio
        self.max = max

    def __iter__(self):
        self.n1 = 0 
        self.n2 = 1
        self.counter = 0 
        return self 
        pass 

    def __next__(self):
        if self.counter == 0: 
            self.counter += 1 
            return self.n1 
        elif self.counter == 1: 
            self.counter += 1 
            return self.n2
        else: 
            if not self.max or self.n2 <self.max: 
                self.aux = self.n2 + self.n1 
                # self.n1 = self.n2  # Swapping clasico
                # self.n2 = self.aux 
                self.n1 , self.n2 = self.n2 , self.aux # Swap en python 
                self.counter +=1 
                return self.aux 
            else:
                raise StopIteration

if __name__ =='__main__':
    fib_iterator = FiboIter()
    for element in fib_iterator: 
        print(element)
        time.sleep(0.1)
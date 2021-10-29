from datetime import datetime 

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now() 
        func(*args, **kwargs) 
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f"Pasaron {time_elapsed.total_seconds()} segundos")
    return wrapper

def with_custom_message(message):
    """
    Decorador con parametros

    """
    def with_message(func):
        print(f"{message}: ")
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
        return wrapper 
    return with_message

@with_custom_message("This is your message!")
def multiply(a,b):
    c = a*b
    print(f"Result: {a} , {b}, {c} ")

@execution_time
def random_func(): 
    for _ in range(1,10000): # Cuando no intersa la variable ponemos _ 
        pass 

@execution_time
def suma(a:int, b:int)-> int:
    print(a+b)

if __name__ == '__main__':
    suma(5,5)
    multiply(4, b=8)
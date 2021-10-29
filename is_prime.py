def is_prime(number:int)->bool:
    divs:int = 0; 
    flag:bool = False
    for i in range(1,number+1):
        if number % i == 0: 
            divs += 1 
        else:
            pass 
    if divs == 2: 
        flag = True
    return flag 
        


def main():
    print(is_prime(5))

if __name__ == '__main__': 
    main() 
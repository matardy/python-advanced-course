def make_repeater_off(n):
    def repeater(string:str):
        assert type(string) == str, "Solo puedes utilizar cadenas"
        return string*n
    return repeater

def make_division_by(n:int):
    def divisor(x:int)->float: 
        assert n!=0, 'No puedes dividir para cero'
        return x/n
    return divisor

def main():


    repeat_5 = make_repeater_off(5)
    #La funcion make_repeater_off es guardada en repeat
    # 5 y esta recuerda el valor 5.
    divide_by5 = make_division_by(5)
    print(divide_by5(25))

    print(repeat_5("Hola!`"))



if __name__ == '__main__': 
    main()
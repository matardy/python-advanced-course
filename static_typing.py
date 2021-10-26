def is_palindrome(string :str) -> bool :
    string  = string.replace(" ", "").lower() #Borro espacio y pongo minuscula
    return string == string[::-1]

def run():
    print(is_palindrome(100))
    #Para ver el error
    # mypy static_typing.py --check-untyped-defs

if __name__ == '__main__':
    run()
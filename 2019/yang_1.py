def palindromecheck(number):

    reversenumber = 0
    cnumber = number

    while cnumber != 0:
        digit = cnumber %10
        reversenumber = reversenumber * 10 + digit
        cnumber //=10

    if number == reversenumber:
       print (reversenumber)
       return True
    return False

def upperpalindromecheck(number): #Put the number in the function
    number += 1
    while not palindromecheck(number):
        number += 1


number = int(input("Number = ")) #You put a number in
upperpalindromecheck(number) #Put the number into function
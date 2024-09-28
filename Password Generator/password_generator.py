import random
import string

def generate_password(minimum: int, hasUpper: bool=True, hasNums: bool=True, hasSpecial: bool=True) -> string:
    availCharacters = string.ascii_lowercase
    upper = string.ascii_uppercase
    special = string.punctuation
    nums = string.digits

    numsCheck = False if hasNums else True
    specialCheck = False if hasSpecial else True
    uppersCheck = False if hasUpper else True

    if hasNums:
        availCharacters += nums
    if hasSpecial:
        availCharacters += special
    if hasUpper:
        availCharacters += upper

    password = ""

    while len(password) <= minimum or (not numsCheck or not specialCheck or not uppersCheck):
        current = random.choice(availCharacters)
        
        if not numsCheck and current in nums:
            numsCheck = True
        elif not specialCheck and current in special:
            specialCheck = True
        elif not uppersCheck and current in upper:
            uppersCheck = True

        password += current

    return password
    
    
def main():
    hasNums = input("Do you require your password to have numeric values (y/n): ")
    hasNums = True if hasNums.lower() == "y" else False

    hasUpper = input("Do you require your password to have uppercase values (y/n): ")
    hasUpper = True if hasUpper.lower() == "y" else False

    hasSpecial = input("Do you require your password to have special characters (y/n): ")
    hasSpecial = True if hasSpecial.lower() == "y" else False

    minimum = input("How many characters long should your password be: ")
    minimum = int(minimum)

    password = generate_password(minimum, hasUpper, hasNums, hasSpecial)
    print(password)

if __name__ == '__main__':
    main()
    

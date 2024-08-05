def checkPassword(password):
    upperChars, lowerChars, specialChars, digits, length, score = 0, 0, 0, 0, 0, 0
    length = len(password)

    with open('common.txt', 'r') as f:
        common = f.read().splitlines()
    
    if password in common:
        print("strength of password is weak, very common password")
        exit()

    if (length < 6):
        print("Password must be at least 6 characters long!\n")
    else:
        for i in range(0, length):
            if (password[i].isupper()):
                upperChars += 1
            elif (password[i].islower()):
                lowerChars += 1
            elif (password[i].isdigit()):
                digits += 1
            else:
                specialChars += 1

    if (upperChars != 0 and lowerChars != 0 and digits != 0 and specialChars != 0):
        if (length >= 8):
            print("The strength of password is strong.")
        else:
            print("The strength of password is medium.")
    else:
        if (upperChars == 0):
            print("Password must contain at least one uppercase character")
        if (lowerChars == 0):
            print("Password must contain at least one lowercase character!")
        if (specialChars == 0):
            print("Password must contain at least one special character!")
        if (digits == 0):
            print("Password must contain at least one digit!")


password = input("Please enter password: ")
checkPassword(password)
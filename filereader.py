def passwd_check(check):

    val = True

    if len(check) < 8:
        print(check+' length should be atleast 8 characters long')
        val = False
    
    if len(check) > 64:
        print(check+' Exceeded maximum length allowed')
        val = False
    
    if not isascii(check):
        print(check+' does not contain ascii characters')
        val = False
    
    if val:
        return val

def isascii(check):
    return len(check) == len(check.encode())
          

def main():
    ##passwd= 'भारत'

    weak_password = open("weak_password.txt", "r")

    read_all = weak_password.read()
    with open("input_password.txt", "r") as fp:
        lines = fp.readlines()

        for line in lines:
            check = line.strip()

            if(passwd_check(check)):
                print(check+ " password is valid")
            elif (line in read_all):
                print(check+" password is common")
            else:
                print(" password is invalid")


if __name__ == "__main__":
    main()
    

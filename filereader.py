def passwd_check(check):

    val = True

    if len(check) < 8:
        print('length should be atleast 8 characters long')
        val = False
    
    if len(check) > 64:
        print('Exceeded maximum length allowed')
        val = False
    
    if not isascii(check):
        print('does not contain ascii characters')
        val = False
    
    if val:
        return val

def isascii(check):
    return len(check) == len(check.encode())
          

def main():
    ##passwd= 'भारत'

    with open("input_password.txt", "r") as fp:
        lines = fp.readlines()

        for line in lines:
            check = line.strip()


    if(passwd_check(check)):
        print("password is valid")
    else:
        print("password is invalid")



if __name__ == "__main__":
    main()
    
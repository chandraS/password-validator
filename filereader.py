from check_common import add, search, TrieNode

<<<<<<< HEAD
if __name__ == "__main__":
    root = TrieNode('*')
=======
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
>>>>>>> 86c77617fcc10cd846dc27d9f913feddf77821d4

    with open("weak_password.txt", "r", encoding='utf-8') as fp:
        lines = fp.readlines()

        for line in lines:
            add(root, line.strip())
            
#     tries will be complete

<<<<<<< HEAD
    with open("input_password.txt", "r", encoding='utf-8') as fp:
=======
    weak_password = open("weak_password.txt", "r")

    read_all = weak_password.read()
    with open("input_password.txt", "r") as fp:
>>>>>>> 86c77617fcc10cd846dc27d9f913feddf77821d4
        lines = fp.readlines()

        for line in lines:
            check = line.strip()

<<<<<<< HEAD
            if not len(check) == len(check.encode()):
                print(len(check)*'*' +' does not contain ascii characters')

            elif len(check) < 8:
                print(check+' length should be atleast 8 characters long')
        
    
            elif len(check) > 64:
                print(check+' Exceeded maximum length allowed')
                                   
            else:
                search(root, line.strip())

=======
            if(passwd_check(check)):
                print(check+ " password is valid")
            elif (line in read_all):
                print(check+" password is common")
            else:
                print(" password is invalid")


if __name__ == "__main__":
    main()
>>>>>>> 86c77617fcc10cd846dc27d9f913feddf77821d4
    

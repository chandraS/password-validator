from check_common import add, search, TrieNode

if __name__ == "__main__":
    root = TrieNode('*')

    with open("weak_password.txt", "r", encoding='utf-8') as fp:
        lines = fp.readlines()

        for line in lines:
            add(root, line.strip())
            

    with open("input_password.txt", "r", encoding='utf-8') as fp:
        lines = fp.readlines()

        for line in lines:
            check = line.strip()

            if not len(check) == len(check.encode()):      ## the length of the encoded word is compared with original word and used to determine whether its a ASCII or not
                print(len(check)*'*' +' does not contain ascii characters')

            elif len(check) < 8:
                print(check+' length should be atleast 8 characters long')
        
    
            elif len(check) > 64:
                print(check+' Exceeded maximum length allowed')
                                   
            else:
                search(root, line.strip())

    

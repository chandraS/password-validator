## Background 

NIST recently updates their Digital Identity Guidelines in June 2017. The new guidelines specify general rules for handling the security of user supplied passwords. Previously passwords were suggested to have certain composition rules (special characters, numbers, etc), hints and expiration times. Those have gone out the window and the new suggestions are as follows: Passwords MUST

1. Have an 8 character minimum
2. AT LEAST 64 character maximum
3. Allow all ASCII characters and spaces (unicode   optional)
4. Not be a common password

```
cat input_passwords.txt | ./password_validator weak_password_list.txt
mom -> Error: Too Short
password1 -> Error: Too Common
*** -> Error: Invalid Charaters

```

The program should accept passwords from STDIN in newline delimited format and print invalid passwords to the command line

Asterixes used to print unprintable characters

## How to approach 

1. List 

List is a linear dynamic data structure in which elements can be added linearly. These elements can then be accessed using indexes or even slicing operations. 

There were two reasons for not using a List:

* The list of weak password contains almost 1 billion rows. This meant iterating through every character of every word in the list of approximately 1 billion words delimited by new line characters. 

This clearly meant, that a time complexity of the order of O(n^m) would be involved. This signifies an exponential time complexity. 

2. Dictionary/HashMap/HashSet 

The second approach could have been to use a key value pair of the passwords in the weak password file consisting of 1 billion rows. A dictionary would take the entire file into the memory and create hashes. This might be useful with small files but as the size increases, the search would take longer to complete. 

3. Tries

The solution used for this assessment leverages the Trie data structure. Trie is a special tree capable of storing sequence of values in such a way that tracing the path from root to any node yields an entire string. 

Trie works on the concept of first buiding and then searching. The available texts or words are first converted into a trie. This phase is called building the trie. If we are storing lots of words that start with similar patterns, tries may reduce the overall storage cost by storing shared prefixes once. The biggest advantage of using a trie is that they save the prefixes of words and when a particular word is queried, only those characters are checked that are diffrent than the prefix, instead of checking every character of the word during every search.  


#function to find charater repeated more that once
#create Hash table(dict in python and loop over it)
def find_duplicates(str):
    l={}
    for letter in str:
        if not l.get(letter):
            l[letter]=1
        else:
            l[letter]+=1

    for key in l.keys():
        if l[key]>1:
            print(key)

#check if strings are anagrams by sorting them and comparing
def check_if_anagrams(str,str1):
    str=sorted(str.lower())
    str1=sorted(str1.lower())
    if str==str1:
        print("Anagrams")
    else:
        print("not anagrams")

#reverse string  using recursion
def reverse_string_recursion(s):
    if len(s)==0:
        return s
    else:
        return  reverse_string_recursion(s[1:])+s[0]


#convert String to integer iterative(yes there are build int functions to do it)
def convert_string_to_int(s):
    len_counter=len(s)-1
    n=0
    for x in (s):
        n+=int(x)*(10**len_counter)
        len_counter-=1
    return n

#convert String to integer recursively(yes there are build int functions to do it)
def convert_string_to_int_recursive(s):
    if len(s)==1:
        return s
    print(s)
    return int(s[0])*(10**(len(s)-1))+int(convert_string_to_int_recursive(s[1:]))

#replace all empty spaces to input string by splitting string an concating
def emptyspace_replace(s,r):
    l=s.split()
    s_new=''
    for x in l:
        s_new=s_new+x+r
    print(s_new)


#find all permutation of a string using backtracking recursive function
def string_permutations(st,s,f):
    if s==f:
        print(st)
    else:
        for x in range(s,f+1):
            st[x],st[f]=st[f],st[x]
            string_permutations(st,s+1,f)
            st[f], st[x]=st[x],st[f]


# check if string is palindrome recursive
def is_palindrome(s):
    if len(s) == 1 or len(s) == 0:
        return True
    else:
        if s[0] == s[len(s) - 1]:
            return  is_palindrome(s[1:len(s)-1])
        else:
            return False

#remove duplicates from string using set
def remove_duplicates(s):
    print(set(list(s)))


#remove char from string
def remove_char(s,c):
    s1=s.replace(c,'')
    print(s1)


#check if string is palindrome recursive

#find_duplicates('adccd')

#check_if_anagrams("abs","abss")

#print(reverse_string_recursion("asd"))

#print(convert_string_to_int("12345"))

#print(convert_string_to_int_recursive("12345"))

#emptyspace_replace("a dd d","%20")


#string_permutations(list("abc"),0,len("abc")-1)


#print(is_palindrome("asa"))

#remove_duplicates("asdsfffff")

remove_char('asd','a')
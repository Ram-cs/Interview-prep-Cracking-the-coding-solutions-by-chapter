###############################
##### ARRAYS AND STRINGS #######
################################
#1
str = "abcdef"
print(len(set(str)) == len(str)) #True if the str has a unique characters otherwise false



#2
str1 = "abd"
str2 = "dba"
print(set(str1) == set(str2) and len(str1) == len(str2))


#3
str = "Mr John Smith        "
str = str.rstrip()
str = str.lstrip()

l = [i if not i.isspace() else "%20" for i in str]
print(''.join(l))


#4
def palindromePermutation(str):
    str = ''.join(str.split(" "))

    import collections
    dic = collections.Counter(str)
    l = len(str) % 2

    if l == 1:
        count = 0
        for val in dic.values():
            if val%2 == 1: count += 1
            if count == 2: return False
    else:
        for val in dic.values():
            if val%2 == 1: return False

    return True

str = "tact coa"
print(palindromePermutation(str))



# #5
def oneWay(str1,str2):
    import collections
    dir1 = collections.Counter(str1.lower())
    dir2 = collections.Counter(str2.lower())
    return (len(dir1-dir2)+len(dir2-dir1)) <= 2

print(oneWay("pale","bake"))



#6
import collections
s = "aabcccccaaa"


SOLUTION I
r = ""
start = 0
for end in range(1,len(s)):
    if s[end] == s[start]: continue
    else:
        r += s[start] + str(end-start)
        start = end
if len(s)-start != 0: r += s[start] + str(len(s)-start)
print(r)

SOLUTION II
r = s[0]
count = 1
for i in range(1,len(s)):
    if s[i] == s[i-1]:
            count += 1

    elif s[i] != s[i-1]:
        if count == 0:
            r += s[i]
        else:
            r += str(count)
            r += s[i]
            count = 1
if count > 0: r += str(count)
print(r)














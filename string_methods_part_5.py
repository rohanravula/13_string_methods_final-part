a="helloworld python is good language"
# print(a.split(" "))  #['helloworld', 'python', 'is', 'good', 'language']
# print(a[::-1]) #in this we can do reverse of the string.
# print(a[0]) #h in this we can know the index postions.
# print(a[:11]) # helloworld. by doing slcicing we know get the full wrod helloworld
# print(a.split(' '))  #['helloworld', 'python', 'is', 'good', 'language']
# print(a.split("")) #valueError: empty separator . coz we didn't gave any space their so it shows error

# a=1,2,3
# print(a) # (1, ,2, 3). a single variable it can hold multiple vlaues then it is callled as tuple
# a,b,c=1,2,3
# print(a) #1
# print(b) #2
# print(c) #3

# a,b,c=1,2,3,4 #value error: too many vlaues to unpack (expected 3)
# a,b,c=1,2 # value error: not enough vlaue to unpcak (expected 3, got 2)

# a=1,2,3,4,5,6,7,8,9,10
# print(sum(a)) #55
 
"importance of split and just basic of input feature"
# a=[int(b) for b in input().split()]
# print(sum(a)) #15. we can directly enter the values in output we can directly get the answer in output thats the importance of the split and the input feature
# a=[int(b) for b in input("Enter Numbers:").split()] #in input we can pass the values it our wish its optional but not compalsary
# print(sum(a))

# a="hello?python"
# print(a.split("?")) #['hello', 'python']

a= "hello world how are you how do you do"
print(a.partition("how"))

import os
import psutil

process = psutil.Process(os.getpid()) # We handle our process using its current PID (Process ID)
print(process.memory_info().rss // (1024*1024), "MB")  # in Mbytes

fdesc = open("words.txt")
data = fdesc.read()
fdesc.close()

print(len(data))
data[0:50]

print(process.memory_info().rss // (1024*1024), "MB")  # in Mbytes
words = data.split("\n")
print(process.memory_info().rss // (1024*1024), "MB")  # in Mbytes

print(len(words))
import re

##EXERCICE 1
import re
##letters and numbers only
number=0
for w in words:
    res = re.match("^[a-zA-Z0-9]+$", w)
    if(res!=None):
        number+=1
    ##print(res)
print("nbLetters&Num=")
print(number)

##letters only
number=0
for w in words:
    res = re.match("^[a-zA-Z]+$", w)
    if(res!=None):
        number+=1
    ##print(res)
print("nbLetters=")
print(number)

##letters only and lowercase
number=0
for w in words:
    res = re.match("^[a-z]+$", w)
    if(res!=None):
        number+=1
    ##print(res)
print("nbLetterLowerCase=")
print(number)

##valid for w but not only letter characters
number=0
list=[]
for w in words:
    res = re.match("^\w+$", w)
    if (res!=None):
        list.append(w)
##print(list)
for l in list:
    res = re.match("^[a-zA-Z]+$", l)
    if(res==None):
        number+=1
    ##print(res)
print("nbNotValidW=")
print(number)

##EXERCICE 2
##REPEATED SEQUENCE : couldn't find the way to do it
'''sequence=[]
##get all the words with letters only
listWords=[]
for w in words:
    res = re.match("^[a-zA-Z]+$", w)
    if (res != None):
        listWords.append(w)
        
for x in range(len(listWords)):       ##for all the words of the list 
    mot=listWords.__getitem__(x)              ##we take and remove the first element of the list
    motChar = [ch for ch in mot]      ##we convert the word in a list of characters
    seq=[]
    for y in range(len(motChar)):
        c=motChar.__getitem__(y)
        if(c==motChar[y]):



##PALINDROME
##a function that will reverse all the letter of our word: starts from to end to the top of the word and step=-1
def reverse(w):
    return w[::-1]

palindrome=[]
##get all the words with letters only
listWords=[]
for w in words:
    res = re.match("^[a-zA-Z]+$", w)
    if (res != None):
        listWords.append(w)
##reverse the word using our previous function and check if the reversed word is the same: if it is, the word if a palindrome
for w in listWords:
    wr = reverse(w)
    if (w == wr):
        palindrome.append(w)

print("list of palindromes =")
print(palindrome)

##ANAGRAM
print("Finding anagrams...")
anagram=[]
##get all the words with letters only
listWords=[]
for w in words:
    res = re.match("^[a-zA-Z]+$", w)
    if (res != None):
        listWords.append(w)

for x in range(len(listWords)):     ##for all the words of the list
    mot=listWords.pop(0)              ##we take and remove the first element of the list
    motChar = [ch for ch in mot]      ##we convert the word in a list of characters
    motChar.sort()                    ##we sort the list in alphabetical order so it is easier to compare with other lists of characters
    for w in listWords:               ##for the remaining words in the list
        if(len(w)!=len(mot)):         ##if the length of the word is not the same, break as it will not be an anagram
            break
        if (mot==w):                  ##if the words are identicals they are not anagrams
            break
        chars=[ch for ch in w]        ##if the length is the same, convert the word into a string of characters
        chars.sort()                  ##sort it in alphabetical order
        if(motChar==chars):           ##compare the tow lists of characters
            anagram.append((mot, w))  ##if they are the same, add them into the list of anagrams
            break                     ##we break when we find the corresponding anagram (we suppose that a word has only 1 possible anagram)
print("list of anagram =")
print(anagram)'''

##SUBSET OF OTHER WORDS
subset=[]
print("Finding subsets...")
##get all the words with letters only
listWords=[]
i=0
for w in words:
    res = re.match("^[a-zA-Z]+$", w)
    if (res != None):
        listWords.append(w)

for x in range(len(listWords)):     ##for all the words of the list
    mot=listWords.pop(0)              ##we take and remove the first element of the list
    motChar = [ch for ch in mot]      ##we convert the word in a list of characters

    for w in listWords:               ##for the remaining words in the list
        if(len(w)<=len(mot)):         ##if the length of the word is not the same, break as it will not be an subset
            break
        if (mot==w):                  ##if the words are identicals they are not subsets
            break
        wChar=[ch for ch in w]        ##if the length is the same, convert the word into a string of characters

        bool=True
        for i in range(len(motChar)):           ##check if all the letters of the smaller word are in the bigger word
                if ( motChar[i] != wChar[i]):   ##if not break
                    bool=False
                    break
        if (bool==True):                        ##if yes, add the word to the list
            subset.append((mot,w))
            i++1

print("list of subsets =")
print(subset)

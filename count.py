'''
 Exercise 3:
 Given a paragraph of text, 
 1. count the number of times each character occurs in the text, 
   and print out each character and its count (in any order).
 2. do it now in a case-insensitive manner for the alphabets
 3. extension: print in the descending order of the count
'''


def count_char(text):
    pass
    
    dictionary = {}
    
    for i in text:
        if i not in dictionary:
            dictionary[i] = 0
        dictionary[i] += 1
    
    for j in dictionary:
        print(j + ' ' + str(dictionary[j]))
    
    
def count_char_insensitive(text):
    pass
    
    dictionary = {}
    
    for i in text.casefold():
        if i not in dictionary:
            dictionary[i] = 0
        dictionary[i] += 1
    
    for j in dictionary:
        print(j + ' ' + str(dictionary[j]))

# bonus task:
def count_char_ordered(text):
    pass
    
    dictionary = {}
    
    for i in text.casefold():
        if i not in dictionary:
            dictionary[i] = 0
        dictionary[i] += 1
    
    char_counts = []
    for j in dictionary:
        if dictionary[j] not in char_counts:
            char_counts.append(dictionary[j])
    
    char_counts.sort()
    char_counts.reverse()
    #counts = sorted(char_counts, reverse = True)
    
    for c in range(0,len(char_counts)):
        for d in dictionary:
            if char_counts[c] == dictionary[d]:
                print(d + ' ' + str(dictionary[d]))

text1 = 'I felt happy because I saw the others were happy and because I knew I should feel happy but I wasn’t really happy' # Robert Bolano
text2 = 'HellO, WorLd!'

# testing exercise 2
count_char(text2)
count_char_insensitive(text2)
count_char_ordered(text2)


#import section
import enchant
#functions
def whole_sentence(ls):
    pass

def cipher_words():
    pass

def word_validity_tester(word):
    d = enchant.Dict("en-US")
    if(d.check(word)==True):
        return 1
    else:
        return 0
#input sections
str1 = input("Input the paragraph you wish to decode ")
ls = str1.split()



class Ceasar:
    alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
                 "j", "k", "l", "m", "n", "o", "p", "q", "r",
                 "s", "t", "u", "v", "w", "x", "y", "z"]

    def __init__(self,string):
        self.string = string

    def encode(self,string):
        returnstring = []
        for i in range(0, len(string)):
            if (string[i] == " "):
                returnstring.append(" ")

            else:
                for j in range(0, len(self.alphabets)):
                    if (string[i] == self.alphabets[j]):
                        index = (j - 3) % 26
                        returnstring.append(self.alphabets[index])
        return returnstring

#asdasd
    def decode(self,string):
        returnstring = []
        for i in range(0, len(string)):
            if (string[i] == " "):
                returnstring.append(" ")

            else:
                for j in range(0, len(self.alphabets)):
                    if (string[i] == self.alphabets[j]):
                        index = (j + 3) % 26
                        returnstring.append(self.alphabets[index])
        return returnstring

    def printing(self, ls):
        for i in ls:
            print(i, end="")
        print("")

string = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG".lower()
cipher1 = Ceasar(string)
print("Encoded: ")
value = cipher1.encode(string)
cipher1.printing(value)
print("Decoded: ")
temp = cipher1.decode(value)
cipher1.printing(temp)


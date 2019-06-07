import random 

def scramble(word):
    middle_words = list(word[1:-1])
    random.shuffle(middle_words)
    return word[0] + ''.join(middle_words) + word[-1]


file1= open("MyFile.txt","r")
file2= open("MyFileScrambled.txt","w")
for line in file1:
        words = line.split()
        for word in words:
            scrambled_word=scramble(word)
            file2.write(scrambled_word)
            file2.write(" ")
print("Scrambled Successfully!")            



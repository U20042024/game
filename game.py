def lengh(mot) :
    if len(mot) >= 4 and len(mot) <= 25 :
        return True

def find(mot, m) :
    return mot.count(m)

word = input("enter a word : ").upper()

while lengh(word) != True :
    word = input("Enter a word with a number of letters between 4 and 25 : ")

Tcar = []

for i in range(len(word)) :
    Tcar.append("*")
l = 0
n = 0

while True :
    letter = input("Enter a letter : ").upper()
    if find(word , letter) == 0 :
        l += 1
    else :
        for i in range(len(word)) :
            if word[i] == letter :
                n += 1
                Tcar[i] = letter
        print(" ".join(Tcar))
    if l == 5 or n == len(word):
        break 

if l == 5 :
    print("Sorry, you lose !")
if n == len(word) :
    print("Congratulations, you win")
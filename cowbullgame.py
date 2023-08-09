import random

a = ""
li = []

def ranint():
    return random.randrange(0, 9)

print("WELCOME TO COWS AND BULLS GAME")
print("______________________________")
print("This game has simple rules, guess the number with hints")
print("For simplicity, we consider a 4 digit number for you to guess")
print("None of the digits in it is repeated")
print("RULE 1 : If you guess the number and its place correctly, it is cow")
print("RULE 2 : If your guess number correctly but not its place, it is bull")
print("For example, if number is 1234 and you guess, 1345, you will have 1 cow and 2 bulls")
print("Because your first digit and place is correct, '1' and digits '3','4' are correct but not place")
print("HAPPY GUESSING")


for i in range(4):
    b = str(ranint())
    while b in li:
        b = ranint()
    li.append(b)

for i in range(4):
    a = a + str(li[i])
c = int(a)

d = int(input("Enter your guess:"))
count = 0
cows = 0
bulls = 0
while d != c :
    s1 = str(d)
    s2 = str(c)
    for i in range(4):
        for j in range(4):
            if s1[i] == s2[j] and i == j:
                cows = cows + 1
            elif s1[i] == s2[j]:
                bulls = bulls + 1
    print("Your input matches \" " + str(cows) + " \" cows and \" " + str(bulls) + " \" bulls. Try Again" )
    #print(c)
    count = count + 1
    d = int(input("Enter your guess:"))
    cows = 0
    bulls = 0
print("YES YOU WON, The Number is indeed " + str(c) + " and you have guessed it in " + str(count) + " tries, Can you beat it? Play again '~'" )


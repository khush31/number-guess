n=21
p=5
print("Guessing game\n")
print("Rules:\n")
print("you need to guess the number\n")
print("you've only 5 guesses to find the number\n")
print("enter the number\n")
s=int(input())
while(n>p):
    if(s==int(n)):
        print("congratulations you have found the correct number")
        break
    elif s>n:
        print("enter the smaller number")
        s=int(input())
        p=p-1
        print("number of guesses left",p)
        if(p==0):
            print("game over try next time")
            break

        
    elif s<n:
        print("enter the greater number") 
        s=int(input())
        p=p-1
        print("number of guesses left",p)
        if(p==0):
            print("game over try next time")
            break

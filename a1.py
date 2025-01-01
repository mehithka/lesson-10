string = input("enter your name: ")
char = input("enter an alphabet")
i=0
count = 0

while (i<len(string)):
    if( string[i] == char):
        count = count + 1
    i= i+1
print("the number of times the character has appeared in your name =",count,'\n',"how many times the condition has been checked: ", i )


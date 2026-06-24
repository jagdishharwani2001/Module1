print("Enter the obtained in 5 subjects: ")

markOne = int(input())
marktwo = int(input())
markthree  = int(input())
markfour = int(input())

sum = markOne +  marktwo + markthree + markfour

avg = int(sum/4)

validRange = range(0,101)

if avg not in validRange:
    print("Invalid Input")
elif avg in range(91,101):
    print("Your grade is A")
elif avg in range(81,91):
    print("You grade is B")
elif avg in range(71,81):
    print("You grade is C")
elif avg in range(71,81):
    print("You grade is D")
elif avg in range(61,71):
    print("You grade is E")
else:
    print("Fail")
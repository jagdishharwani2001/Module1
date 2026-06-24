Amount = int(input("Enter the amount for withdraw"))

note1 = Amount//100
note2 = (Amount%100)//50
note3 = ((Amount%100)%50)//10

print("Number of 100 notes are: ",note1)
print("Number of 50 notes are : ",note2)
print("Number of 10 notes are : ",note3)
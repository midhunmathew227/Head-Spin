strng=input("\n Enter String : ")
vowels=0
consonants=0
spaces=0

for x in strng:
    if(x=='A' or x=='E' or x=='I' or x=='O' or x=='U' or x=='a'
       or x=='e' or x=='i' or x=='o' or x=='u'):
        vowels+=1
    elif(x==' ') :
        spaces+=1
    else :
        consonants+=1

print("\n No of Vowels : ", vowels)
print(" No of Consonants : ", consonants)
print(" No of Spaces : ",spaces)

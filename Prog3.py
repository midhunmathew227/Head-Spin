txt=input("\n Enter the String : ")
x = txt.split()
res = len(x)
result = ''

def reverse(string): 
    string = string[::-1] 
    return string 

if res%2 == 0 :
    pos = 1    
else :
    pos = 0
    
while pos<res :
                 result+= reverse(x[pos]) + ' '
                 pos = pos+2
                 
if res%2 == 0 :
    pos = 0    
else :
    pos = 1

while pos<res :
                 result+= x[pos] + ' '
                 pos = pos+2
                 
print(result)

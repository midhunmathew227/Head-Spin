def reverse(string, start, end): 

    temp = '' 
    while start <= end: 
        temp = string[start] 
        string[start] = string[end] 
        string[end] = temp 
        start += 1
        end -= 1
  
def reverseletter(string, start, end): 
    wstart, wend = start, start 
    while wend < end: 
        if string[wend] == " ": 
            wend += 1
            continue

        while wend <= end and string[wend] != " " : 
            wend += 1
        wend -= 1
  
        reverse(string, wstart, wend) 
        wend += 1
  
if __name__ == "__main__": 
    string = input("\n Enter String : ")
    string = list(string) 
    reverseletter(string, 0, len(string) - 1)
    print('\n')
    print(''.join(string))

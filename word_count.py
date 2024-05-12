def word_count(str1):
    leng=len(str1)
    count=0
    if leng==0:
        return count
    for i in range(leng):
        if(i<leng):
            if (str1[i]==" " or str1[i]=="."):
                if i<leng-1:
                    if (str1[i+1]==" " or str1[i+1]=="."):
                        continue
                    else:
                        count=count+1
                        continue
                
    if str1[0]==" " or str1[0]==".":
        count=count-1               
    if str1[leng-1] != " " or str1[leng-1] != ".":
        count=count+1
    return count
#str1=['my name is aswin.I am 21 years old']
str1=input("Enter the string:")
word=word_count(str1)
print("Number of words in the sentence are:",word)

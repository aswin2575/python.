def word_count(str1):
    leng=len(str1[0])
    count=0
    for i in range(leng):
        if(i<leng-1):
            if(str1[0][i]==" " or str1[0][i]=="."):
                count=count+1
    return count+1
#str1=['my name is aswin.I am 21 years old']
str1=input("Enter the string:")
print(str1)
word=word_count(str1)
print("Number of words in the sentence are:",word)
def romanToInt(self, s):
        dict1={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        n=len(s)
        value=0
        for i in range(n):
            if i<n-1:
                if s[i]=='I':
                        if s[i+1]=='V' or s[i+1]=='X':
                            value=value-2
                if s[i]=='X':
                        if s[i+1]=='L' or s[i+1]=='C':
                            value=value-20
                if s[i]=='C':
                        if s[i+1]=='D' or s[i+1]=='M':
                            value=value-200
            for j in dict1.keys():
                if dict1[j]==s[i]:
                    value=value+j
                    break
        return value
self=0
s=input('Enter the roman letters')
inte=romanToInt(self,s)
print(inte)
# dict1={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
# print(dict1.keys())
# print(dict1['I'])
# for j in dict1.keys():
#     print(j)
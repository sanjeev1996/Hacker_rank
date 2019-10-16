string,string1=input(),input()
print(len([string1 for index,value in enumerate(string[0:-(int(len(string1))-1)]) if (string1==string[index:index+len(string1)])]))

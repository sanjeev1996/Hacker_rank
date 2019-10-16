import re
m=re.sub(r'[aieouAIEOU]+$','',input())
m=re.sub(r'^[aieouAIEOU]+','',m)
m=re.findall(r'[aieouAIEOU][aieouAIEOU]+',m)
m=[i for i in m if (len(i)>1)]
print("\n".join(m) if m else "-1")

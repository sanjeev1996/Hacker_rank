import re
for _ in range(int(input())):
    b=[]
    a=''.join(sorted(input())).upper()
    [b.append(True) if re.search('[A-Z]{2}',a) else b.append(False)]
    [b.append(True) if re.search('[0-9]{3}',a) else b.append(False)]
    [b.append(True) if a.isalnum() else b.append(False)]
    [b.append(True) if not re.search(r'(.)\1', a) else b.append(False)]
    [b.append(True) if len(a)==10 else b.append(False)]
    [print('Valid') if all(b) else print('Invalid')]
        

import re

for _ in range(int(input())):
    u = ''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}', u)
        assert re.search(r'\d\d\d', u)
        assert not re.search(r'[^a-zA-Z0-9]', u)
        assert not re.search(r'(.)\1', u)
        assert len(u) == 10
    except:
        print('Invalid')
    else:
        print('Valid')

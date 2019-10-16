import re
for _ in range(int(input())):
    a=input()
    try:
        assert re.search(r'^[456]',a)
        assert re.search(r'^[0-9]{4}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}',a)
        assert re.sub(r'[- ]','',a).isdigit()
        assert not re.search(r'(.)\1{4}',''.join(sorted(re.sub('[- ]','',a))))
    except:
        print('Invalid')
    else:
        print('Valid')

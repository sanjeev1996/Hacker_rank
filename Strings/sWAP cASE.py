'''
def swap_case(s):
    s=list(s)
    for index, value in enumerate(s):
        if (value.islower()):
            s[index]=value.upper()
        elif (value.isupper()):
            s[index]=value.lower()
    return ''.join(s)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
'''

print(''.join([a.lower() if a.isupper() else a.lower() for a in input()]))

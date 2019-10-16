letters='abcdefghijklmnopqrstuvwxyz1234567890_-'
let_dig='abcdefghijklmnopqrstuvwxyz1234567890'

def fun(email):
    b=[]
    try:
        username, url = email.split("@")
        if len(username)==0:
            return False
        website, extension = url.split(".")
    except ValueError:
        return False
    b.append(all([j in letters for j in username]))
    b.append(all([j in let_dig for j in website]))
    b.append(all([len(extension)<4]))
    return all(b)

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)




'''
letters='abcdefghijklmnopqrstuvwxyz1234567890_-'
let_dig='abcdefghijklmnopqrstuvwxyz1234567890'

def fun(emails):
    a=emails
    b=[]
    try:
        username=a.split('@')[0]
        website1=a.split('@')[1]
        website=website1.split('.')[0]
        extension=website1.split('.')[1]
    except IndexError:
        return False
    b.append(all([j in letters for j in username]))
    b.append(all([j in let_dig for j in website]))
    b.append(all([len(extension)==3]))
    return all(b)

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)
'''

members = ['egoing', 'duru']
for member in members:
    print('member', member)

members2 = [
    ['egoing', 'seoul', 'programmer'], 
    ['duru', 'daegu', 'dba']
]
print(members2[0][0])
for member in members2:
    print(member[0], member[1])

egoing1 = ['egoing', 'seoul', 'programmer']
egoing2 = {'name': 'egoing', 'city': 'seoul', 'job': 'programmer'} # 사전형
print(egoing2['city'])
for name in egoing2:
    print(egoing2[name])

members3 = [
    {'name':'egoing', 'city':'seoul', 'job':'programmer'}, 
    {'name':'duru', 'city':'daegu', 'job':'dba'}
]
for member in members3:
    print(member['name'])
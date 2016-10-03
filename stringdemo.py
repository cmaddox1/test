team = 'New England Patriots'
print(team[0])
#print(team[1.5])-this is wrong

print(len(team))

print(team[len(team)-1])

last = team[-1]
print(last)

index=0
while index<len(team):
    letter=team[index]
    print(letter)
    index +=1

prefixes='JKLMNOPQ'
suffix='ack'
for letter in prefixes:
    if letter == '0' or letter=='Q':
        suffix='uack'
    else:
        suffix='ack'
    print(letter+suffix)

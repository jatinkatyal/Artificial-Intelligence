sentence = input("Enter Statement: ")
print (sentence)
sentence = sentence.split()
predLogic=''
i=0
flag=True
while i < len(sentence):
    word = sentence[i]
    if word == 'all' or word == 'every' or word=='everyone':
        predLogic += 'Vx:'
        noun = sentence[i+1]
    elif word == 'some':
        predLogic += 'Ex:'
        noun = sentence[i+1]
    elif word == 'is' or word=='are':
        collNoun = sentence[i+1]
    elif flag == True:
        noun = word
        flag=False
    else:
        collNoun = word
    i+=1
predLogic += collNoun + '(' + noun + ')'

print(predLogic)


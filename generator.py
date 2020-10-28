
# def getRandomInt(combien):
#     import random
#     result=[]
#     for __ in range(combien):
#         result.append(random.randint(1,100))
#     return result

def getRandomInt(combien):
    import random
    for __ in range(combien):
        yield random.randint(1,100)

# data=set(getRandomInt(combien=10))
# print(data)

for e in getRandomInt(combien=100):
    if e > 80: 
        break
    print(e)

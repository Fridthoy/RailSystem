

point = '[(33,9),(31,10),(2021,18)]'

def update(points):
    a= ''
    liste = []
    for i in point:

        if i.isdigit():
            a+= i
        else:
            if len(a) > 0:
                liste.append(a)
                a=''

    liste = list(map(int, liste))

    finalList =[]

    count= 1
    for i in liste:
        if count == 3:
            count= 1
        if count== 1:
            a= i
        elif count ==2:
            b= i
        if count== 2:
            finalList.append((a,b))

        count += 1

    return finalList

print(update(point))


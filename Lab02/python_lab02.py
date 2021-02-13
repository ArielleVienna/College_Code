#part 01
def multiplyList(myList) : 
    result = 1
    for x in myList: 
         result = result * x  
    return result  

list1 = [1, 2, 3, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]  
print(multiplyList(list1))
# returned: 906694364710971881029632

#part 02
def addList(thisList) : 
    result = 1
    for x in thisList: 
         result = result + x  
    return result  

list2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]
print(addList(list2))
#returned: 719788177

#part 03
def modoloList(thisList) : 
    result = 1
    for x in thisList: 
        if x % 2 == 0:
            continue
        else:
            #remove it from thisList
            thisList.remove(x)
        result = result + x  
    return result

list3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21] 
print(modoloList(list3))
#returned: 1486

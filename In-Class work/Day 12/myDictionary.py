#******************************************************
#Program Name:        myDictionary.py
#Programmer:          Gabriela Tolosa Ramirez
#CSC - 119:           Fall 2018 - 002
#Date:                Nov 12, 2018
#Purpose:             Manipulate myDictionary
#Modules used:        None
#Input Variable(s):   N/A
#Output(s):           N/A
#******************************************************

def main():
    myDictionary = {"Red":102,"Green":612,"Blue":920}
    print("myDictionary: ",myDictionary)
    print()

    #Find the length of the myDictionary
    myDictionaryLength = len(myDictionary)
    print("The length of the dictionary is: ",myDictionaryLength)
    print()

    #Use get function to retrieve "Blue"
    item = myDictionary.get("Blue")
    print("The value to the key 'Blue' is: ",item)
    print()

    #Find the sume of the values
    sum = 0
    for item in myDictionary:
        sum = sum+myDictionary[item]
    print("The sum of the values in the dictionary is: ",sum)
    print()

    #Respond true or false - if the value for key "Red"=612
    print("The value for the key 'Red' is 612")
    if myDictionary.get("Red")==612:
        print("True")
    else:
        print("False")
    print()

    #Change the value for "Green" to 710
    if "Green" in myDictionary:
        myDictionary["Green"]=710
    print("myDictionary: ",myDictionary)
    print()

    #add the Key-Value pair "Orange":832
    key = "Orange"
    value = 832
    if key not in myDictionary:
        myDictionary[key] = value
    print("myDictionary: ",myDictionary)
    print()

    #Change the value for "Red" to 523
    if "Red" in myDictionary:
        myDictionary["Red"]=523
    print("myDictionary: ",myDictionary)
    print()

    #Append yourDictionary = {"Yellow":1040,"Orange":1214}
    yourDictionary = {"Yellow":1040,"Orange":1214}
    list1 = list(myDictionary.items())
    list2 = list(yourDictionary.items())
    myDictionary = dict(list1+list2)
    print("myDictionary: ",myDictionary)
    print()

    #Delete "Yellow":1040 from myDictionary
    if "Yellow" in myDictionary:
        del myDictionary["Yellow"]
    print("myDictionary: ",myDictionary)
    print()

main()

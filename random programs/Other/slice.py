myList = [2,4,6,8,10,12,14,16]

slice1 = myList[2:6]
print(slice1)          #[6,8,10,12]

slice2 = myList[2:]
print(slice2)          #[6,8,10,12,14,16]

slice3 = myList[:6]
print(slice3)          #[2,4,6,8,10,12]

slice4 = myList[::-1]
print(slice4)          #[16,14,12,10,8,6,4,2]

slice5 = myList[6:2:-1]
print(slice5)          #[14,12,10,8]

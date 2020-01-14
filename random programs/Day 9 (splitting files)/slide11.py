#Note: the variable 'volume' in main() and cubeVolume()
#is not the same.
#The have different storage locations.

def main():
    length = float(input("Please enter a number. "))
    volume = cubeVolume(length)
    print("The length of the cube's side is: ", length)
    print("The volume is: ",volume)
def cubeVolume(lengthOfSide):
    volume = lengthOfSide**3
    return volume

main()

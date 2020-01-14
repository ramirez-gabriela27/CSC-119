def cubeVolume (sideLength):
    volume = sideLength**3
    return volume
def unitTest():
    if cubeVolume(2)==8:
        return True
    else:
        return False
def main():
    testPassed = unitTest()
    if testPassed == True:
        print("The UnitTest passed")
    else:
        print("The UnitTest failed")
main()

def mericaToMetric():
    feetString = input("How many feet? Do not enter units.  -3")
    inchString = input("How many inches? Do not enter units.    ")
    feet = float(feetString)
    inches = float(inchString)

    feetAndInches = feet + (inches/12)
    meters = feetAndInches/3.281

    return meters

#main function included for testing convenience c:
if __name__ == "__main__":
    print(f"The result is: {mericaToMetric():.5f} meters")
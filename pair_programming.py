def mericaToMetric(): ### feedback: fantastic function name
    feetString = input("How many feet? Do not enter units.  ")
    ### feedback: function will be more useful if it does not require user inputs, maybe take arguments instead
    inchString = input("How many inches? Do not enter units.    ")

    ### feedback: i usually like numpy datatypes for numerical calculations, but this works too. could also do float(input()) above instead
    feet = float(feetString)
    inches = float(inchString)

    feetAndInches = feet + (inches/12)
    meters = feetAndInches/3.281

    return meters

### feedback: might also include some case handling for negative inputs or non-numeric inputs, i.e. if your user enters a string it should tell them why that doesn't work.

#main function included for testing convenience c:
if __name__ == "__main__":
    print(f"The result is: {mericaToMetric():.5f} meters") # function works well for this use case!
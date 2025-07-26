while True:
    wgt=input("Enter the weight in kg (or 'q' to quit): ")
    if wgt.lower() == 'q':
        print("Exiting the program.")
        break
    hgt=input("Enter the height in meters : ")
    try:
        wgt=float(wgt)
        hgt=float(hgt)
    except:
        print("Invalid input. Please enter numeric values for weight and height.")
        continue
    bmi=wgt/(hgt**2)
    print('Your BMI is: ',round(bmi, 2))

# checks if the year is a leap year or not
while True:
    year=input("Enter a year (or type 'q' to exit): ")
    if year.lower()=='q':
        print("Exiting...")
        exit()
    year=int(year)
    if year %4==0:
        if year%100==0:
            if year %400==0:
                print("This is a leap year!")
            else:
                print("This is not a leap year")
        else:
            print("This is a leap year!")
    else:
        print("This is not a leap year")
                
        

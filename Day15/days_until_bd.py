# checks how many days are left till your birthday
while True: 
    import datetime
    start=input("press 'Enter' to start the program or press 'q' to exit:")
    if start.lower()=='q':
        print("Exiting the program...")
        exit()

    day=input("Enter the date of birth (1-31): ")
    month=input("Enter the month of birth (1-12): ")
    try:
        day=int(day)
        month=int(month)
    except:
        print("ERROR!")

    today=datetime.date.today()
    cyear=today.year

    try:
       bd=datetime.date(cyear,month,day)
       if bd<today:
          bd=datetime.date(cyear+1,month,day)
    except:
      print("VALUE ERROR!")

    days_left=(bd-today).days

    if days_left==0:
       print("HAPPY BIRTHDAY!!!")
    elif days_left<7:
      print("ITS YOUR BIRTHDAY SOON!!!")
      print("only",days_left,"more days to go")
    else:
       print("you've",days_left,"days until your next birthday.")

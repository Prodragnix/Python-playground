x=12570
yeslist=['England'or'Wales'or'Northrn Ireland']
print('\nThis is a tax calculator for the UK!')
country=input('Please enter your country:\nEngland\nScotland\nWales\nNorthen Ireland\nEnter your country in the way it is presented in the list above:  ' )
total=int(input('\nPlease enter your annual salary(without tax): £'))
remain=total-x
if country in yeslist:
    if total<=12570:
        year=remain+x
        month=remain+x
        month=month/12
        year=round(year,2)
        month=round(month,2)
        print('Your yearly salary is : £',year,'\nYour monthly salary is : £',month)
    elif total<=50270:
        remain=remain-(remain*20/100)
        year=remain+x
        month=remain+x
        month=month/12
        year=round(year,2)
        month=round(month,2)
        print('Your yearly salary is : £',year,'\nYour monthly salary is : £',month)
    elif total<=125140:
        remain=remain-(remain*40/100)
        year=remain+x
        month=remain+x
        month=month/12
        year=round(year,2)
        month=round(month,2)
        print('Your yearly salary is : £',year,'\nYour monthly salary is : £',month)
    else:
        remain=remain-(remain*45/100)
        year=remain+x
        month=remain+x
        month=month/12
        year=round(year,2)
        month=round(month,2)
        print('Your yearly salary is : £',year,'\nYour monthly salary is : £',month)
elif country=='Scotland':
    if total<=12570:
        year=remain+x
        month=remain+x
        month=month/12
        year=round(year,2)
        month=round(month,2)
        print('Your yearly salary is : £',year,'\nYour monthly salary is : £',month)
    elif total<=14876:
        remain=remain-(remain*19/100)
        year=remain+x
        month=remain+x
        month=month/12
        year=round(year,2)
        month=round(month,2)
        print('Your yearly salary is : £',year,'\nYour monthly salary is : £',month)
    elif total<=26561:
        remain=remain-(remain*20/100)
        year=remain+x
        month=remain+x
        month=month/12
        year=round(year,2)
        month=round(month,2)
        print('Your yearly salary is : £',year,'\nYour monthly salary is : £',month)
    elif total<=43662:
        remain=remain-(remain*21/100)
        year=remain+x
        month=remain+x
        month=month/12
        year=round(year,2)
        month=round(month,2)
        print('Your yearly salary is : £',year,'\nYour monthly salary is : £',month)
    elif total<=75000:
        remain=remain-(remain*42/100)
        year=remain+x
        month=remain+x
        month=month/12
        year=round(year,2)
        month=round(month,2)
        print('Your yearly salary is : £',year,'\nYour monthly salary is : £',month)
    elif total<=125140:
        remain=remain-(remain*45/100)
        year=remain+x
        month=remain+x
        month=month/12
        year=round(year,2)
        month=round(month,2)
        print('Your yearly salary is : £',year,'\nYour monthly salary is : £',month)
    elif total>125140:
        remain=remain-(remain*48/100)
        year=remain+x
        month=remain+x
        month=month/12
        year=round(year,2)
        month=round(month,2)
        print('Your yearly salary is : £',year,'\nYour monthly salary is : £',month)
else:
    print('\nERROR! Please rerun the program! :(')

print('\nThank you for using this tax calculator! ')
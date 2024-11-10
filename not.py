def main():
    print('\nThis is a calculator!')
    first=eval(input('\nPlease enter your first number: '))
    print('\nHere are the options:\n1 = Addition\n2 = Substraction\n3 = Multiplication\n4 = Division with decimals\n5 = Division with remainders\n6 = Division with only the quotient\n7 = Division wth only the remainder\n8 = Indicies\n9 = Root')
    operation=input('\n\nPlease enter the number of your operation: ')
    second=eval(input('\nPlease enter your second number: '))
    if operation=='1':
        print(first+second)
    elif operation=='2':
        print(first-second)
    elif operation=='3':
        print(first*second)
    elif operation=='4':
        print(first/second)
    elif operation=='5':
        print(first//second,'r',first%second)
    elif operation=='6':
        print(first//second)
    elif operation=='7':
        print(first%second)
    elif operation=='8':
        print(first**second)
    elif operation=='9':
        x=pow(first,1/second)
        print(x)
    else:
        print('ERROR! Please try again! :(')
    b=input('\nDo you want to do another equation?\nYES\nNO\nEnter your choice in CAPITALS: ')
    if b=='YES':
        main()
    else:
        print('\nThank you for using this calculator!Hope this helped you!\n\n')
        exit()
main()
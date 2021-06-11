list = []

while True:
    print('\n')
    print('****** MENU START******')
    print('1. Add data')
    print('2. Display data')
    print('3. Search data')
    print('4. Update data')
    print('5. Delete data')
    print('6. Exit')
    print('****** MENU END******')
    print('\n')

    menu = str(input("Enter Menu Option: "))

    if(menu == '1'):
        print('**** SELECTED OPTION ----> 1. Add Data ****')

        n = str(input("Enter Value: "))

        if(list.__contains__(n) == False):
            list.append(n)
        else:
            print('\n')
            print('######################################')
            print("The value "+n+" is already exist in List!")
            print('######################################')

        continue
    elif(menu == '2'):
        print('**** SELECTED OPTION ----> 2. Display Data ****')
        print('\n')
        print('######################################')
        print(list)
        print('######################################')
        continue
    elif(menu == '3'):
        print('**** SELECTED OPTION ----> 3. Search Data ****')

        n = str(input("Search Value: "))

        if(list.__contains__(n) == True):
            print('\n')
            print('######################################')
            print("Index of "+n+" is "+str(list.index(n)))
            print('######################################')
        else:
            print('\n')
            print('######################################')
            print(n+" is not found in List!")
            print('######################################')

        continue
    elif(menu == '4'):
        print('**** SELECTED OPTION ----> 4. Update Data ****')

        list_index = int(input("Search Index of List: "))
        n = str(input("Enter Value to Update List Index: "))

        if((len(list) - 1) < list_index):
            print('\n')
            print('######################################')
            print("No such index found!")
            print('######################################')
        else:
            list[list_index]=n

        continue
    elif(menu == '5'):
        print('**** SELECTED OPTION ----> 5. Delete Data ****')

        n = str(input("Enter Value to Delete from List: "))

        if(list.__contains__(n) == True):
            list.remove(n)
        else:
            print('\n')
            print('######################################')
            print("No such value found in List!")
            print('######################################')
        
        continue
    elif(menu == '6'):
        print('**** SELECTED OPTION ----> 6. Exit ****')
        break
    else:
        print('\n')
        print('######################################')
        print('Invalid Option!')
        print('######################################')
        continue
camps_to_be_conducted=[]
dates_of_camps=[]
camps_conducted=[]
people_served=0
no_of_camps_conducted=0
no_of_camps_to_be_conducted=0
print('1 : Add camp location')
print('2 : Camp conducted')
print('3 : look for a camp')
print('4 : REPORT')
print('5 : Display list')
print('6 : Exit')


while True:
    try:
        choice = int(input('Enter your choice : '))
        if choice == 6:
            print('Thank You')
            break
        elif choice == 1:
            location = input('Enter the location : ')
            date = input('Enter the date : ')
            camps_to_be_conducted.append([location, date])
            no_of_camps_to_be_conducted += 1
        elif choice == 2:
            location = input('Where was the camp conducted : ')
            people_served += int(input('How many people were served : '))
            for i in camps_to_be_conducted:
                if i[0] == location:
                    print('Camp was successfully conducted')
                    no_of_camps_to_be_conducted -= 1
                    no_of_camps_conducted += 1
                    camps_conducted.append(i)
                    camps_to_be_conducted.remove(i)
                    continue
        elif choice == 3:
            location = input('Enter the location : ')
            for i in camps_to_be_conducted:
                if i[0] == location:
                    print(f'Camp at {i[0]} is to be conducted on {i[1]} of this month')
                    continue
        elif choice == 4:
            print(f'Camps Conducted so far is {no_of_camps_conducted}')
            print(f'People served so far {people_served}')
            print(f'Camps to be conducted : {no_of_camps_to_be_conducted}')
        elif choice == 5:
            print('Camps planned')
            for i in camps_to_be_conducted:
                print(i[1],i[0], end=' ,')
            print('.......!!!!')
            print('Camps Conducted so far')
            for i in camps_conducted:
                print(i[1],i[0], end=' ,')
            print('.......!!!!')
    except ValueError as e:
        print('Some Error Occurred !! try again')
        print('Error code : ',e)
        continue











politicleParties=['AAP','Elephent','Hand','Rest']
electionYear=['2014','2009','2005','2001']
countryStatus=['worst','developing','developed']
corruptionStatus=['Max','Normal','Min']
while True:
    '''for party in politicleParties:'''
    year=input("***To stop the system type: QUIT *** \n Enter Year: ")
    
    if year == 'QUIT':
        print('System has stopped!')
        break
    elif year in electionYear:
        if year == '2014':
            print('AAp Wins!')
            print('Country status: '+countryStatus[2])
            print('Corruption Status: '+corruptionStatus[2])
            continue
        elif year == '2009':
            print('Hand Won : ')
            print('Country status: '+countryStatus[0])
            print('Corruption Status: '+corruptionStatus[0])
            continue
        elif year == '2005':
            print('Hand won!')
            print('Country status: '+countryStatus[0])
            print('Corruption Status: '+corruptionStatus[0])
            continue
        elif year == '2001':
            print('Rest Won!')
            continue
    else:
        print('Wrong year of election!')
        continue
    '''else:
        print('The above loop was just for demonstration purpose!')
        continue'''
# Name: Keyin LIN
# unikey: klin8602
import sys

#Schedule of movies, their times and room:
#list[0]==name of the movie   #list[1]==year of the movie   #list[3]==how long of the movie   #list[4]==times of the movie   #list[5]==room of the movie
#The purpose of using the tuples is to prevent fixed movie information from being changed
mov1_1=[('The Shining'),('1980'),('2h 26m'),('10:00'),('Room 1')]
mov1_2=[('Your Name'),('2016'),('1h 52m'),('13:00'),('Room 1')]
mov1_3=[("Fate/Stay Night: Heaven's Feel - III. Spring Song"),('2020'),('2h 0m'),('15:00'),('Room 1')]
mov1_4=[('The Night Is Short, Walk on Girl'),('2017'),('1h 32m'),('17:30'),('Room 1')]
mov1_5=[('The Truman Show'),('1998'),('1h 47m'),('19:30'),('Room 1')]
mov1_6=[('Genocidal Organ'),('2017'),('1hr 55m'),('21:45'),('Room 1')]

mov2_1=[("Jacob's Ladder"),('1990'),('1h 56m'),('10:00'),('Room 2')]
mov2_2=[('Parasite'),('2019'),('2h 12m'),('12:15'),('Room 2')]
mov2_3=[('The Dark Knight'),('2008'),('2h 32min'),('14:45'),('Room 2')]
mov2_4=[('Blade Runner 2049'),('2017'),('2h 44m'),('17:45'),('Room 2')]
mov2_5=[('The Mist'),('2007'),('2h 6m'),('21:00'),('Room 2')]
mov2_6=[('Demon Slayer: Mugen Train'),('2020'),('1h59min'),('23:20'),('Room 2')]

mov3_1=[('The Matrix'),('1999'),('2h 16m'),('10:00'),('Room 3')]
mov3_2=[('Inception'),('2010'),('2h 42m'),('11:30'),('Room 3')]
mov3_3=[('Shutter Island'),('2010'),('2h 19m'),('14:30'),('Room 3')]
mov3_4=[('Soul'),('2020'),('1hr 40m'),('17:00'),('Room 3')]
mov3_5=[('Mrs. Brown'),('1997'),('1h 41min'),('19:00'),('Room 3')]
mov3_6=[('Peppa Pig: Festival of Fun'),('2019'),('1h 8min'),('21:00'),('Room 3')]
mov3_7=[('Titanic'),('1997'),('3h 30min'),('22:15'),('Room 3')]

mov_total=[mov1_1, mov1_2, mov1_3, mov1_4, mov1_5, mov1_6, mov2_1, mov2_2, mov2_3, mov2_4, mov2_5, mov2_6, mov3_1, mov3_2, mov3_3, mov3_4, mov3_5, mov3_6, mov3_7]

#The prices of tickets and popcorn:
tickets_before=float(13.00)
tickets_after=float(15.00)
pop_s=float(3.50)
pop_m=float(5.00)
pop_l=float(7.00)

#About the room:
room_1=round(35/2)+1
room_2=round(136/2)
room_3=round(42/2)

#After discount:
pop_s_dis=pop_s*0.2
pop_m_dis=pop_m*0.2     
pop_l_dis=pop_l*0.2
tic_before_dis=tickets_before*0.1
tic_after_dis=tickets_after*0.1
#------------------------------------------------------------------------

#Some functions for later operations：
#------------------------------------------------------------------------
#Convert time to minutes:
def time_minute(time_user):
    time_minute=(int(time_user[0])*600)+(int(time_user[1])*60)+(int(time_user[3])*10)+(int(time_user[4])*1)
    return time_minute

#------------------------------------------------------------------------
#Determine if a movie exists:
def mov_exist(mov_entered_user,mov_total):
#Ask for the name of the movie and check the name whether exist: 
    while True:                
        for i in range(len(mov_total)):
            mov_name=(mov_total[i][0]).lower()
            if mov_entered_user==mov_name:
                mov_name_exist=True
                mov_time_user=time_minute(mov_total[i][3])
                break
            else:
                mov_name_exist=False
#If the name is not exist:            
        if mov_name_exist==False:
            y_n_movie=(input('Sorry, we could not find that movie. Enter Y to try again or N to quit. ')).lower()
            while y_n_movie!='n' and y_n_movie!='y':
                y_n_movie=(input('Sorry, we could not find that movie. Enter Y to try again or N to quit. ')).lower()

            if y_n_movie=='n':
                print('\nBye.')
                exit()
            elif y_n_movie=='y':
                mov_entered_user=(input('What is the name of the movie you want to watch? ')).lower()
                continue 
        if mov_name_exist==True:
            break 
    return mov_time_user, True, mov_entered_user

#------------------------------------------------------------------------
#Deal with popcorn related issues:
def details(ticket_time, pop_size_ls, number_people):
    if ticket_time<960:
        ticket_cost=tickets_before
        ticket_time_type='before 16:00'
    elif ticket_time>960:
        ticket_cost=tickets_after
        ticket_time_type='from 16:00'

    total_cost=0.00
    pop_cost_ls=[]
    sml_ls=[]
    for i in range(len(pop_size_ls)):
        if pop_size_ls[i]=='s':
            pop_cost=pop_s
            sml_size='Small'
        elif pop_size_ls[i]=='m':
            pop_cost=pop_m
            sml_size='Medium'
        elif pop_size_ls[i]=='l':
            pop_cost=pop_l
            sml_size='Large'
        elif pop_size_ls[i]=='n':
            pop_cost=0.00
            sml_size='n'
        total_cost_each=pop_cost+ticket_cost
        total_cost+=total_cost_each
        pop_cost_ls.append(pop_cost)
        sml_ls.append(sml_size)

    if number_people==1:
        print('For {} person, the initial cost is '.format(number_people).ljust(35, ' ') + '$' + '{:6.2f}'.format(total_cost))
        print(' Person 1: Ticket {}'.format(ticket_time_type).ljust(34, ' ') + '$' + '{}'.format(ticket_cost).ljust(5, '0'))
        if pop_size_ls==[]:
            pass
        else:
            print(' Person 1: {} popcorn'.format(sml_ls[0]).ljust(34, ' ') + '$' + '{}'.format(pop_cost_ls[0]).rjust(4, ' ').ljust(5, '0'))
    elif number_people>1:
        print('For {} persons, the initial cost is '.format(number_people).ljust(34, ' ') + '$' + '{:5.2f}'.format(total_cost))
        for a in range(number_people):
            print(' Person {}: Ticket {}'.format(a+1, ticket_time_type).ljust(34, ' ') + '$' + '{}'.format(ticket_cost).ljust(5, '0'))
            if pop_cost_ls[a]==0.00:
                pass
            elif pop_cost_ls[a]!=0.00:
                print(' Person {}: {} popcorn'.format(a+1, sml_ls[a]).ljust(34, ' ') + '$' + '{}'.format(pop_cost_ls[a]).rjust(4, ' ').ljust(5, '0'))

    return total_cost, pop_cost_ls

#------------------------------------------------------------------------
#Deal with change:
def Transact_change(user_paid,total_cost):
#Transact and give change
    while True:
        user_paid_ls=list(str(user_paid))
        check_paid_ls=str(user_paid).split('.')       
                
#Check the user enters whether divisible by 5c :
        if len(check_paid_ls[1])==2:
            div_paid=int(user_paid_ls[-1])
            if div_paid%5!=0:
                print('The input given is not divisible by 5c. Enter a valid payment.')
                user_paid=float(input('Enter the amount paid: $'))
                continue
        else:                    
            money_change=user_paid-total_cost
            if money_change<0:
                money_change=abs(money_change)
                money_enough=False
                print('The user is ${:.2f} short. Ask the user to pay the correct amount. '.format(money_change))
                user_paid=float(input('Enter the amount paid: $'))
                continue
            elif money_change>=0:
                money_enough=True
                break
                
#Calculate the change:    
    print('Change: ${:.2f}'.format(money_change))
    currency=[0.05, 0.1, 0.2, 0.5, 1, 2, 5,10, 20, 50, 100]
    i=len(currency)-1
    while i>=0:
        if money_change>=currency[i]:
            number_currency=int((money_change)//currency[i])
            money_change=float(money_change-(number_currency*currency[i]))
            if i>=4:
                print(' ${:2d}: '.format(currency[i])+'{}'.format(number_currency))
            else:
                form_cent=int(currency[i]*100)
                print(' {:2d}c: '.format(form_cent)+'{}'.format(number_currency))
                         
            if money_change!=0:
                i-=1
                continue
            else:
                break
        else:
            i-=1
            continue           
    return 

#------------------------------------------------------------------------
#Ask for the number of people:
def ask_number_people():
    mov_time_user, mov_name_exist, mov_name=mov_exist(mov_entered_user,mov_total)
    while mov_name_exist==True:
        number_people=int(input('\nHow many persons will you like to book for? '))
        print('')
        if number_people<=1:
            y_n_people=input(('Sorry, you must have at least two customers for a group booking. Enter Y to try again or N to quit. ')).lower()  
            while y_n_people!='n' and y_n_people!='y':
                y_n_people=(input('Sorry, you must have at least two customers for a group booking. Enter Y to try again or N to quit. ')).lower()

            if y_n_people=='n':
                print('\nBye.')
                exit()
            elif y_n_people=='y':
                continue
        else:
            break
    return number_people
    
#------------------------------------------------------------------------














#First message
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"+"~ Welcome to Pizzaz cinema ~\n"+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"+"-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")

#------------------------------------------------------------------------
#Part: Switch errors
#If No switch provided:
if len(sys.argv)<2:
    print('Usage: python3 pizzaz.py [--show <timenow> | --book | --group]') 
    exit()
else:
    switch=sys.argv[1]

#If the switch options are not correct:
if switch!='--show' and switch!='--book' and switch!='--group':
    print('Sorry. This program does not recognise the switch options.\n'+'\nBye.')
    exit()

#------------------------------------------------------------------------

#------------------------------------------------------------------------
#Part: Switch --show
#Check the time entered whether it is valid:
if switch=='--show':
    if len(sys.argv)<3 or len(sys.argv)>3:
        print('Sorry. This program does not recognise the switch options.\n'+'\nBye.')
        exit()

    time_user=list(sys.argv[2])
    if len(time_user)!=5:
        print('Sorry. This program does not recognise the time format entered.\n'+'\nBye.')
        exit()
    else:
        if time_user[2]!=':':
            print('Sorry. This program does not recognise the time format entered.\n'+'\nBye.')
            exit()
        else:
            if time_user[0].isdigit()==False or time_user[1].isdigit()==False or time_user[3].isdigit()==False or time_user[4].isdigit()==False:
                print('Sorry. This program does not recognise the time format entered.\n'+'\nBye.')
                exit()
            else:
                if int(time_user[0])>2 or int(time_user[3])>5:
                    print('Sorry. This program does not recognise the time format entered.\n'+'\nBye.')
                    exit()
                else:
                    if int(time_user[0])==2 and int(time_user[1])>3:
                        print('Sorry. This program does not recognise the time format entered.\n'+'\nBye.')
                        exit()
                    else:
                        time_valid=True

#Converts the time entered by the user to a comparable time:
    if time_valid==True:
        time_minute_user=time_minute(time_user)

#Converts the time of the movies and compare them and the time entered by the user:
        order_of_mov=0
        while order_of_mov<len(mov_total):
            time_mov=list(mov_total[order_of_mov][3])
            convert_time_mov=time_minute(time_mov)
            if convert_time_mov>=time_minute_user:
                print(f'{mov_total[order_of_mov][0]}. {mov_total[order_of_mov][1]}. {mov_total[order_of_mov][2]}. {mov_total[order_of_mov][3]}. {mov_total[order_of_mov][4]}')
            order_of_mov+=1

#End of the program:
        print('\nBye.')
        exit()

#------------------------------------------------------------------------

#------------------------------------------------------------------------
#Part: Switch --book
if switch=='--book':
    if len(sys.argv)!=2:
        print('Sorry. This program does not recognise the switch options.\n'+'\nBye.')
        exit()

#Ask for the name of the movie and check the name whether exist: 
    mov_entered_user=(input('What is the name of the movie you want to watch? ')).lower()
    mov_time_user, mov_name_exist, mov_name=mov_exist(mov_entered_user,mov_total)

#If the name is exist, ask the user if they would like a popcorn:
    if mov_name_exist==True:
        y_n_pop=(input('\nWould you like to order popcorn? Y/N ')).lower()  
        while y_n_pop!='n' and y_n_pop!='y':
            y_n_pop=(input('Would you like to order popcorn? Y/N ')).lower()

        if y_n_pop=='n':
            size_pop='n'
        elif y_n_pop=='y':
            size_pop=(input('You want popcorn. What size Small, Medium or Large? (S/M/L) ')).lower() 
            while size_pop!='s' and size_pop!='m'and size_pop!='l':
                size_pop=(input('You want popcorn. What size Small, Medium or Large? (S/M/L) ')).lower()
        size_pop=list(size_pop)

#Generate and print the seat allocation:         
        print('\nThe seat number for person 1 is #17\n')
        total_cost_book, pop_cost_ls=details(mov_time_user, size_pop, 1)
        print('\n No discounts applied'.ljust(35, ' ')+ '$' + '0.00'.rjust(5, ' '))
        print('\nThe final price is'.ljust(35, ' ') + '$' + '{}'.format(total_cost_book).ljust(5, '0'))
    
#Transact and give change:
        user_paid=float(input('\nEnter the amount paid: $'))
        Transact_change(user_paid,total_cost_book)

#End of the program:
        print('\nBye.')
        exit()

#------------------------------------------------------------------------

#------------------------------------------------------------------------
#Part: Switch --group
if switch=='--group':
    if len(sys.argv)!=2:
        print('Sorry. This program does not recognise the switch options.\n'+'\nBye.')
        exit()

#Ask for the name of the movie and check the name whether exist:    
    while True:
        mov_entered_user=(input('What is the name of the movie you want to watch? ')).lower()
        mov_time_user, mov_name_exist, mov_name=mov_exist(mov_entered_user,mov_total)    

#Ask for the number of people and check the space of the room:    
        number_people=ask_number_people()
        for i in range(len(mov_total)):
            if (mov_total[i][0]).lower()==mov_name:
                mov_room=(mov_total[i][4])
                break
            else:
                pass
            i+=1
        if mov_room=='Room 1':
            room_space=int(room_1)
        elif mov_room=='Room 2':
            room_space=int(room_2)
        else:
            room_space=int(room_3)
    
        if room_space<number_people:
            y_n_space=(input(f'Sorry, we do not have enough space to hold {number_people} people in the theater room of {room_space} seats. Enter Y to try a different movie name or N to quit. ')).lower()
            while y_n_space!='n' and y_n_space!='y':
                y_n_space=(input(f'Sorry, we do not have enough space to hold {number_people} people in the theater room of {room_space} seats. Enter Y to try a different movie name or N to quit. ')).lower()
            if y_n_space=='n':
                print('\nBye.')
                exit()
            else:
                continue
        else:
            break

#Ask about popcorn for each person:    
    pop_size_ls=[]
    for i in range(number_people):
        y_n_pop_group=input(f'For person {i+1}, would you like to order popcorn? Y/N ').lower()
        while y_n_pop_group!='n' and y_n_pop_group!='y':
            y_n_pop_group=input(f'For person {i+1}, would you like to order popcorn? Y/N ').lower()
            
        if y_n_pop_group=='n':
            pop_size_ls+='n'
        if y_n_pop_group=='y':
            size_pop_group=input(f'Person {i+1} wants popcorn. What size Small, Medium or Large? (S/M/L) ').lower()
            while size_pop_group!='s' and size_pop_group!='m'and size_pop_group!='l':
                size_pop_group=(input(f'Person {i+1} wants popcorn. What size Small, Medium or Large? (S/M/L) ')).lower()
            pop_size_ls+=size_pop_group
    print('')

#Print the seat allocation
    for i in range(number_people):
        seat_num=2*(i+1)-1
        print(f'The seat number for person {i+1} is #{seat_num}')
        i+=1
    print('')

#Generate and print the seat allocation:
    total_cost_group, pop_cost_ls=details(mov_time_user, pop_size_ls, number_people)
    print('')

#Group Discount:
    if total_cost_group<100.00:
        print(' No discounts applied'.ljust(34, ' ')+ '$' + '0.00'.rjust(5, ' '))
        print('\nThe final price is'.ljust(35, ' ') + '$' + '{}'.format(total_cost_group).ljust(5, '0'))
   
    else:
        ticket_count=number_people
        if mov_time_user<960:
            ticket_cost=tickets_before
        elif mov_time_user>960:
            ticket_cost=tickets_after

        ticket_discount=ticket_count*ticket_cost*0.1
        ticket_print=round(ticket_discount,2)

        pop_cost=0.00
        pop_count=0
        for i in range(len(pop_cost_ls)):
            pop_cost+=pop_cost_ls[i]
            if pop_cost_ls[i]!=0.00:
                pop_count+=1
            i+=1
        pop_discount=pop_cost*0.2
        pop_print=round(pop_discount,2)

        total_after=total_cost_group-pop_discount-ticket_discount
        total_print=round(total_after,2)

        print(' Discount applied tickets x{}'.format(ticket_count).ljust(33, ' ') + '-$' + '{:.2f}'.format(ticket_print).rjust(5, ' '))
        print(' Discount applied popcorn x{}'.format(pop_count).ljust(33, ' ') + '-$' + '{:.2f}'.format(pop_print).rjust(5, ' '))
        print('\nThe final price is'.ljust(35, ' ') + '$' + '{}'.format(total_print).ljust(5, '0'))
        total_cost_group=total_print

#Transact and give change:
    user_paid=float(input('\nEnter the amount paid: $'))
    Transact_change(user_paid,total_cost_group)

#End of the program:
    print('\nBye.')
    exit()
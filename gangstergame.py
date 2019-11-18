import random

drugs = ('heroin', 'cocaine', 'weed', 'shrooms')
drugprice = {'heroin':50 , 'cocaine':40, 'weed':30, 'shrooms':20}

cars = ('Lamborgini', 'Audi RS6', 'VW Golf', 'Opel Kadett')
car_price = {'Lamborgini':200000, 'Audi RS6':140000, 'VW Golf':50000,'Opel Kadett':2000}
carsescapechance = {'Lamborgini':98, 'Audi RS6':90, 'VW Golf':60, 'Opel Kadett':20}

ownedcars= ['Opel Kadett'] # list of cars you own


totalfunds = 0
startfund = 50000

totalfunds = totalfunds + startfund
print ("\nYour funds are: €{}".format(totalfunds))

########### functions ###############################

def choose_name():
    i = input("\nWhat is your gangster name? ")
    return i

def random_drugs_select():
    x = random.choice(drugs)
    return x
    #print('{} €{}'.format(x.title(), drugprice[x]))


def escape_vehicle():
    print("Your car is a {}".format(cars[3]))
    print("Your current balance is €{}".format(totalfunds))
    i = input("Do you want to buy a new car? y or n: ")
    if i == "y":
        while True:
            x = input("\nYou can choose: \n1: {} €{} \n2: {} €{} \n3: {} €{} \n4: {} €{} \npress a number: "
                .format(cars[0],car_price['Lamborgini'],cars[1],car_price['Audi RS6'],cars[2],car_price['VW Golf'], cars[3],car_price['Opel Kadett']))
            if x == '1':
                if (totalfunds - car_price['Lamborgini']) < 0:
                    input_money = input("not enough money, do you want to choose another car? y or n ")
                    if input_money == "n":
                        break
                else:
                    return cars[0]       
            elif x == '2':
                if (totalfunds - car_price['Audi RS6']) < 0:
                    input_money = input("not enough money, do you want to choose another car? y or n ")
                    if input_money == "n":
                        break
                else:
                    return cars[1]
            elif x == '3':
                if (totalfunds - car_price['VW Golf']) < 0:
                    input_money = input("not enough money do you want to choose another car? y or n ")
                    if input_money == "n":
                        break
                else:
                    return cars[2]
            elif x == '4':
                if (totalfunds - car_price['Opel Kadett']) < 0:
                    input_money = input("not enough money do you want to choose another car? y or n ")
                    if input_money == "n":
                        break
                else:
                    return cars[3]
            else:
                print("No car selected")
    
    else:
        return cars[3]

def escape_chance(object):
    x = object
    if x == cars[0]:
        return (carsescapechance[x])
    elif x == cars[1]:
        return (carsescapechance[x])
    elif x == cars[2]:
        return (carsescapechance[x])    
    elif x == cars[3]:
        return (carsescapechance[x])
    else:
        print("your old car")

def smuggle_drugs(escapechance, drugprice):
    x = escapechance
    y = drugprice
    if x >= 50:
        return True 
        print("yes")     
    else:
        return False

############### logic #################

print("\n"*50)

#Starts the game and asks the name the player chooses
print("This is a textbase gangster game")

gangstername = choose_name()
print ("\nYour gangstername is {}".format(gangstername.title()))

while True:
    
    # print what kind of drugs you need to smuggle
    randomdrugsselect = random_drugs_select()
    drugprice_select = drugprice[randomdrugsselect]
    print('You need to smuggle {} for €{}'.format(randomdrugsselect.title(), drugprice_select))


    #print which car you bought
    escapevehicle = escape_vehicle() #puts the output of escape_vehicle function in variable

    if escapevehicle == cars[0]:
        print("\nYou bought a {}".format(cars[0]))
    elif escapevehicle == cars[1]:
        print("\nYou bought a {}".format(cars[1]))
    elif escapevehicle == cars[2]:
        print("\nYou bought a {}".format(cars[2]))
    elif escapevehicle == cars[3]:
        print("\nYou bought a {}".format(cars[3]))

    # prints the escape chance of the car
    escapechance = escape_chance(escapevehicle)
    print("Your chance to escape is {}%". format(escapechance))
    #start the smuggle of drugs based on type of car you get more chance to succeed
    smuggledrugs = smuggle_drugs(escape_chance(escapevehicle), drugprice_select)

    if smuggledrugs == True:
        print("You smuggled succesfully")
        totalfunds = totalfunds + drugprice_select
    else:
        print("You are busted!")
        totalfunds = totalfunds - drugprice_select
    print("Your new balance is €{}".format(totalfunds))
    
    # Quit the game
    quit = input("Do you want to quit? yes or no ")
    if quit[0].lower()=='y':
        print("Thanks for playing!")
        break
    else:
       continue 






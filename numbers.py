#---------------------------------------------------#
#                                                   #
#                Code by Kevin Xiao                 #
#                                                   #
#---------------------------------------------------#

# Skills are labelled with "// " before each skill
# and they also appear in CAPSLOCK

import time, math
from os import system
# importing modules

def mainMenu():
    # // FUNCTION
    system('clear')
    textSep = '\033[96m________________________________________________________________________________________\033[0m\n'
    # defines a text seperator for convenience
    screenSelectionInput = input(f'''{textSep}\nThis program will be able to provide with 
the prime factorization, least common multiple, and prime status
of up to 5 numbers from 2-100000
\033[96m© 2021 Kevin Xiao\033[0m\n
To continue to the program: press \033[96menter\033[0m
To see instructions: type \033[96mhelp\033[0m
To end the program: type \033[96mquit\033[0m\n\n''').lower().replace(" ", "")
    # asks the user for an input of either continue or help
    # this will be used to either start the program or get help
    # quits if quit is typed
    # // .LOWER(), // .REPLACE()

    if screenSelectionInput == '':
        # if user inputs enter // IF STATEMENT
        system('clear')
        # clears screen
        integerEvaluation()
        # calls the positive integer function (the main program) // CALLING FUNCTION

    elif screenSelectionInput == 'help':
        # elif the user inputs help // ELIF STATEMENT
        system('clear')
        # clears screen
        returnToMainMenu = input(
            f'''{textSep}\nYou can select how many numbers you want to know about in the initial question
and the subsequent questions ask for the numbers themselves
for information about the algorithms used, refer to this explanation video (unfinished)\n
The program will subsequently provide you with a prime factorization of the number(s)
and if there are more than one, a LCM and GCF as well
when the program is given 2 numbers, an exact quotient value + remainder
along with an approximate quotient will be provided
\n\npress \033[96menter\033[0m to continue\n\n''')
        # prints help message then tells user to press enter
        if returnToMainMenu or returnToMainMenu == '':
            # if a string has something in it returns true
            # and if it is empty it still returns true because of the boolean
            system('clear')
            # clears screen
            mainMenu()
            # calls main menu

    elif screenSelectionInput == 'quit':
        # if user inputs quit
        system('clear')
        # clears screen first
        return
        # before the function returns nothing and will quit

    else:
        # if the user inputs an invalid value then this screen will appear // ELSE STATEMENT
        system('clear')
        # clears screen
        print("Please enter a valid input: Returning to menu in 3 seconds")
        # prints message // PRINT
        for i in range(3, 0, -1):
            # counts down from 5 to 1 (stops at 0) // FOR LOOP (COUNTS DOWN)
            print(f"\n{i}")
            # prints message using f string
            time.sleep(1)
            # waits 1 second

        system('clear')
        # clears screen
        mainMenu()
        # calls main menu // CALLING FUNCTION


def integerEvaluation():
    LCM = 1
    # initializes the integer of the LCM which will be changed later // VARIABLE (INTEGER)
    leastCommonMultiple = {}
    # initializes a list to hold the factors of the least common multiple of all numbers // VARIABLE (DICTIONARY)
    lcmFactorMessage = ''
    # initializes a string that will be manipulated to create a message later // VARIABLE (STRING)
    numberQuantity = int(input("Enter how many numbers you would like to observe (up to 5): \n"))
    # asks for how many numbers will be observed // CASTING (string to integer)
    numbersList = []
    # a list of which these values will be appended
    numbersFactors = []
    # a list which will hold the prime factors of the numbers
    textSep = '\033[96m_____________________________________________________________\033[0m'
    # defines a text seperator for convenience

    while True:
        # a loop that doesn't end
        if 1 <= numberQuantity <= 5:
            break
            # code breaks after the code confirms that the input was valid
        numberQuantity = int(input("\nPlease enter a valid value between 1-5 for numbers being observed: \n"))
        # if not, then it will continue asking for a valid input

    system('clear')
    # clears the output screen

    for numbers in range(numberQuantity):
        # will loop for as many times as the user asked in the previous input
        numberVal = int(input(f"\nPlease enter a value for your {numbers+1}/{numberQuantity} number(s) between 1-100000: \n"))
        # asks for the input of a number and displays which iteration they are on
        # there is a +1 as a loop starts counting from 0, and the output should start from 1

        while True:
            # a loop that always runs
            if 1 <= numberVal <= 100000:
                # if the number value is within the asked range
                numbersList.append(numberVal)
                # the value given will be appended to the list numbersList
                break
                # breaks out of the true loop
            numberVal = int(
                input("\nPlease enter a valid value for between 1-100000: \n"))
            # if the value is invalid then it will keep asking for an input

    system('clear')
    # clears the output screen

    for i in range(len(numbersList)):
        # will loop through each of the values in the numberlist by getting the
        # length of the number list
        factorMessage = ''
        # a string that will be manipulated to be printed later
        isPrime = 'not'
        # defines is prime as not (this will change based on later comparisons)
        numbersFactors.append(primeFactorization(numbersList[i]))
        # appends all the factors of the current number being iterated to the list numbersFactors
        # which will have dictionaries nested in lists

        if len(numbersFactors[i]) == 1 and list(numbersFactors[i].values())[0] == 1:
            # if there is only 1 prime factor and that its power is equal to 1 it means the number is prime
            isPrime = "a"
            # changes prime discrim to "a" which will say the number is a prime number
        for keys, values in numbersFactors[i].items():
            # finds the keys and values in the nested dictionary (where keys are factors, and values are powers)
            factorMessage += "\033[96m" + str(keys) + "\033[0m" + "^" + "\033[96m" + str(values) + "\033[0m" + " x "
            # formats the string message for each factor and power // CONCATENATION

        print(f"\n{textSep} \n")
        print(f"|   The integer \033[96m{numbersList[i]}\033[0m: \n|\n|   Is \033[96m{isPrime}\033[0m prime \n|")
        # splices the original string message so not to include the " x " as it is redundant
        print(f"|   and has the factors of {factorMessage[:len(factorMessage)-3]}")
        # splices the original string message so not to include the " x " as it is redundant
        print(f"{textSep}\n")
        # prints the message
        time.sleep(1)
        # waits one second

    for dictionaries in numbersFactors:
        # for all of the nested dictionaries in the list holding the factors
        for keys, values in dictionaries.items():
            # loops through all factors and their powers in the nested dictionaries
            if leastCommonMultiple.get(keys, 0) < values:
                # if the current factors is less than the one in iteration
                # or if the factor does not exist yet
                leastCommonMultiple[keys] = values
                # the dictionary leastCommonMultiple has the factor and power added to it // DICTIONARY BEING ALTERED

    for keys, values in leastCommonMultiple.items():
        # for the factors and powers in the leastCommonMultiple factors
        LCM *= keys**values
        # changing the LCM to an integer variable to represent the least common multiple, rather than a string
        # in the form of its prime factorization
        # by multiplying the values into the LCM integer which starts at 1

    if numberQuantity > 1:
        # this code only runs if more than one number was requested to be evaluated
        GCF = 1
        # initially defines gcf as 1
        gcfFactors = dict(numbersFactors[0])
        # initially defines the first factors of
        gcfFactorMessage = ''
        # initializes an empty string that will be manipulated later

        for dictionary in numbersFactors:
            # will go through all nested dictionary factors in the numbersFactors
            for keys, values in dictionary.items():
                # for the keys and values in the dictionary
                for dictionaries in numbersFactors:
                    # these single keys will also be compared to all dictionaries
                    if keys in gcfFactors and keys in dictionaries:
                        # and if they are in both of them it means that there is a common factor // AND LOGIC OPERATOR
                        if gcfFactors[keys] > values:
                            # but only if it is lesser than the existing value of the factor
                            # the gcf factors has its power reassigned
                            gcfFactors[keys] = values
                            # // UPDATING DICTIONARY
                    else:
                        # else statement // BOOLEAN LOGIC (IF THE FIRST COMPARISON WAS FALSE, THEN THIS CODE RUNS)
                        gcfFactors.pop(keys, None)
                        # if the factor is not present in both dictionaries then it will be popped
                        # if the value isnt in the gcfFactor list it returns None instead of giving a keyerror
                        # as it is not a common factor between all numbers

        for keys, values in gcfFactors.items():
            # for the final factors remaining in the gcfFactor dictionary
            GCF *= keys**values
            # we multiply the values out to get an integer value

        if GCF == 1:
            gcfFactors = {'any prime': 0}
            # if gcf is still 1 it means there are no factors inside
            # so we should provide a value to be printed
            # as 1 does not fall under the definition of a prime or composite

        for keys, values in leastCommonMultiple.items():
            # for the factors and powers in the leastcommonmultiple dict
            lcmFactorMessage += "\033[96m" + str(keys) + "\033[0m" + "^" + "\033[96m" + str(values) + "\033[0m" + " x "
            # formats the string message

        for keys, values in gcfFactors.items():
            # for the factors and powers in the gcf factor dict
            gcfFactorMessage += "\033[96m" + str(keys) + "\033[0m" + "^" + "\033[96m" + str(values) + "\033[0m" + " x "
            # formats the string message

        print(f"\n{textSep}\n\n|   The integers", end="")
        for numbers in numbersList:
            print(f", \033[96m{numbers}\033[0m", end="")
        print(f" have a LCM of \033[96m{LCM}\033[0m \n|\n|   which has the factors of {lcmFactorMessage[:len(lcmFactorMessage)-3]}\n|")
        print(f"|   and have a GCF of \033[96m{GCF}\033[0m \n|\n|   which has the factors of {gcfFactorMessage[:len(gcfFactorMessage)-3]}")
        print(f"{textSep}")

        if numberQuantity == 2:
            # this code runs only if there are 2 numbers
            number1 = numbersList[0]
            number2 = numbersList[1]
            # defines these number initally
            if number1 > number2:
                # if number 1 is greater than number 2 then we define it to be larger
                numberLarge = number1
                numberSmall = number2
            else:
                # otherwise number 2 will be the larger number
                numberLarge = number2
                numberSmall = number1

            if numberLarge % numberSmall == 0:
                # if the numbers perfectly divide each other
                time.sleep(1)
                # delays by one second
                print(f"\n\n{textSep}\n\n|   The quotient of \033[96m{numberLarge}\033[0m ÷ \033[96m{numberSmall}\033[0m \n|")
                print(f"|   is \033[96m{int(numberLarge/numberSmall)}\033[0m")
                print(f"{textSep}")
                # prints messages using f string and converts the quotient to an integer
            else:
                time.sleep(1)
                print(f"\n\n{textSep}\n\n|   The quotient of \033[96m{numberLarge}\033[0m ÷ \033[96m{numberSmall}\033[0m \n|")
                print(f"|   is about \033[96m{round(numberLarge/numberSmall, 3)}\033[0m\n|")  # (rounds the quotient to 3 decimal places) // ROUND
                print(f"|   or in exact terms has the quotient of \033[96m{math.floor(numberLarge/numberSmall)}\033[0m\n|")
                print(f"|   and has a remainder of \033[96m{numberLarge % numberSmall}\033[0m")
                print(f"{textSep}")
                # prints message using f string, and will round the quotient to 3 decimal places
                # along with exact quotient and remainder values
    
    time.sleep(3)
    # waits 3 seconds
    returnToMenu = input("\n\nReturn to main menu? (press \033[96menter\033[0m)\n\n")
    # asks user for input afterwards if they would like to return to the main menu
    if returnToMenu or returnToMenu == "":
        # if there are letters in the input or if it is empty this runs (always runs)
        mainMenu()
        # calls mainMenu function // CALLING FUNCTION


def primeFactorization(num):
    numberToFactor = num
    # creates variable of the original number which will be manipulated
    primes = primesTo100000
    # generates a list of primes between 2-the inputted number
    primeFactorList = []
    # initializes a list that will have the prime factors appended to them // LIST
    primeFactorDict = {}
    # initializes a dictionary which will be the final value returned
    # having a key and a value is far more suitable for prime factorization rather than a list

    if numberToFactor == 1:
        # if the number given is 1
        primeFactorDict['\033[96mAny Prime'] = 0
        # defines the value of the any prime as zero
        # this is because 1 does not fall into the category of prime or composite
        return primeFactorDict
        # returns the factor dictionary and the rest of the code does not run

    while numberToFactor != 1:
        # when a number is divided by itself it equals open // WHILE LOOP
        # so after it is divided by all prime factors it is equal to one and the loop breaks
        for i in range(len(primes)):
            # loops through all primes in the prime list
            if numberToFactor % primes[i] == 0:
                # if the number is divisible by a prime factor // COMPARISON (EQUAL TO)
                while numberToFactor % primes[i] == 0:
                    # then we will find how many times it divides into it (can be once as well)
                    primeFactorList.append(primes[i])
                    # and will append it to the list as accordingly // APPENDING VALUES TO LIST
                    numberToFactor /= primes[i]
                    # divides the number by the factor to ensure this // OPERATOR (DIVISIONI)
            if primes[i] > numberToFactor:
                # if the prime factor being tested surpasses the number itself then no more factors are needed to be tested
                break
                # // BREAK

    for factors in primeFactorList:
        # for the factors in the list
        primeFactorDict[factors] = primeFactorList.count(factors)
        # a new key is created and its value is how many factors of it exists

    return primeFactorDict


def primeNumberGenerator(numLimit):
    # this function is based off the sieve of eratosthenes
    # learn more about it in this video
    # https://www.youtube.com/watch?v=Lj_SzTGr-G4&ab_channel=EddieWoo #

    listLoopValue = 1
    # this value will be the one looping through the list of integers
    primeNumbers = []
    # initializes an empty list which will be manipulated
    if numLimit == 1:
        return None
    for i in range(2, numLimit + 1):
        # appends numbers within the limit given using for loop
        primeNumbers.append(i)

    for discriminator in range(numLimit):
        if primeNumbers[discriminator]**2 > numLimit:
            # when the prime factor squared is greater than the initial number limit
            # all remaining numbers are prime (see reasoning in the video)
            break
        listLoopValue = discriminator + 1
        # we don't want to remove the prime that we are dividing everything by
        while listLoopValue < len(primeNumbers):
            # Once the prime squared is equal to the limit
            # all remaining numbers are prime (for information see linked page at the top)
            if primeNumbers[listLoopValue] % primeNumbers[discriminator] == 0:
                # if the value is divisible by a prime then it is not prime
                primeNumbers.pop(listLoopValue)
                # so it is removed
                continue
                # skips this iteration as if the value is removed then the next value will have the same
            listLoopValue += 1

    return primeNumbers

global primesTo100000
# creates global variable of primes up to 100000 (it can be used in all functions)
primesTo100000 = primeNumberGenerator(100000)
# defines the variable by calling the function primeNumberGenerator
# this will make the program more effecient as it does not have to call the function numerous times

mainMenu()
# calls menu function
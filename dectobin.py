while True:    
    try:
        number = int(input("Enter any number: "))
        binary = bin(number)
        print("The binary representation of the number is " + str(binary))
        break
    except KeyboardInterrupt:
        print("You cancelled the program")
    except ValueError:
        print("Incorrect values entered")
    except NameError:
        print("Incorrect values entered")

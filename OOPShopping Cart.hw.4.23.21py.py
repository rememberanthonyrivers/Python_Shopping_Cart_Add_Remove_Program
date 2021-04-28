print('''
<><> My shopping Cart <><>

   Here are your options
      to choose from:
        
        1: Add 
        2: Remove
        3: Show Cart
        4: Exit
''')

whattodo = int(input("Choose an option(1 - 4): "))

while whattodo != 0:
    if whattodo == 1:
        item = input("Enter an item: ")
        quantity = int(input("Enter an amount: "))
        basket = quantity 

    elif whattodo == 2:
        item = input("Enter an option: ")
        del(basket)

    elif whattodo == 3:
        for item in basket:
            print(item,":", basket)
    
    elif whattodo != 0:
        print("Succes! Your good to go.")

    whattodo = int(input("\nEnter an option: "))

else:
    print('See you soon!')



from sys import argv


def main():
    # Sample code to read inputs from the file
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()
    for line in lines:
        # Using a dictionary is probably the best way to represent all the available data at once, more like a struct or a class instance.
        data = {'TSHIRT': {'Category': 'Clothing', 'Price': 1000, 'Discount': 0.1},
                'JACKET': {'Category': 'Clothing', 'Price': 2000, 'Discount': 0.05},
                'CAP': {'Category': 'Clothing', 'Price': 500, 'Discount': 0.2},
                'NOTEBOOK': {'Category': 'Stationery', 'Price': 200, 'Discount': 0.2},
                'PENS': {'Category': 'Stationery', 'Price': 300, 'Discount': 0.1},
                'MARKERS': {'Category': 'Stationery', 'Price': 500, 'Discount': 0.05}}
        inventory = {}  # initially nothing
        itemAdd = ['ADD_ITEM']  # using a list with 0th index as adding command
        itemPrint = ['PRINT_BILL']  # likewise for the printing part
        max = {'Clothing': 2, 'Stationery': 3}  # setting the limits
    # splitting the line into different commands, then checking if a certain command matches with previously defined ones
    for line in lines:
        command = line.split(' ')
        for i in range(len(command)):
            # reconfig back in the form of a list and not a single string
            command[i] = ''.join(command[i].split())
        # adding an item:
        if(command[0] in itemAdd):
            inventory.setdefault(command[1], 0)
            temp = inventory[command[1]]+int(command[2])
            if(temp > max[data[command[1]]['Category']]):
                print('ERROR_QUANTITY_EXCEEDED')
            else:
                inventory[command[1]] += int(command[2])
                print('ITEM_ADDED')
        # Printing:
        elif(command[0] in itemPrint):
            total = 0
            discount = 0
            output = ''
            for item in inventory:
                discount = discount + \
                    ((data[item]['Discount']*data[item]['Price'])*inventory[item])
                total += (data[item]['Price']*inventory[item])
            if(total >= 1000):
                total -= discount
            else:
                discount = 0
            if(total >= 3000):
                extraDiscount = total * 0.05
                discount += extraDiscount
                total = total-(total*0.05)
            print('TOTAL_DISCOUNT '+str("%.2f" % discount))
            total = total+(total*0.1)
            print('TOTAL_AMOUNT_TO_PAY '+str("%.2f" % total))
            inventory.clear()  # clearing to wipe it out for the next session.
        # bad input:
        else:
            print('Enter a valid command')


if __name__ == "__main__":
    main()

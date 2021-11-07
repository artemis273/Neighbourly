clothing = {'winter coats': ['small', 'medium', 'large'], 'fall coats':['small', 'medium', 'large'], 'tops': ['small', 'medium', 'large'], 'bottoms': ['large', 'extra large'],
            'sneakers':['6', '7', '10'], 'boots':['4', '5', '13'], 'socks': ['small', 'large']}
itemsNeeded = {'winter coats': ['large'], 'fall coats':['small', 'medium', 'large'], 'tops': ['small', 'medium', 'large'], 'bottoms': ['large', 'extra large'],
             'sneakers':['6', '10'], 'boots':['4', '5', '13'], 'socks': ['large']}
pendingPickup ={'winter coats': ['small', 'medium', 'large'], 'fall coats':['small', 'medium', 'large'], 'tops': ['small', 'medium', 'large'], 'bottoms': ['large', 'extra large'],
            'sneakers':['6', '7', '10'], 'boots':['4', '5', '13'], 'socks': ['small', 'large']}

def give ():

    print("What article of clothing would you like to donate?\nThe options are as follows\nwinter coats\nfall coats\ntops\nbottoms\nsneakers\nboots\nsocks")
    category = input("Type your selction")

    if category == 'winter coats':
        size = input("What size is the coat?")
        clothing['winter coats'].append(size)

    if category == 'fall coats':
        size = input("What size is the coat")
        clothing['fall coats'].append(size)

    if category == 'tops':
        size = input("What size is the top")
        clothing['tops'].append(size)

    if category == 'bottoms':
        size = input('What size are the bottoms')
        clothing['bottoms'].append(size)

    if category == 'sneakers':
        size = input("What size are the sneakers?")
        clothing['sneakers'].append(size)

    if category == 'boots':
        size = input("What size are the boots?")
        clothing['boots'].append(size)

    if category == 'socks':
        size = input("What size are the boots?")
        clothing['socks'].append(size)

    else:
        print('Article of clothing not found')
    
    print(clothing)

def request():

    print ("What article of clothing are you looking for?\nThe options are as follows\nwinter coats\nfall coats\ntops\nbottoms\nsneakers\nboots\nsocks")
    category = input("Type your selection")

    if category == 'winter coats':
        size = input("What size is the coat?")
        if size in clothing[category]:
            print('Match Found ' + size)
            pendingPickup[category].append(size)
            clothing[category].remove(size)
        else:
            itemsNeeded[category].append(size)

    if category == 'fall coats':
        size = input("What size is the coat")
        if size in clothing[category]:
            print('Match Found ' + size)
            pendingPickup[category].append(size)
            clothing[category].remove(size)
        else:
            itemsNeeded[category].append(size)

    if category == 'tops':
        size = input("What size is the top")
        if size in clothing[category]:
            print('Match Found ' + size)
            pendingPickup[category].append(size)
            clothing[category].remove(size)
        else:
            itemsNeeded.append(size)

    if category == 'bottoms':
        size = input('What size are the bottoms')
        if size in clothing[category]:
            print('Match Found ' + size)
            pendingPickup[category].append(size)
            clothing[category].remove(size)
        else:
            itemsNeeded[category].append(size)

    if category == 'sneakers':
        size = input("What size are the sneakers?")
        if size in clothing[category]:
            print('Match Found ' + size)
            pendingPickup[category].append(size)
            clothing[category].remove(size)
        else:
            itemsNeeded[category].append(size)

    if category == 'boots':
        size = input("What size are the boots?")
        if size in clothing[category]:
            print('Match Found ' + size)
            pendingPickup[category].append(size)
            clothing[category].remove(size)
        else:
            itemsNeeded[category].append(size)
            
    if category == 'socks':
        size = input("What size are the boots?")
        if size in clothing[category]:
            print('Match Found ' + size)
            pendingPickup[category].append(size)
            clothing[category].remove(size)
        else:
            itemsNeeded[category].append(size)

    else:
        print("Category of clothing not found")


def checkMatches():
    '''
    iterates through both dictionaries and removes the matches, sends them to pendingPickup dict
    '''
                
    
    

def main():
    x = input("Type Donate to add a donation or Type Request to request an item")

    if x == Donate:
        give()
    if x == Request:
        request()
    else:
        print("Invalid input")

    #checkMatches()
            
            
main()


clothing = {'winter coats': ['small', 'medium', 'large'], 'fall coats':['small', 'medium', 'large'], 'tops': ['small', 'medium', 'large'], 'bottoms': ['large', 'extra large'],
            'sneakers':['6', '7', '10'], 'boots':['4', '5', '13'], 'socks': ['small', 'large']}
itemsNeeded = []

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
        for size in clothing[category]:
            print('Match Found' + size)

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
    
    
give()

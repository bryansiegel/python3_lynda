def main():
    animals = dict(kitten = 'meow', dog = 'ruff', lion = 'grr')
    # animals = { 'kitten': 'meow', 'puppy': 'ruff', 'lion': 'grr' }
    
    #ternary operator
    #print('found' if 'kitten' in animals else 'nope')
    
    #get method does not return exception
    print(animals.get('godzilla'))
    
    print_dict(animals)

def print_dict(o):
    # for x in o: print(f'{x}: {o[x]}')
    
    #items
    # for k, v in o.items(): print(f'{k}, {v}')
    
    #values
    # for v in o.values(): print(v)

    #keys
    for k in o.keys(): print(k)

if __name__ == "__main__": main()
        

for i in range (1,10):
    for j in range (1,11):
        if i in {1,9} or j in {1,10}:
            print ('-', end = '')
        else:
            print ('*', end = '')
    print()
            
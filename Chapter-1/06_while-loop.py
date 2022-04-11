while True:
    x=input("Enter a number to count to: ")
    if x == "q" or x == "Q" or x == "quit" or x == "Quit" or x == "QUIT":
        break
    
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break


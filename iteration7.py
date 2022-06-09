rabbit = 0
while True:
    if rabbit % 3 == 1:
        if rabbit % 5 == 3:
            if rabbit % 7 == 2:
                print(rabbit)
                break
    rabbit += 1
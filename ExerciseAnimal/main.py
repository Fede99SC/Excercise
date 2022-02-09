from animal import Dog,Lion,Mouse,LadyBug, Zebra

if __name__ == '__main__':
    mylist = [Dog(), Lion(), Mouse(), LadyBug(), Zebra()]
    [mylist[i].move() for i in range(len(mylist))]

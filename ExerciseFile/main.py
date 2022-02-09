import class_find


if __name__ == '__main__':
    find = class_find.Find(8)

    if(find.is_find(8) == True):
        print("Present!")
    else:
        print("Not Present!")
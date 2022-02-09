import random, uuid

if __name__ == '__main__':
    mylist = [random.randint(0,200) for i in range(50)]
    mylist.sort()
    mylist = [str(uuid.uuid4()) for i in range(50)]
    str_of_guid = ';'.join(mylist)
    print(str_of_guid)
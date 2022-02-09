class Find:

    def __init__(self, pos):
        """
        :param pos:
        """
        self.pos = pos

    def read_file(self):
        """
        :return: mylist
        """
        mylist = []
        with open("myfile.txt") as myfile:
            for line in myfile:
                mylist = line.split(",")
        return mylist


    def is_find(self, pos):
        """
        :param pos:
        :return:
        """
        mylist = self.read_file()
        find = False
        try:
            if mylist[pos] != "":
                find = True
                return find
            else:
                return find
        except IndexError:
            return find
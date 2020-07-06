"""
Assignment 1 - PS1 - [Box Office]
Group No. 145
"""


class ticketSystem(object):

    # Implementation of queue data structure.
    def __init__(self, w, n):
        self.n = n
        self.w = w
        self.queues = [[None for i in range(n)] for j in range(w)]
        self.starts = [0 for i in range(w)]
        self.ends = [0 for i in range(w)]
        self.size = [0 for i in range(w)]
        self.open = [False for i in range(w)]
        self.open[0] = True

    def getWindow(self, windowId):
        # [TODO]: Add logic part
        return True

    def isOpen(self, windowId):
        # [TODO]: Add logic part
        return True

    def addPerson(self, personId):
        # [TODO]: Add logic part
        return 'XYZxxxx'

    def giveTicket(self):
        # [TODO]: Add logic part
        return True


# Helps to prepossess input from input file.
def split_input_line(line):
    val = line.strip().split(':')
    if len(val) == 3:
        return int(val[1]), int(val[2])
    elif len(val) == 2:
        return int(val[-1])
    else:
        return 'Invalid Line'


# Input and Output part is working fine. No more changes required.
# If any changes requires highlight on particular line.
if __name__ == "__main__":
    output = open("outputPS1.txt", "a")
    with open("inputPS1.txt") as f:
        for line in f:
            val = split_input_line(line)
            res = None
            if line.startswith('ticketSystem'):
                obj = ticketSystem(val[0], val[1])
            elif line.startswith('isOpen'):
                res = obj.isOpen(val)
            elif line.startswith('getWindow'):
                res = obj.getWindow(val)
            elif line.startswith('addPerson'):
                res = obj.addPerson(val)
            elif line.startswith('giveTicket'):
                res = obj.giveTicket()
            else:
                print('Wrong Input!!!')
            if res:
                output.write(res + '\n')    # Writing result into output file.

    f.close()
    output.close()

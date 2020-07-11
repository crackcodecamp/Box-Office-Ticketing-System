"""
Assignment 1 - PS1 - [Box Office]
Group No. 145
"""


class ticketSystem(object):

    def __init__(self, w, n):
        """
        Implementation of queue data structure.

        :param w: Number of Windows
        :param n: Number of persons in each window
        """

        self.n = n
        self.w = w

        self.queues = [[None for i in range(n)] for j in range(w)]
        self.starts = [0 for i in range(w)]
        self.ends = [0 for i in range(w)]
        self.size = [0 for i in range(w)]
        self.open = [False for i in range(w)]
        self.open[0] = True

    def getWindow(self, windowId):
        """
        Return the number of persons available in a window.

        :param windowId: Window number
        :return: All available persons waiting for ticket in that window.
        """
        windowInfo = [item for item in self.queues[windowId - 1] if
                      item is not None]

        return windowInfo

    def isOpen(self, windowId):
        """
        To check weather window is open or not.

        :param windowId: Window number
        :return: True or False
        """
        return self.open[windowId - 1]

    def addPerson(self, personId):
        """
        Add Person checks first for queue allocation/window

        :param personId:
        :return:
        """
        window = self.eligibleQueueforInsert()

        if window == -1:
            return "all queues are full"
        else:
            # add person performfed through Queue operation
            # it accepts personId and which Window to add
            self.enqueue(personId, window)

            return "w" + str(window)

    def giveTicket(self):
        """
        Returns No of tickets were issued

            Issues if all the Windows have persons waiting tickets
        it return the tickets maximum of number of windows available.
        This operation handled with Queue operation "dequeue".

        :return: Counter number which provide ticket to the person.
        """
        ticketCounter = 0
        for item in range(self.w):
            res = self.dequeue(item)
            if res != -1:
                ticketCounter += 1
        if ticketCounter == 0:
            return "Queue is Empty"
        else:
            return str(ticketCounter)

    def enqueue(self, personId, window):
        """
        Queue operation to insert a element into the queue.

        :param personId: Person number to insert
        :param window: In which Window person needs to assigned
        :return: None
        """
        # insert Item into Queue
        index = self.queues[window - 1].index(None)
        self.queues[window - 1][index] = personId

    def dequeue(self, windowId):
        """
        Performing dequeue operation for the queue.

        :param windowId: Item to remove from which Window.
        :return: Item deleted from Queue.
        """
        if self.isEmptyQ(windowId):
            return -1
        else:
            person = self.queues[windowId - 1][0]
            del self.queues[windowId - 1][0]
            self.queues[windowId - 1].append(None)
            return person

    def sizeQ(self, windowId):
        """
        Queue operation - Get the size of the queue.

        :param windowId: Label of the window.
        :return: Queue Size (int)
        """
        # if no None means  maximum of queue length
        if None not in self.queues[windowId - 1]:
            return self.n
        else:
            return self.queues[windowId - 1].index(None)

    def isEmptyQ(self, windowId):
        """
        Queue operation - To check is queue is empty or not.

        :param windowId: check whether the Queue associated to WindowId is
                        empty or not.
        :return: empty : Boolean
                    True for empty or yet to open Window
                    False for queue with items
        """
        if not self.isOpen(windowId):
            return True
        empty = True
        if None in self.queues[windowId - 1] and \
                self.queues[windowId - 1].index(None) == 0:
            empty = True
        else:
            empty = False
        return empty

    def frontQ(self, windowId):
        """

        :param windowId:
        :return:
        """
        if not (self.isEmptyQ(windowId - 1)):
            return self.queues[windowId - 1][0]
        else:
            return -1

        # Return, but do not remove, the front object in the queue,

    def eligibleQueueforInsert(self):
        """
        If more than one window has the least number of people,
        then the system can prompt the person to join the first
        window (smaller window Id) it encounters with the
        least number of people.

        :return: Window number to insert
                -1 if All Queue are full and no more allowed to insert
        """
        if False in self.open:
            # check howmany windows are already opened
            getOpenWindows = self.open.index(False)

        else:
            getOpenWindows = self.w
        min_queue = self.sizeQ(1)  # Get details from First window
        window = 1

        for n in range(1, getOpenWindows + 1):
            # Iterate all the Windows to check for min Queue length
            length = self.sizeQ(n)
            if min_queue > length:
                min_queue = length
                window = n
        # if Queue Length is equal to maximum queue size
        if min_queue == self.n:
            # Check all the Windows opened and no more allowed to insert
            if getOpenWindows == self.w:
                return -1
            else:
                # If all the open Windows are full then open new Queue
                self.open[getOpenWindows] = True
                window = getOpenWindows
                return window + 1
        else:
            return window


def split_input_line(input):
    """
    The method helps to prepossess the input from the input file.

    :param input: Split the incoming input.
    :return: parameter to pass to method.
    """
    value = input.strip().split(':')

    if len(value) == 3:
        return int(value[1]), int(value[2])
    elif len(value) == 2 and value[-1]:
        return int(value[-1])
    else:
        return 'Invalid Input'


# Input and Output part is working fine. No more changes required.
# If any changes requires highlight on particular line.
if __name__ == "__main__":
    output = open("outputPS1.txt", "a")
    # TODO: Ask for input file. Use try cache to handle the exception if file is not available.
    try:
        input_file = input("Enter Input file name located in current "
                           "directory(e.g. inputPS1.txt): ").strip()

        with open(input_file) as f:
            for line in f:
                val = split_input_line(line)
                res = None
                final_output = None
                if line.startswith('ticketSystem'):
                    obj = ticketSystem(val[0], val[1])
                elif line.startswith('isOpen'):
                    res = obj.isOpen(val)
                    final_output = line.strip() + " >> " + str(res)
                elif line.startswith('getWindow'):
                    res = obj.getWindow(val)
                    final_output = line.strip() + " >> " + str(res)
                elif line.startswith('addPerson'):
                    res = obj.addPerson(val)
                    final_output = line.strip() + " >> " + str(res)
                elif line.startswith('giveTicket'):
                    res = obj.giveTicket()
                    final_output = line.strip() + " >> " + str(res)
                else:
                    print('Wrong Input!!!')
                if res:
                    # Writing result into output file.
                    output.write(final_output + '\n')

        f.close()
        output.close()
        print('Execution of input file is completed. '
              'Please find `outputPS1.txt` for execution result.')

    except NameError:
        print('ERROR!!!\n\tEntered file is not available in this directory.'
              'Please provide valid input file.')

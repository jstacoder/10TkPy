import random

class Die(object):
    _faces = [None, 'One', 'Two', 'Three', 'Four', 'Five', 'Six']

    def __init__(self, sideNumber=6):
        if not(sideNumber <=0):
            self.sides = sideNumber
        else:
            raise ValueError('Need a positive integer')
        self.roll()

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        rtn = '<<{0}>>[{1}]'.format(self.face, self.value)
        return rtn

    def __int__(self):
        return self.value
    
    def _reset_value(self, num=None):
        if num is None:
            self.rollNum = self.sides
        else:
            self.rollNum = num

        self._value = random.randrange(1, (self.rollNum + 1))

    def _reset_face(self):
        self.face = Die._faces[self._value]

    def roll(self, num=None):
        self._reset_value(num)
        self._reset_face()


    def _get_value(self):
        return int(self._value)

    value = property(_get_value)

    def __iter__(self):
        return self.__next__()

    def __next__(self):
        self.track = 1
        if self.track == 1:
            return iter(self.value)
        else:
            raise StopIteration

class Roll(object):
    def __init__(self, rollNumber=None):
        if rollNumber is None:
            self.rollNumber = 6
        #elif rollNumber >= 70 or rollNumber <= 0:
        #    raise ValueError('Need a decent roll')
        else:
            self.rollNumber = rollNumber
        self.dice = [][:]
        self.roll_dice()

    def __str__(self):
        rtn = 'Rolled: {0}'.format(' ,'.join(map(str, self.dice)))
        return rtn

    def __repr__(self):
        return self.dice

    def __getitem__(self, idx):
        return self.dice[idx]

    def __iter__(self):
        self.crt = 0
        return iter(self.dice)


    def __next__(self):
        if self.crt == len(self.dice):
            raise StopIteration
        else:
            item =  self.dice[self.crt]
            self.crt += 1
            return item
        
    def __contains__(self, itm):
        return itm in self.dice

    def _reset_dice(self, num=None):
        self.lastRoll = self.dice[:]
        if num == None:
            rollNum = self.rollNumber
        else:
            rollNum = num
        self.held = [][:]
        tmpRoll = [0]*self.rollNumber
        self.dice = tmpRoll[:]
        for die in range(rollNum):
            self.dice[die] = Die()
    
    def roll_dice(self, num=None):
        self._reset_dice(num)

    def _reset_some(self):
        for i in range(len(self.dice)):
            if self.dice[i] is None or self.dice[i] == 0:
                pass
            else:
                self.dice[i].roll()
    
    def _hold_die(self,ndx):
        if not(len(self.dice)+2 > ndx):
            raise IndexError
        else:
            ndx = ndx - 1
            self.held.append(self.dice[ndx])
            self.dice[ndx] = 0

    def hold_die(self, ndx):
        self._hold_die(ndx)

    def _print_held(self):
        return self.held

    def print_last(self):
        return self.lastRoll

    print_held = property(_print_held)
    


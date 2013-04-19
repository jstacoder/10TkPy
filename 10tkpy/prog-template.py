'''
    __name__ =
    __version__ = 0.0.1
    __author__ = 'kyle roux'
    __date__ = '4/19/2013'
    __package__ = '10TkPy'  
    __description__ = 'logic to score dice games'

    TODO - 
        * doubles ie: xx,yy,zz -             1000
        * strait  ie: 1,2,3,4,5 -            1000
        * (2,3,4,6) 3 of a kind ie: x,x,x -         x * 100
        * (2,3,4,6) 4 of a kind ie: x,x,x,x -       x * 200
        * (2,3,4,6) 5 of a kind ie: x,x,x,x,x -     x * 400
        * (2,3,4,6) 6 of a kind ie: x,x,x,x,x,x -   x * 800
        * 5 - 1-50,  2-100, 3-500,  4-1000, 5-2000, 6-4000
        * 1 - 1-100, 2-200, 3,1000, 4-2000, 5-4000, 6-8000

        then a general return function

        start with a function to grab and unpack the roll
'''
import sys
from dice import Roll


class RollGrabber(object):
    def __init__(self, aRoll=None):
        if aRoll is None:
            raise ValueError('Need a roll to score!!')
        else:
            self.rolledDiceNumber = 0
            self.roll = [0]*6
            tmpRoll = aRoll.dice[:]
            for i in range(len(tmpRoll)):
                tmp = tmpRoll[i]
                self.roll[i] = tmp
            for i in self.roll:
                if i is not None and not(int(i) == 0):
                    self.rolledDiceNumber += 1
                
        
    def give_roll(self):
        rtn = (self.roll[0], self.roll[1], self.roll[2], 
            self.roll[3], self.roll[4], self.roll[5], 
            self.rolledDiceNumber)
        ''' 
        returning  die1-die6 and 
        the number of non zero dice 
        '''
        return rtn

class Scorer(object):
    def __init__(self, fmtRoll):
        self.die = [0]*7
        self.die[0], self.die[1], self.die[2], self.die[3], self.die[4], self.die[5] = fmtRoll[:-1]
        
    def __str__(self):
        rtn = ' '.join(map(str, self.die[:-1])) #+ ' {0} dice'.format(self.die[6])
        return rtn

class DieCounter(object):
    def __init__(self, dies):
        self.allNums = ['1','2','3','4','5','6']
        for i in self.allNums:
            self[i] = 0
        self.dies = dies[:]
        self.counts = {'1': 0, '2': 0,'3': 0,'4':0,'5': 0,'6': 0}

    def count(self):
        for i in self.dies:
            self.counts[str(i)] += 1
    #   self.make_counts()

    #def make_counts(self):
    #    for i in self.allNums:
    #        self.counts[i] += i

    def return_count(self):
        return self.counts
    
    def __getitem__(self, itm):
        return self.__dict__[itm]


    def __setitem__(self, key, itm):
        self.__dict__[key] = itm

    def __str__(self):
        ret = ''
        for i in self.counts:
            ret = ret + self[i] + " {0}'s".format(i)
        return ret

    def _report_single(self):
        for i in self.counts:
            if self.counts[i] == 1 and i == '1' or i == '5':
                print  'you got 1 {0}'.format(i)
                continue

    def _report_multi(self):
        for i in self.counts:
            if self.counts[i] >= 2:
                if i == '1' or i == '5' and self.counts[i] == 2:
                    print 'you had 2 {0}s'.format(i)
                    continue
                else:
                    if self.counts[i] > 2:
                        print 'you had {0} {1}s'.format(self.counts[i], i)
                        continue



    def report_all(self):
        print self._report_single()
        print self._report_multi()







                    



def main():

    tstRoll = Roll(int(sys.argv[1]))
    sc = RollGrabber(tstRoll)
    print sc.give_roll()
    for i in tstRoll:
        print str(i) + ' ',
    print
    x = Scorer(sc.give_roll())
    print x
    counter = DieCounter(tstRoll)
    counter.count()
    print counter.return_count()
    counter.report_all()

if __name__ == "__main__":
    main()

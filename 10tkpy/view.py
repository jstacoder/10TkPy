'''
    __file__ = 10tkpy.view.py
    __author__ = 'kyle roux'
    __date__ = '04-16-13'
    __pkg__ = '10tkpy'
'''
from Tkinter import *
import random
import sys

DIES = ('   One', '   Two', ' Three', '  Four', '   Five', '    Six',)
DIEMAP = {'   One': 1, '   Two': 2, ' Three': 3, '  Four': 4, '   Five': 5, '    Six': 6}


class LabelDemo(Frame):
    def __init__(self):
        ''' set up the window widget '''
        Frame.__init__(self)
        self.master.title('10 Tk Py')
        self.grid()
        self._label = Label(self, text="Hello World!")
        self._label.grid()

class DiceRollWidget(Frame):
    """ use DiceRollWidget to keep track of dice rolls """
    global DIES
    global DIEMAP
    _dies = DIES
    _diemap = DIEMAP

    def __init__(self):
        """ set up inital setting and windows """
        Frame.__init__(self)
        self.heldDice = [][:]
        self.heldNumber = 0
        self.dieNum = 6
        self.roll()
        self.master.title('TZP Softwares "10Tk Py"')
        self.grid()
        self.topLabel = Label(self, text="Your Roll:\n\n", font="Sans 18")
        self.topLabel.grid(row=0, column=0)
        self.set_buttons()
        self.rollButton = Button(self, text="Roll Dice", font="Sans 11", command=self.roll)
        self.rollButton.grid(row=50, column=2)
        self.reset_held()
        self.resetButton = Button(self, text="Reset", command=self.reset_held)
        self.resetButton.grid(row=100, column=2)
        self.quitButton = Button(self, text="Quit", command=sys.exit)
        self.quitButton.grid(row=100, column=0)


    def reset_roll_label(self):
        """ update the roll label """
        try:
            self.rollLabel.configure(text=self.make_roll_label_text())
        except AttributeError:
            self.rollLabel = Label(self, text=self.make_roll_label_text(), font="Times 16")
        self.rollLabel.grid(row=1, column=0, columnspan=3)

    def make_roll_label_text(self):
        """ return a string of the current roll """
        return ', '.join(map(str, self.dice))


    def set_buttons(self):
        """ seprate function to set up numbered buttons """
        self.oneHoldButton = Button(self, text="Not Held", font="Times 14", command=self.hold_one)
        self.oneHoldButton.grid(row=2, column=2)
        self.twoHoldButton = Button(self, text="Not Held", font="Times 14", command=self.hold_two)
        self.twoHoldButton.grid(row=3, column=2)
        self.threeHoldButton = Button(self, text="Not Held", font="Times 14", command=self.hold_three)
        self.threeHoldButton.grid(row=4, column=2)
        self.fourHoldButton = Button(self, text="Not Held", font="Times 14", command=self.hold_four)
        self.fourHoldButton.grid(row=5, column=2)
        self.fiveHoldButton = Button(self, text="Not Held", font="Times 14", command=self.hold_five)
        self.fiveHoldButton.grid(row=6, column=2)
        self.sixHoldButton = Button(self, text="Not Held", font="Times 14", command=self.hold_six)
        self.sixHoldButton.grid(row=7, column=2)

    def inc_held(self, number, num=1):
        """ increment the heldNumber number """
        if str(number) in self.heldDice:
            pass
        else:
            self.heldNumber += num
        self._reset_held_label()

    def hold_one(self):
        """ check if button says held or not held and switch """
        if self.oneHoldButton['text'] == "Not Held":
            self.oneHoldButton.configure(text="   Held   ")
            self.inc_held('one')
            self.heldDice.append('one')
        else:
            self.heldNumber -= 1
            self._reset_held_label()
            self.heldDice.remove('one')
            self.oneHoldButton.configure(text="Not Held")

    def hold_two(self):
        """ same as last function and next function """
        if self.twoHoldButton['text'] == "Not Held":
            self.twoHoldButton.configure(text="   Held   ")
            self.inc_held('two')
            self.heldDice.append('two')
        else:
            self.heldNumber -= 1
            self._reset_held_label()
            self.heldDice.remove('two')
            self.twoHoldButton.configure(text="Not Held")

    def hold_three(self):
        """ same as last function and next function """
        if self.threeHoldButton['text'] == "Not Held":
            self.threeHoldButton.configure(text="   Held   ")
            self.inc_held('three')
            self.heldDice.append('three')
        else:
            self.heldNumber -= 1
            self._reset_held_label()
            self.heldDice.remove('three')
            self.threeHoldButton.configure(text="Not Held")


    def hold_four(self):
        """ same as last function and next function """
        if self.fourHoldButton['text'] == 'Not Held':
            self.fourHoldButton.configure(text="   Held   ")
            self.inc_held('four')
            self.heldDice.append('four')
        else:
            self.heldNumber -= 1
            self._reset_held_label()
            self.heldDice.remove('four')
            self.fourHoldButton.configure(text="Not Held")

    def hold_five(self):
        """ same as last function and next function """
        if self.fiveHoldButton["text"] == "Not Held":
            self.fiveHoldButton.configure(text="   Held   ")
            self.inc_held('five')
            self.heldDice.append('five')
        else:
            self.heldNumber -= 1
            self._reset_held_label()
            self.heldDice.remove('five')
            self.fiveHoldButton.configure(text="Not Held")

    def hold_six(self):
        """ same as last function and next function """
        if self.sixHoldButton['text'] == 'Not Held':
            self.sixHoldButton.configure(text="   Held   ")
            self.inc_held('six')
            self.heldDice.append('six')
        else:
            self.heldNumber -= 1
            self._reset_held_label()
            self.heldDice.remove('six')
            self.sixHoldButton.configure(text="Not Held")


    def _reset_held_num(self):
        """ reset held number to 0 and reset held list """
        self.heldNumber = 0
        self.heldDice = [][:]

    def _reset_held_label(self):
        """ refresh heldLabel on screen """
        self.diceHeldLabel = Label(self, text="Dice Held: "  + str(self.heldNumber), font="Sans 11")
        self.diceHeldLabel.grid(row=50, column=0)

    def reset_held(self):
        """ reset all held stats """
        self.set_buttons()
        self._reset_held_num()
        self._reset_held_label()
        self.roll()


    def roll(self, num=None):   # define for custom die implementations
        global DIES
        if num is None:
            num = self.dieNum
        self.dice = [][:]       # copy an empty list
        self.dice = [0] * num   # make an empty list of n size
        for i in range(len(self.dice)):
            self.dice[i] = random.choice(DIES)
        self._reset_dice()

    def _reset_one(self):
        try:
            self.oneLabel.configure(text="1: \t" + self.dice[0] + ' (' + str(DiceRollWidget._diemap[self.dice[0]]) + ')')
        except AttributeError:
            self.oneLabel = Label(self, text="1: \t" + self.dice[0] + ' (' + str(DiceRollWidget._diemap[self.dice[0]]) + ')')
        self.oneLabel.grid(row=2, column=0)

    def _reset_two(self):
        try:
            self.twoLabel.configure(text="2: \t" + self.dice[1] + ' (' + str(DiceRollWidget._diemap[self.dice[1]]) + ')')
        except AttributeError:
            self.twoLabel = Label(self, text="2: \t" + self.dice[1] + ' (' + str(DiceRollWidget._diemap[self.dice[1]]) + ')')
        self.twoLabel.grid(row=3, column=0)

    def _reset_three(self):
        try:
            self.threeLabel.configure(text="3: \t" + self.dice[2] + ' (' + str(DiceRollWidget._diemap[self.dice[2]]) + ')')
        except AttributeError:
            self.threeLabel = Label(self, text="3: \t" + self.dice[2] + ' (' + str(DiceRollWidget._diemap[self.dice[2]]) + ')')
        self.threeLabel.grid(row=4, column=0)

    def _reset_four(self):
        try:
            self.fourLabel.configure(text="4: \t" + self.dice[3] + ' (' + str(DiceRollWidget._diemap[self.dice[3]]) + ')')
        except AttributeError:
            self.fourLabel = Label(self, text="4: \t" + self.dice[3] + ' (' + str(DiceRollWidget._diemap[self.dice[3]]) + ')')
        self.fourLabel.grid(row=5, column=0)

    def _reset_five(self):
        try:
            self.fiveLabel.configure(text="5: \t" + self.dice[4] + ' (' + str(DiceRollWidget._diemap[self.dice[4]]) + ')')
        except AttributeError:
            self.fiveLabel = Label(self, text="5: \t" + self.dice[4] + ' (' + str(DiceRollWidget._diemap[self.dice[4]]) + ')')
        self.fiveLabel.grid(row=6, column=0)

    def _reset_six(self):
        try:
            self.sixLabel.configure(text="6: \t" + self.dice[5] + ' (' + str(DiceRollWidget._diemap[self.dice[5]]) + ')')
        except AttributeError:
            self.sixLabel = Label(self, text="6: \t" + self.dice[5] + ' (' + str(DiceRollWidget._diemap[self.dice[5]]) + ')')
        self.sixLabel.grid(row=7, column=0)

    def _reset_dice(self):
        if 'one' in self.heldDice:
            pass
        else:
            self._reset_one()
        if 'two' in self.heldDice:
            pass
        else:
            self._reset_two()
        if 'three' in self.heldDice:
            pass
        else:
            self._reset_three()
        if 'four' in self.heldDice:
            pass
        else:
            self._reset_four()
        if 'five' in self.heldDice:
            pass
        else:
            self._reset_five()
        if 'six' in self.heldDice:
            pass
        else:
            self._reset_six()
        self.reset_roll_label()




def main():
    DiceRollWidget().mainloop()

if __name__ == "__main__":
    main()
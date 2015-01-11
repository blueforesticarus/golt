#!/usr/bin/env python3

from os import system
import curses
import random
import time
import os
import math


INITIAL_TEXT = """  
    display = Display()
    cols, rows = display.setup()
    

   
            display.refresh()
            pass

        time.sleep(DELAY)
    pass

def stop():
    curses.endwin()


class Simulator:
    display = Display()
    cols, rows = display.setup()
    cols *= 4
    rows *= 2
    
    display.inputText(INITIAL_TEXT)
    display.insertChar(176,47,chr(2))


class Simulator:
    display = Display()
    cols, rows = display.setup()
    cols *= 4
    rows *= 2
    
    display.inputText(INITIAL_TEXT)
    display.insertChar(176,47,chr(2))
    display.insertChar(176,48,chr(23))
    sim = Simulator(cols,rows)

    sim.thisGen = display.getBoolArray(display.text)

    display.refresh()
     
def start():
    global sim, display, running, paused, wait, DELAY

    while running:
        if not paused and not wait:
            sim.step()
            display.update(sim.getArray())
            display.refresh()
            pass

        time.sleep(DELAY)
    pass

def stop():
    curses.endwin()


class Simulator:
class Simulator:      
"""
#---------------------------------------------------------------------------
DELAY =0 

running = True
paused = False
wait = False

ENDIAN='little'#this does nothing

sim = None
display = None

def init():
    global sim, display

    display = Display()
    cols, rows = display.setup()
    cols *= 4
    rows *= 2

    display.inputText(INITIAL_TEXT)
    
    sim = Simulator(cols,rows)    
    sim.thisGen = display.getBoolArray(display.text)
    
    sim.glider(60,70)
    display.insertChar(10,5,chr(2))
    display.insertChar(10,6,chr(23))

    display.refresh()
     
def start():
    global sim, display, running, paused, wait, DELAY

    while running:
        if not paused and not wait:
            sim.step()
            display.update(sim.getArray())
            display.refresh()
            pass

        time.sleep(DELAY)
    pass

def stop():
    curses.endwin()


class Simulator:
    rows = None
    cols = None

    thisGen = []
    nextGen = []

    def __init__(self,cols,rows):
        self.cols = cols
        self.rows = rows
        self.thisGen = self.initGrid(cols,rows)
        self.nextGen = self.initGrid(cols,rows)

    def initGrid(self, cols, rows):
        array=[]
        for col in range(cols):
            arrayCol = []
            for row in range(rows):
                arrayCol += [False]

            array += [arrayCol]

        return array

    def step(self):
        for col in range(self.cols):
            for row in range(self.rows):
                self.nextGen[col][row] = self.checkCell(col, row)
                
        #Alex Martelli's opinion (at least back in 2007) about this is, that it is a weird syntax and it does not make sense to use it ever.
        self.thisGen = [col[:] for col in self.nextGen]
        
    def checkCell(self, x, y):
        living = 0 #number of living neighboring cells
        for x1 in [-1, 0, 1]:
            for y1 in [-1, 0, 1]:
                if not(x1 == y1 == 0):
                    col=(x1+x)%self.cols 
                    row=(y1+y)%self.rows         
                    if self.thisGen[col][row]:                           
                        living += 1

        if self.thisGen[x][y] == True and living < 2:
            return False
        elif self.thisGen[x][y] == True and living > 3:
            return False
        elif self.thisGen[x][y] == False and living == 3:
            return True
        else:
            return self.thisGen[x][y]
            
    def getArray(self): 
        return self.thisGen[:]

    def setCell(self,x,y,bool):
        self.thisGen[x][y] = bool

    def glider(self,x,y):
        self.setCell(x,y,True)
        self.setCell(x-1,y,True)
        self.setCell(x-2,y,True)
        self.setCell(x,y-1,True)
        self.setCell(x-1,y-2,True)


class Display:  
    screen = None
    text = None
    rows = 0
    cols = 0
    #modified=False
    #needsRefresh=False
    
    def __init__(self):
        self.screen = curses.initscr()
        pass

    #array is an aray of booleans from simulator
    def getCharArray(self, array):
        text=[]
        if(len(array)%4 == 0 and len(array[0])%2 == 0):
            cols = int(len(array)/4)
            rows = int(len(array[0])/2)
            for col in range(cols):
                textCol = []
                for row in range(rows):
                    binary = []
                    for y in range(2):
                        for x in range(4):
                            binary += [array[col*4 + x][row*2 + y]]
                    textCol += [self.getChar(binary)]
                text += [textCol]
        else:
            #invalid simulator board
            text += [-1]
        
        return text
        
    def getText(self, array):
        text = ""
        for row in range(self.rows):
            for col in range(self.cols):
                text += self.text[col][row]
            
    def inputText(self, text):
        for row in range(self.rows):
            for col in range(self.cols):
                try:
                    self.text[col][row]= text[col+(row*self.cols)]
                except:
                    self.text[col][row]=chr(0)
    
    def getChar(self, array):
        if len(array) is not 8:          
            #problem
            return None            

        charCode = 0
        for bit in array:
            charCode *= 2
            charCode += 1 if bit else 0

        return chr(charCode)

    def getBinaryChar(self, char):
        charCode = ord(char)  
        binary = []
        while charCode != 0:
            bit = charCode % 2 == 1
            binary.insert(0, bit)
            charCode = math.floor(charCode / 2)

        while len(binary)<8:
            binary.insert(0, False)

        return binary

    
    def getBoolArray(self, array):
        cols = len(array)
        rows = len(array[0])
        boolArray = Simulator.initGrid(None, cols*4,rows*2)
        
        for col in range(cols):
            for row in range(rows):
                binary = self.getBinaryChar(array[col][row])
                for x in range(4):
                     for y in range(2):
                          boolArray[col*4 + x][row*2 + y] = binary[x + 4*y]
                            
        return boolArray

    def setup(self):
        os.system('clear')
        self.cols = self.screen.getmaxyx()[1]-1
        self.rows = self.screen.getmaxyx()[0]
        array=[]
        for col in range(self.cols):
            arrayCol = []
            for row in range(self.rows):
                arrayCol += [chr(0)]
            array += [arrayCol]

        self.text = array
        return self.cols , self.rows
        
    def update(self, array):
        self.text = self.getCharArray(array)
        
    def refresh(self):
        for col in range(self.cols):
            for row in range(self.rows):
                char = self.text[col][row]
                if char == chr(0):
                    char = " "
                else:
                    char = char
                try:
                    self.screen.addch(row, col, char)

                except:
                    pass

        #print(self.text)
        self.screen.refresh()
        
    def insertChar(self, col, row, char):
        self.text[col][row] = char
    
    def getSimGrid(self):
        return self.getBoolArray(self.text)
    
init()
start()
stop()



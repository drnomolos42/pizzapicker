#!/usr/bin/python

import re
import sys

global EaterSet 
EaterSet = set()
ObjectList = []

class pizzaEater(object):

    def __init__(self, name):
        self.name = name
        self.toppingPreference = set()

    def hello(self):
        return "hello"

    def toppingValidater(self, topping):
        self.pizza_toppings = set([ "pepperoni", 
                                    "sausage", 
                                    "meatball", 
                                    "canadian bacon"])
        if topping in self.pizza_toppings:
            return True
        else:
            return False 

def topinput():
    print "1. Enter name"
    print "2. List users and topping selections"
    print "3. Complete order"
    print "4. Exit"
    topoption = raw_input("")
    if re.match('4', topoption):
        print "Exiting"
        sys.exit(0)
    if re.match('1', topoption):
        return 1
    if re.match('2', topoption):
        return 2
    if re.match('3', topoption):
        return 3
    print "You need to select 1, 2 or 3"
    topinput()

def PreferredToppingInput(EaterObject):
    topping = raw_input("Please enter a topping, or press enter when complete. ")
    if re.match('^\s*$', topping):
        print "End of list detected"
        return
    EaterObject.toppingPreference.add(topping)
    PreferredToppingInput(EaterObject)
    

def EaterInput():
    BlankPreferredToppingList = []
    PrerredToppings = []
    name = raw_input("Please enter a name: ")
    if name in EaterSet:
        print "You need to enter a unique name, that one is taken already."
        EaterInput()
    EaterSet.add(name)
    EaterObject = pizzaEater(name)
    ObjectList.append(EaterObject) 
    PreferredToppingInput(EaterObject)

def OrderList():
    for OrdererObject in ObjectList:
        print OrdererObject.name
        for topping in OrdererObject.toppingPreference:
            print topping
        print ""

def OrderCompletor():
    TopSet = set()
    for EaterObject in ObjectList:
        TopSet = TopSet.union(EaterObject.toppingPreference)
    for topping in TopSet:
        print topping
        
    
def main():
    topselector = topinput()
    if topselector == 1:
        EaterInput()
    if topselector == 2:
        OrderList()
    if topselector == 3:
        OrderCompletor()
    main()

if __name__ == "__main__":
        main()
    #eric = pizzaEater("eric")
    #eric.hello()
    #eric.toppingPreference.append("pepperoni")
    #eric.toppingPreference.append("sausage")
    #for topping in eric.toppingPreference:
    #    print topping

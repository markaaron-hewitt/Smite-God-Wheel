# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 02:17:20 2021

@author: MarkyMark
"""

import random
import datetime as dt

class God:

    def __init__(self, Name, Pantheon, Attack_Type, Power_Type, Class, Difficulty, Favor_Cost, Gems_Cost, Release_Date):
        self.Name = Name
        self.Pantheon = Pantheon
        self.Attack_Type = Attack_Type
        self.Power_Type = Power_Type
        self.Class = Class
        self.Difficulty = Difficulty
        self.Favor_Cost = Favor_Cost
        self.Gems_Cost = Gems_Cost
        self.Release_Date = Release_Date
        #self.Image = Image

    '''
    def __init__(self, god):
        self.Name = god[0]
        self.Pantheon = god[1]
        self.Attack_Type = god[2]
        self.Power_Type = god[3]
        self.Class = god[4]
        self.Difficulty = god[5]
        self.Favor_Cost = god[6]
        self.Gems_Cost = god[7]
        self.Release_Date = god[8]
    '''

    def __repr__(self):
        return self.Name

    def __str__(self):
        return self.Name

    def get_Name(self):
        return self.Name

    def get_Pantheon(self):
        return self.Pantheon

    def get_Attack_Type(self):
        return self.Attack_Type
    
    def get_Power_Type(self):
        return self.Power_Type

    def get_Class(self):
        return self.Class

    def get_Difficulty(self):
        return self.Difficulty

    def get_Favor_Cost(self):
        return self.Favor_Cost

    def get_Gems_Cost(self):
        return self.Gems_Cost

    def get_Release_Date(self):
        return self.Release_Date
    
    #def get_Image(self):
    #    return self.Image
    
    def get_traits(self):
        traits = [self.Name,self.Pantheon,self.Attack_Type,self.Power_Type,self.Class,self.Difficulty,self.Favor_Cost,self.Gems_Cost,self.Release_Date]
        return traits

    def display(self):
        print(self.Name, end ="," )
        print(self.Pantheon, end ="," )
        print(self.Attack_Type, end ="," )
        print(self.Power_Type, end ="," )
        print(self.Class, end ="," )
        print(self.Difficulty, end ="," )
        print(self.Favor_Cost, end ="," )
        print(self.Gems_Cost, end ="," )
        print(self.Release_Date)

def godconvert(god):
    return God(god[0],god[1],god[2],god[3],god[4],god[5],god[6],god[7],god[8])

def find_god(name):
    for god in GOD_LIST:
        if god.Name == name:
            god.display()
            return god
    print ('"' + name + '" not found')
    return God(["","","","","","","","",""])

def read_gods():                    #Reads Smite_Gods.txt to import the god list and saves is in a global variable
    global GOD_LIST
    GOD_LIST = []
    f = open('Smite_Gods.txt','r')
    GOD_LIST_TXT = f.readlines()
    for god in GOD_LIST_TXT:
        god = god.strip()
        god = god.split(',')
        if god[6] == "Free":
            god[6] = 0
        else: 
            god[6] = int(god[6])
        if god[7] == "Free":
            god[7] = 0
        else: 
            god[7] = int(god[7])
        god[8] = god[8].split('-')
        god[8] = dt.date(int(god[8][0]),int(god[8][1]),int(god[8][2]))
        g = godconvert(god)
        GOD_LIST.append(g)
    f.close()

def latest_god():
    pass

def display_traits(trait):          #Prints list of all possible values for a trait given list index of trait
    trait_list = []
    for god in GOD_LIST:
        x = god.get_traits()[trait]
        trait_list.append(x)
    trait_list = set(trait_list)
    trait_list = list(trait_list)
    trait_list.sort()
    print(*trait_list, sep = ', ')

def traits():
    trait_types = ['Name', 'Pantheon', 'Attack Type', 'Power Type', 'Class', 'Difficulty', 'Favor Cost', 'Gems Cost', 'Release Date']
    trait_number = len(trait_types)
    for i in range(0,trait_number):
        print(str(i) + ': ' + trait_types[i])

def random_gods(n):                 #Returns a list containing n distinct random gods
    god_pool = GOD_LIST.copy()
    results = []
    for i in range(0,n):
        x = random.choice(god_pool)
        results.append(x)
        god_pool.remove(x)
    return results

def random_gods_specialised(n,god_pool):
    results = []
    for i in range(0,n):
        x = random.choice(god_pool)
        results.append(x)
        god_pool.remove(x)
    print(results)
    return results

def display_cheap_gods():
    cheap_gods = []
    for god in GOD_LIST:
        if ((god.get_Favor_Cost() < 5500) & (god.get_Favor_Cost() != 0)):
            cheap_gods.append(god)
    for god in cheap_gods:
        print(god, end = ': ')
        print(god.get_Favor_Cost())
    return cheap_gods

def god_wheel():                    #Returns 1 random god
    return random_gods(1)[0]

def main():
    global GOD_LIST
    read_gods()

if __name__ == "__main__":
    main()


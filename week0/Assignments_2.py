import string
class PasswordValidator:
    ## when putting nothing for contains_capital or contains_number, it switch off.
    ## so they have to be False
    def __init__(self, contains_capital=False,contains_number=False,symbols=[]):
        self.symbols = symbols
        self.contains_capital = contains_capital
        self.contains_number = contains_number
        
    def validate(self, strings):

        symbo_check =  len(set(self.symbols) - set(list(strings))) != len(self.symbols)
        
        if self.contains_capital == True:
            capit_check =  len(set(list(string.ascii_uppercase)) -  set(list(strings))) != len(list(string.ascii_uppercase))
        else:
            capit_check = True 
            ## when self.contains_capital == False, assuming it was true so that "&" in return works
        
        if self.contains_number == True:
            num = ["0","1","2","3","4","5","6","7","8","9"]
            num_check = len(set(num) - set(list(strings))) != len(num)
        else:
            num_check = True
        
        return (symbo_check&capit_check&num_check)

validator = PasswordValidator(symbols=['!', '?', '#'])
print(validator.validate('moshi?'))

import numpy as np
class VectorSegmenter:
    def __init__(self, a_list):
        self.a_list = a_list
    def segment(self,bool_list):
        self.new_list = [self.a_list[i] for i in range(len(self.a_list)) if bool_list[i] == True]
        return self.new_list
    def sum(self,bool_list):
        return sum(self.new_list,bool_list)
    def average(self,bool_list):
        return np.mean(self.new_list)

v = VectorSegmenter([1, 2, 3, 4, 5, 6])
print(v.segment([True, True, False, False, True, True]))
print(v.average([True, True, False, False, True, True]))


import numpy as np
class DungeonRoom:
    def __init__(self,i,j):
        self.i = i
        self.j = j
        self.b_room =[]
                
        ## create a i x j array
        self.room = np.full((self.i,self.j),".")

        
        ## creat a copy, so one for printing and the other for get overlap/union of boolean
        self.room_ori = np.copy(self.room) 
    def add_rectangle(self,a,b,c,d):      
        ## add wall
        self.room[a:c,b] = "#"
        self.room[a:c,d-1] = "#"
        self.room[a,b:d] = "#"
        self.room[c-1,b:d] = "#"
                
        ## select overlap
        room_bool = np.full((self.i, self.j), False) # creat a i x j array with full of False
        
        for i in range(a,c):
            room_bool[i,b:d] = True # set True for inside rectangular 
        
        self.b_room.append(room_bool) # self.b_room contain 1st and 2nd boolean array
        
        ## when there are more than one rectangular
        if len(self.b_room) > 1:
            b_room_int = np.all(self.b_room, axis=0) # overlap area
            self.room[b_room_int] = "." # overlap area have to be "."
            
            self.b_room = [np.any(self.b_room, axis=0)] # replace the rectangular area with union 
                                                        # so always two boolean array in self.b_room
    def print_room(self):
        print("\n".join(["".join(a) for a in self.room]))

room = DungeonRoom(10, 10)
room.add_rectangle(1, 2, 5, 6)
room.add_rectangle(4, 4, 8, 9)
room.add_rectangle(6, 2, 9, 7)

room.print_room()



class Quadratic_Polynomial:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
    def evaluate(self,x):
        return self.a * (x**2) + self.b*x + self.c
    
    def __add__(self,other):
        a = self.a + other.a
        b = self.b + other.b
        c = self.c + other.c
        return Quadratic_Polynomial(a,b,c)
    
    def __sub__(self,other):
        a = self.a - other.a
        b = self.b - other.b
        c = self.c - other.c
        return Quadratic_Polynomial(a,b,c)
    
    def __eq__(self,other):
        return self.a == other.a and self.b == other.b and self.c == self.c
    
    def __repr__(self):
        return "%dx^2 + %dx + %d"%(self.a,self.b,self.c)
    
    def __str__(self):
        ## set arguments in equation in list
        string = [["",str(self.a),"x^2"],["+ ",str(self.b),"x"],["+ ",str(self.c),""]]
        string2 = []
        
        ## only put sections with a/b/c != 0 into string2
        for i in range(len(string)):
            if float(string[i][1]) != 0:
                string2.append(string[i])
        
        ## adjust +/-
        for i in range(len(string2)):
            if float(string[i][1]) < 0:
                string2[i][0] = "- " # when a/b/c < 0 , set symbol as "- "
                string2[i][1] = string2[i][1][1:] # when a/b/c < 0, set a/b/c as abstract
            if string[i][1] == "1" and i < len(string2)-1:
                string[i][1] = "" # if a/b/c = 1, don't display it, excluding last section.

        if string2[0][0] == "- ":
            string2[0][0] = "" # when first section a/b/c < 0, rm symbol
            string2[0][1] = "-" + string2[0][1] # when first section a/b/c < 0, make a/b/c negative

    
        return " ".join(["".join(a) for a in string2])



test1 = Quadratic_Polynomial(1,-2,-3)
test1.evaluate(2)
#test2 = Quadratic_Polynomial(1,2,3)
#test3 = test1 - test2
print(test1)


import bs4          # The most important library for us, see the note below
import requests     # Requests will allow us to access the website via HTTP requests
import pandas as pd # A standard tabular data manipulation library

def get_webpage(url):
    response = requests.get(url)  #  Get the url
    return bs4.BeautifulSoup(response.text, 'html.parser') #  Turn the url response into a BeautifulSoup object

COLUMNS = ['cy-pair', 'rate']

def scrape(webpage):
    table = webpage.find("table") # Find the "table" tag in the page
    rows = table.find_all("tr")  # Find all the "tr" tags in the table
    cy_data = [] 
    for row in rows:
        cells = row.find_all("td") #  Find all the "td" tags in each row 
        cells = cells[1:3] # Select the correct columns (1 & 2 as python is 0-indexed)
        cy_data.append([cell.text for cell in cells]) # For each "td" tag, get the text inside it
    return pd.DataFrame(cy_data, columns=COLUMNS).drop(0, axis=0)


class Currency:
    def __init__(self, amount, unit):
        URL = 'https://uk.finance.yahoo.com/currencies'
        page = get_webpage(URL)
        data = scrape(page)
        self.currency_dict = dict(zip(data["cy-pair"],data["rate"]))
        self.currency_dict = {key:float(values) for key, values in self.currency_dict.items()}
        self.currency_dict.update({(key.split("/")[1]+"/"+key.split("/")[0]):(1/values) for key, values in self.currency_dict.items()})

        self.amount = amount
        self.unit = unit
        
    def __repr__(self):
        return str(self.amount) + " "+ self.unit
    
    def convert(self, to_unit):
        if to_unit != self.unit: # if same unit, self.converted_amount = self.amount
            key = to_unit+"/"+self.unit
            self.converted_amount = round(self.currency_dict[key] * self.amount,2)
        else:
            self.converted_amount = self.amount
        print( str(self.converted_amount) + " "+ to_unit )
        
    def __add__(self,other):
        if other.unit != self.unit:
            other_key = self.unit +"/"+ other.unit
            other_converted = round(self.currency_dict[other_key]*other.amount)
        else: # if same unit, other_converted = other.amount
            other_converted = other.amount
        
        return Currency(self.amount + other_converted,self.unit)

v1 = Currency(23.43, "EUR")
#v1.convert("USD")
v2 = Currency(19.97, "USD")
v2.convert("EUR")
print(v1+v2)
'''
Given a file with the following format:

    City name;time;date;temperature
    Geneva;12:34;2003/12/23;2.34;
    Lausanne;12:36;2003/12/23;3.34;
    Bern;12:36;2003/12/23;-3.34;
    ....

Write a python script to parse this file and store it's content into a "custom
object".
You could define a class "Record" that will represent a line of this file and
a class "ListOfRecord" to represent a list of "Record".
This class "ListOfRecord" should offer a way to construct an instance of it
with the help of a text file like the one above.
It should also offers ways to save/restore the list easily.
And a method to compute the average of the temperature recorded for a given city name.
'''

import pickle

class Record:
    def __init__(self, name, time, date, temperature):
        self.city=name # Creation and initialisation of the attribute "city"
        self.time=time
        self.date=date
        self.__temperature=temperature
    
    def __str__(self):
        return f"In {self.city} at {self.date} {self.time} temp is {self.temperature}"
    
    def __repr__(self):
        return f"{self.city} at {self.date} {self.time}: {self.temperature}"
    
    # Note: classmethod is equivalent to staticmethod the only difference is that a
    # classmethod get an implicit argument: the class
    
    @classmethod
    def parse(cls, text):
        c,t,d,temp=text.split(";")
        return Record(c, t, d, float(temp))
    
    def temperatureGet(self):
        return self.__temperature 
       
    def temperatureSet(self, val):
        if not isinstance(val, float):
            raise Exception("Wrong kind of temperature")
        self.__temperature=val
    
    temperature=property(fget=temperatureGet, fset=temperatureSet) 
    
    # NOTE: city, time and date could (and should) also be defined as properties ...       
           
class ListOfRecord:
        
    def __init__(self):
        self.data=[] 
        
    def __str__(self):
        return str(self.data)
       
    def addRecord(self, record):
        self.data.append(record)
        
    @staticmethod
    def parseFile(fname):
        lr=ListOfRecord()
        with open(fname,"r") as fic:
            fic.readline()
            for line in fic:
                lr.addRecord(Record.parse(line))
        return lr  
          
    #parseFile=staticmethod(parseFile) 
       
    @staticmethod
    def readFromFile(fname):
        with open(fname,"rb") as fic:
            return pickle.load(fic)
        
    #readFromFile=staticmethod(readFromFile)
    
    def __iter__(self): # to make ListOfRecord be an "iterable" object
        return self.data.__iter__()
    
    def saveIntoFile(self, fname):
        with open(fname,"wb") as fic:
            pickle.dump(self, fic) 
            
    def __contains__(self, city): # in
        for r in self:
            if r.city == city:
                return True
        return False 
            
    def averageTemp(self, cityName):
        if not cityName in self:
            raise Exception (f"{cityName} is not in the list")
        total=0
        ix=0
        for r in self:
            if r.city==cityName:
                ix += 1
                total += r.temperature 
        return total/ix   
    
if __name__ == "__main__":
      
    lofr=ListOfRecord.parseFile("measures.txt")
    print(lofr)
    
    for r in lofr:
        print(r)
        
    lofr.saveIntoFile("data.out")
    
    newlist=ListOfRecord.readFromFile("data.out")
    print(newlist)
    print("Newlist type: ", type(newlist))
    
    city="Geneva"
    result=lofr.averageTemp(city)
    print(result)
    city="Lausanne"
    result=lofr.averageTemp(city)
    print(result)
    city="Bern"
    result=lofr.averageTemp(city)
    print(result)
    city="Neuchatel"
    if city in lofr:
        result=lofr.averageTemp(city)
    else:
        print(f"{city} not in the list of record")
    print(result)
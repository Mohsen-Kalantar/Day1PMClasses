import pickle

class Record:
    def __init__(self, name, time, date, temperature):
        self.city=name # Creation and initialisation of the attribute "city"
        self.time=time
        self.date=date
        self.temperature=temperature
    
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
    
class ListOfRecord(list):
       
    def addRecord(self, record):
        self.append(record)
        
    def addRecords(self, *records):
        for r in records:
            self.append(r)   
             
    @staticmethod
    def parseFile(fname):
        lr=ListOfRecord()
        with open(fname,"r") as fic:
            fic.readline()
            for line in fic:
                lr.addRecord(Record.parse(line))
        return lr  
      
    @staticmethod
    def readFromFile(fname):
        with open(fname,"rb") as fic:
            return pickle.load(fic)

    def saveIntoFile(self, fname):
        with open(fname,"wb") as fic:
            pickle.dump(self, fic) 
            
    def __contains__(self, city): # in operator
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
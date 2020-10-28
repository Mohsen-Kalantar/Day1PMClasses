"""
MyList extends the class list (it "inherits" from list).
We can say that MyList is a sub-class or a child-class of list.
We can say that list is the super-class or the mother-class of MyList.

A MyList object "is a" list with a lot of shared features (append(), insert(), remove(), ...)
and some new  ones: 
    a new method save() 
    a new definition of the + operator

"""
class MyList(list):
    def __add__(self, other):
        return MyList(map(lambda a,b:a+b, self, other))
    def save(self, filename):
        import pickle
        with open(filename, "wb") as f:
            pickle.dump(self,f)
            
l1=MyList([2,3,4,8,77])
l2=MyList([3,4,5,1])
l3=l1 + l2
print(l3)
l3.save("myl.out")

# l.append(12)
# l.insert(0,34)
# print(l)

# l1=[2,3,4]
# l2=[3,4,5]
# l3=l1 + l2
# print(l3) # [5,7,9]

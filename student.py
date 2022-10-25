from unicodedata import name


class Student:
    #Class Variable
    school_name = 'ABC School'
    #Instance method..self refers to the current object
    def __init__(self,name,age):
        self.name = name
        self.age = age
    # instance method has access to instance variables and class variable.
    def show(self):
        print(self.name,'is in school named',Student.school_name,'and age is',self.age)

    @classmethod
    def change_school(cls,name):
        cls.school_name = name   
        
    @staticmethod
    def find_notes(subject_name):
        return['ch1','ch2','ch3']

s = Student('Aydin',6)
s.show()

Student.change_school("Rush Creek Elementary")
s.show()

s.change_school('XYZ')
s.show()

z = s.find_notes('math')
print(z)

y = Student.find_notes('math')
print(y)




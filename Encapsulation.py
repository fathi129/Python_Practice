class Employee:
    def __init__(self,name,project):
        self.name = name
        self.project = project
    def show(self):
        print(self.name,'is in project named',self.project)
    def get(self,age):
        self.age = age
        print(self.name,'is',self.age,'years old and working in project',self.project)

emp = Employee('Nasreen','CyberSecurity')
emp.show()
emp.get(10)
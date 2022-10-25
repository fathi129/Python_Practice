class Company:
    def info(self):
        return 'Google'
class Employee(Company):
    def comp_info(self,name):
        self.name = name
        c_info = super().info()
        print(self.name,"works at ",c_info)  

emp = Employee()
emp.comp_info("Jessie")              
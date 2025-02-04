# Your task is to design an Employee Management System using Object-Oriented Programming (OOP) principles such as abstraction, inheritance, and polymorphism in Python.

# Instructions:
# Create an Interface Employee (Abstract Base Class)

# Define an abstract class Employee using the ABC module.
# Include two abstract methods:
# work(self) -> str: Defines the work responsibilities of the employee.
# get_salary(self) -> float: Returns the salary of the employee.
# Implement Concrete Employee Classes
  
# Create two classes, Manager and Developer, that inherit from Employee.
# Each class should implement the work method to describe the employee’s role.
# Implement the get_salary method to return the salary of the employee.
# Create a Department Class to Manage Employees

# The Department class should store a list of employees.
# Implement methods:
# hire(self, employee: Employee): Adds an employee to the department.
# fire(self, employee: Employee): Removes an employee from the department.
# get_total_salary(self) -> float: Returns the total salary of all employees.
# show_employee_details(self): Displays all employees, their salary, and work description.
# Test the Implementation

# Create instances of Manager and Developer with names and salaries.
# Add them to a Department and display their details.
# Calculate and print the total salary expense.


from abc import ABC,abstractmethod

# class Employee_interface():
    

class Abstract_employee(ABC):
    @abstractmethod
    def get_work():
        pass

    abstractmethod
    def get_salary():
        pass

class Manager(Abstract_employee):
    def __init__(self,name,salary,work):
        self.name=name
        self.salary=salary
        self.work=work
    def add_emp(self,new_emp,department_list):
        department_list.append(new_emp)
    def get_work(self,employeeList,employee1):
        for i in employeeList:
            if i.name==employee1:
                print(f"work details of {i.name} are {i.work}")
        
    def get_salary(self,employeeList,salary1):
         for i in employeeList:
            if i.name==salary1 :
                print(f"work details of {i.name} are {i.salary}")

        

class Developer(Abstract_employee):
    def get_work(self,employeeList,employee1):
        for i in employeeList:
            if i.name==employee1:
                print(f"work details of {i.name} are {i.work}")
        
    def get_salary(self,employeeList,salary1):
         for i in employeeList:
            if i.name==salary1:
                print(f"work details of {i.name} are {i.salary}")

class Department:
    
        
    
    def hire_emp(self,new_emp,department_list):
        department_list.append(new_emp)
    def fire_emp(self,department_list,remove_emp):
        department_list.remove(remove_emp)
    def get_emp_details(self,department_list):
        for i in department_list:
            print(i.name,i.salary,i.work)
    def total_salary(self,department_list):
        sum=0
        for i in department_list:
            sum+=i.salary
        print(sum)
        

department_list=[]

Manager1=Manager("rajesh",100000,"manager")
Manager2=Manager("sai",100000,"manager")
Manager3=Manager("indra",100000,"manager")
Manager4=Manager("mani",100000,"manager")
Manager5=Manager("akhil",100000,"manager")


dep=Department()


Manager1.add_emp(Manager1,department_list)
Manager1.add_emp(Manager2,department_list)
Manager1.add_emp(Manager3,department_list)
Manager1.add_emp(Manager4,department_list)
Manager1.get_work(department_list,"rajesh")
Manager5.get_work(department_list,"sai")
dep.total_salary(department_list)
dep.get_emp_details(department_list)
dep.fire_emp(department_list,"rajesh")
dep.get_emp_details(department_list)

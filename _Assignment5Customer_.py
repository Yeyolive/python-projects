import random

class Person:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_name(self):
        return self.get_first_name() + " " + self.get_last_name()


class Customer(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.__customer_id = ""
        self.__customer_email = ""

    def get_customer_id(self):
        return self.__customer_id

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def get_customer_email(self):
        return self.__customer_email

    def set_customer_email(self, email):
        self.__customer_email = email

    def get_customer_info(self):
        return self.get_name() + ", " + self.get_customer_email()


class Employee(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.emp_id = ""
        self.emp_salary = ()
    def set_emp_id(self):
        self.emp_id = random.randint(0, 726819)
    def get_emp_id(self):
        return self.emp_id
    def set_emp_salary(self):
        try:
            if self.emp_salary < 20000:
                raise ValueError ("ERROR! Salary is less than 20000")
        except: 
            print("ERROR! Salary should be 20000")
    def get_emp_salary(self):
        return self.emp_salary


from Assignment5Customer import Employee

emp1 = Employee(' Jake', 'Johnson')
emp1.set_emp_id()
emp1.emp_salary = int(input("Please enter your pay"))
emp1.set_emp_salary()
if emp1.emp_salary <= 20000:
    raise ValueError ("ERROR! Salary is less than 20000")
else:
    print("Employee details:")
    print("Jake Johnson's Employee ID number:", emp1.get_emp_id())
    print("Jake Johnson's salary:", emp1.get_emp_salary())

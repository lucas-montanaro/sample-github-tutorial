class Salary:
    def __int__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return(self.pay*12)*self.bonus

class Employee:
    def __int__(self, name, sal):
        self.name = name

        self.agg_salary = sal

    def total_sal(self):
        return self.agg_salary.annual_salary()

name = input("Enter Employee Name: ")
mthpay = float(input("Enter Employee Monthly Salary: "))
bonus = float(input("Enter Employee Annual Bonus: "))

salary = Salary(mthpay, bonus)

emp = Employee(name, salary)

print(f"{emp.name}'s annual salary is ${emp.total_sal():,.2f}")

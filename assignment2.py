class Employee:
    def __init__(self, name, base_salary, experience):
        self.name = name
        self.base_salary = base_salary
        self.experience = experience

    def calculate_salary(self, monthly_hours):
        total_hours = monthly_hours * 12
        monthly_salary = self.base_salary / 12

        if self.experience < 8:
            total_salary = monthly_salary * total_hours
        else:
            total_salary = monthly_salary * total_hours + 5000

        tax_deduction = total_salary * 0.13
        net_salary = total_salary - tax_deduction

        return net_salary

    def display_employee_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Base Salary: {self.base_salary}")
        print(f"Experience: {self.experience} years")


name = input("Enter employee name: ")
base_salary = float(input("Enter base salary: "))
experience = int(input("Enter experience in years: "))
monthly_hours = float(input("Enter monthly working hours: "))

employee = Employee(name, base_salary, experience)
salary = employee.calculate_salary(monthly_hours)

employee.display_employee_details()
print(f"Salary: {salary:.2f}")

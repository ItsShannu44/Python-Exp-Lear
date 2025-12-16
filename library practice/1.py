class SalaryNotInRange(Exception):
    def __init__ (self,salary,msg="salary not in range"):
        self.salary=salary
        self.msg=msg
        super().__init__(self.msg)

salary=int(input("Enter the sal:"))
if not 5000<salary<15000:
    raise SalaryNotInRange(salary)
else:
    print(f"Salary is: {salary}")
#multi level class methods using two are more class mixing

class working: #parrent class or base class or super class
    emp = 12
    salary =10000
    salary_amount= 0
    def wfh(self):
        salary_amount = self.emp * self.salary
        print("working employees salary amount : ", salary_amount)
        return salary_amount

class teacher(working): # children one
    days = 31
    sundays = 4

    def msg(self):

        print("School working days ", self.days - self.sundays)


class student(teacher):  # children two
    cls = 8
    strength = 40
    def fee(self):
        total = self.cls * self.strength
        self.fee_amount = total * 2000.00
        print("total fee collection amount : ", self.fee_amount)

    def income(self):
        total_income =  self.fee_amount - self.salary_amount
        print("School income per year :",total_income )


    def attendence():
        wd = 365
        hd = 51
        sd = 20
        twd = wd - (hd + sd)
        print(" School Working days : ",twd)

#  calling is most important
print("working employees :",teacher.emp)
a=working()
a.wfh()
print("School working days",student.attendence())
print("students collection fee",student.fee(student))
print("school employee salary",student.salary)
print("School Staff",student.emp)
student.attendence()
teacher.msg(teacher)
student.fee(student)
student.income(student)


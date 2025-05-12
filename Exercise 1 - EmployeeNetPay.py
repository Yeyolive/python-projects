
def get_hours_worked():
    hours = float(input("Enter the number of hours worked: "))
    return hours 

def get_hourly_rate():
    rate = float(input("Enter the employee hourly pay rate: "))
    return rate

def get_input():
    hours = get_hours_worked() 
    rate = get_hourly_rate() 
    return hours, rate 

def calc_overtime(hoursWorked, regularRate):
    overtimeRate = regularRate * 1.5 
    overtimePay = (hoursWorked - 40) * overtimeRate
    return overtimePay 

def calc_gross_pay(hoursWorked, regularRate, overtimePay):
    if hoursWorked > 40:
        
        regularPay = 40 * regularRate
        gross = regularPay + overtimePay
    else:
        
        gross = hoursWorked * regularRate
    
    return gross

def calc_taxes(grossPay):
    return 0.10*grossPay

def calc_benefits(grossPay):
    return 0.06*grossPay

def calc_withholdings(grossPay):
    tax = calc_taxes(grossPay) 
    benefits = calc_benefits(grossPay) 
    withholdings = tax + benefits 
    return withholdings

def calc_net_pay(grossPay,withholdings):
    netPay = grossPay - withholdings
    return netPay

hoursWorked, regularRate = get_input()
if hoursWorked > 40:

    overtimePay = calc_overtime(hoursWorked, regularRate)
else:
    overtimePay = 0

grossPay = calc_gross_pay(hoursWorked, regularRate, overtimePay)
withholdings = calc_withholdings(grossPay)
netPay = calc_net_pay(grossPay,withholdings)

print('Net Pay =', netPay)

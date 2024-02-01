def getDatesWorked():
    fromDate = input("Please enter start date in the following format MM/DD/YYYY: ")
    endDate = input("Please enter end date in the following format MM/DD?YYY: ")
    return fromDate, endDate
#this function means xyz
def getEmpName():
    empName = input("Enter employee name: ")
    return empName

def getHoursWorked():
    hours = float(input("Enter hours worked: "))
    return hours

def getHourlyRate():
    hourlyRate = float(input("Enter hourly rate: "))
    return hourlyRate

def getTaxRate():
    taxRate = float(input("Enter tax rate: "))
    taxRate = taxRate / 100
    return taxRate

def CalcTaxAndNetPay(hours, hourlyRate, taxRate):
    gPay = hours * hourlyRate
    incomeTax = gPay * taxRate
    netPay = gPay - incomeTax
    return gPay, incomeTax, netPay

def printInfo(empName, hours, hourlyRate, gPay, taxRate, incomeTax, netPay):
    print(empName, f"{hours:,.2f}", f"{hourlyRate:,.2f}", f"{gPay:,.2f}", f"{taxRate:,.1%}", f"{incomeTax:,.2f}", f"{netPay:,.2f}")
        
def PrintTotals(totalEmployees, totalHours, totalGrossPay, totalTax, totalNetPay):
    print(f"\nTotal number of employees: {totalEmployees}")
    print(f"Total hours worked: {totalHours:,.2f}")
    print(f"Total gross pay: {totalGrossPay:,.2f}")
    print(f"Total tax: {totalTax:,.2f}")
    print(f"Total Net pay: {totalNetPay:,.2f}")
    
if __name__ == "__main__":
    totalEmployees = 0
    totalHours = 0.00
    totalGrossPay = 0.00
    totalTax = 0.00
    TotalNetPay = 0.00
    
while True:
    empName = getEmpName()
    if (empName.upper() == "END"):
        break
    hours = getHoursWorked()
    hourlyRate = getHourlyRate()
    taxRate = getTaxRate()
    gPay, incomeTax, netPay = CalcTaxAndNetPay(hours, hourlyRate, taxRate)
    
    printinfo(empName, hours, hourlyRate, gPay, taxRate, incomeTax, netPay)
    
    totalEmployees += 1
    totalHours += hours
    totalGrossPay += gPay
    totalTax += incomeTax
    totalNetPay += netPay
    
PrintTotals(totalEmployees, totalHours, totalGrossPay, totalTax, totalNetPay)

    
    

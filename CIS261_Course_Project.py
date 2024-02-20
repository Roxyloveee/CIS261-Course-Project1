def getDatesWorked():
    fromDate = input("Please enter start date in the following format MM/DD/YYYY: ")
    endDate = input("Please enter end date in the following format MM/DD/YYYY: ")
    return fromDate, endDate
#this function means xyz
def getEmpName():
    empName = input("Enter employee name: ")
    return empName
def getHoursWorked():
    hours = float(input("Enter Hours: "))
    return hours
def getHourlyRate():
    hourlyRate = float(input("Enter Hourly Rate: "))
    return hourlyRate
def getTaxRate():
    taxRate = float(input("Enter Tax Rate: "))
    taxRate = taxRate / 100
    return taxRate
def CalcTaxAndNetPay(hours, hourlyRate, taxRate):
    gPay = hours * hourlyRate
    incomeTax = gPay * taxRate
    netPay = gPay - incomeTax
    return gPay, incomeTax, netPay
def printInfo(empDetailList):
    totalEmployees = 0
    totalHours = 0.00
    totalGrossPay = 0.00
    totalTax = 0.00
    totalNetPay = 0.00
    for empList in empDetailList:
        fromDate = empList[0]
        endDate = empList[1]
        empName = empList[2]
        hours = empList[3]
        hourlyRate = empList[4]
        taxRate = empList[5]
        
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyRate, taxRate)
        print(fromDate, endDate, empName, f"{hours:,.2f}", f"{hourlyRate:,.2f}", f"{grosspay:,.2f}", f"{taxRate:,.1%}", f"{incometax:,.2f}", f"{netpay:,.2f}")
        totalEmployees += 1
        totalHours += hours
        totalGrossPay += grosspay
        totalTax += incometax
        totalNetPay += netpay

        empTotals["totEmp"] = totalEmployees
        empTotals["totHours"] = totalHours
        empTotals["totGross"] = totalGrossPay
        empTotals["totTax"] = totalTax
        empTotals["totNet"] = totalNetPay
        
def printTotals(empTotals):
    print(f'Total Number Of Employees: {empTotals["totEmp"]}')
    print(f'Total Hours Of Employees: {empTotals["totHours"]}')
    print(f'Total Gross Pay Of Employees: {empTotals["totGross"]}')
    print(f'Total Tax Of Employees: {empTotals["totTax"]}')
    print(f'Total Net Pay Of Employees: {empTotals["totNet"]}')
    
def writeEmployeeInfo(employee):
    file = open("employeeinfo.txt", "a")
    file.write('{}|{}|{}|{}|{}|{}\n'.format(employee[0], employee[1], employee[2], employee[3], employee[4], employee[5]))
    
def getFromDate():
    valid = False
    fromDate = ''
    while not valid:
        fromDate = input("Enter a from date (mm/dd/yyyy): ")
        if (len(fromDate.split('/')) != 3 and fromDate.upper() != 'ALL'):
            print("Invalid date format! ")
        else:
            valid = True
    return fromDate

def readEmployeeInfo(fromDate):
    empDetailList = []
    file = open("employeeinfo.txt", "r")
    data = file.readlines()
    condition = True
    if fromDate.upper() == 'ALL':
        condition = False
    for employee in data:
        employee = [x.strip() for x in employee.strip().split("|")]
        if not condition:
            empDetailList.append([employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5])])
        else:
            if fromDate == employee[0]:
                empDetailList.append([employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5])])
    return empDetailList
          

if __name__ == "__main__":
    empDetailList = []
    empTotals = {}
    while True:
        empName = getEmpName()
        if (empName.upper() == "END"):
            break
        fromDate, endDate = getDatesWorked()
        hours = getHoursWorked()
        hourlyRate = getHourlyRate()
        taxRate = getTaxRate()
        print()
       
        empDetail = [fromDate, endDate, empName, hours, hourlyRate, taxRate]
        writeEmployeeInfo(empDetail)
        
    print()       
    fromDate= getFromDate()
    empDetailList = readEmployeeInfo(fromDate)
    printInfo(empDetailList)
    printTotals(empTotals)    
        
    empDetail = []
    empDetail.insert(0, fromDate)
    empDetail.insert(1, endDate)
    empDetail.insert(2, empName)
    empDetail.insert(3, hours)
    empDetail.insert(4, hourlyRate)
    empDetail.insert(5, taxRate)
    empDetailList.append(empDetail)
    

from datetime import datetime
def createUsers():
    print('  Create users, passwords, and roles     ')
    userFile = open("Users.txt", "a+")
    while True:
        username = getUserName()
        if (username.upper() == "END"):
            break
        userpwd = getUserPassword()
        userrole = getUserRole()

        userDetail = username + "|" + userpwd + "|" + userrole + "\n"
        userFile.write(userDetail)

    userFile.close()
    printuserinfo()
def getUserName():
    username = input("Enter user name or 'End' to quit: ")
    return username
def getUserPassword():
    pwd = input("Enter password: ")
    return pwd
def getUserRole():
    userrole = input("Enter role (Admin or User): ")
    while True:
        if (userrole.upper() == "ADMIN" or userrole.upper() == "USER"):
            return userrole
        else:
            userrole = input("Enter role (Admin or User): ")
def printuserinfo():
    userFile = open("Users.txt", "r")
    while True:
        userDetail = userFile.readline()
        if not userDetail:
            break
        userDetail = userDetail.replace("\n", "")
        userList = userDetail.split("|")
        userName = userList[0]
        userPassword = userList[1]
        userRole = userList[2]
        print("User Name: ", userName, " Password: ", userPassword, "Role: ", userRole)

def Login():
    userFile = open("Users.txt", "r")
    userList = []
    userName = input("Enter User Name: ")
    userPwd = input("Enter Password: ")
    userRole = "None"
    while True:
        userDetail = userFile.readline()
        if not userDetail:
            return userRole, userName, userPwd
        userDetail = userDetail.replace("\n", "")

        userList = userDetail.split("|")
        if userName == userList[0] and userPwd == userList[1]:
            userRole = userList[2] # user is valid, return role
            return userRole, userName
    return userRole, userName

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
if __name__ == "__main__":

    empDetailList = []
    empTotals = {}
    while True:
        empName = getEmpName()
        if (empName.lower() == "end"):
            break
        fromDate, endDate = getDatesWorked()
        hours = getHoursWorked()
        hourlyRate = getHourlyRate()
        taxRate = getTaxRate()
        empDetail = []
        empDetail.insert(0, fromDate)
        empDetail.insert(1, endDate)
        empDetail.insert(2, empName)
        empDetail.insert(3, hours)
        empDetail.insert(4, hourlyRate)
        empDetail.insert(5, taxRate)
        empDetailList.append(empDetail)
    printInfo(empDetailList)
    printTotals(empTotals)


    createUsers()
    print()
    print("##### Data Entry #####")
    userRole, userName = Login()
    detailsPrinted = False
    empTotals = {}
    if (userRole.upper() == "NONE"):
        print(userName, " is invalid.")
    else:
        if (userRole.upper() == "ADMIN"):

            empFile = open("Employees.txt", "a+")
            while True:
                empName = getEmpName()
                if (empName.upper() == "END"):
                    break
                fromdate, enddate = getDatesWorked()
                hours = getHoursWorked()
                hourlyrate = getHourlyRate()
                taxrate = getTaxRate()
                empDetail = fromDate + "|" + endDate + "|" + empName + "|" + str(hours) + "|" + str(hourlyRate) + "|" + str(taxRate) + "\n"
                empFile.write(empDetail)
            empFile.close()
        printInfo(detailsPrinted)
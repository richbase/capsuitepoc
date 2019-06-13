import pandas as pd


def readFnbSchedule():
    salary = int(input("enter salary: "))
    #maritalStatus = input("enter marital status: ")
    currentSalary = int(input("enter the current salary: "))
    netWilling = int(input("enter net willing "))
    currentInstallment = int(input("enter current installment"))

    #calculate monthly installment
    qualifiedLoanAmount = (currentSalary + currentInstallment)-netWilling

    print(qualifiedLoanAmount)

    schedule = pd.read_csv("private_24_months_custom.csv")

    matchValues = schedule[schedule.MonthlyLoanInstalment <= qualifiedLoanAmount]
    print(matchValues)

readFnbSchedule()

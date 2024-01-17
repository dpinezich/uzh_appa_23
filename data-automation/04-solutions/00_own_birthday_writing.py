import csv

with open('00_own_birthday_writing.csv', mode='a') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
    employee_writer.writerow(['Robin Robbers', 'Marketing', 'March'])
    employee_writer.writerow(['Sam Salmon', 'IT', 'March'])
    employee_writer.writerow(['Robert Rost', 'Accounting', 'April'])
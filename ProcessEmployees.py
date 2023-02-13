"""
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
"""

import csv

# open the file

infile = open("employee_data.csv", "r")

line = csv.reader(infile, delimiter=",")

next(infile)


# create an empty dictionary

emp_info = {}
# use a loop to iterate through the csv file

for record in line:
    if record[3] == "Marketing":
        if record[4] == "CSR":
            # check if the employee fits the search criteria
            name = record[1] + " " + record[2]
            salary = record[5]
            new_salary = float(record[5]) * 1.10
            emp_info = {"name": name, "new salary": new_salary}
            print(
                "Manager Name: "
                + str(emp_info["name"])
                + "  "
                + "Current Salary: "
                + salary
            )


print()
print("=========================================")
print()

# iternate through the dictionary and print out the key and value as per printout
for employee in emp_info:
    print(
        "Manager Name: "
        + str(emp_info["name"])
        + "  "
        + "New Salary: "
        + str(emp_info["new salary"])
    )

import csv

# Reading from a CSV
with open("data.csv", newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Writing to a CSV
with open("output.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Location"])
    writer.writerow(["Ali", 25, "London"])
    writer.writerow(["Josh", 23, "Birmingham"])

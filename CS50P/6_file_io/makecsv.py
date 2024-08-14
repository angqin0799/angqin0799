import csv

name = input("Name: ")
home = input("Home: ")

# with open("make.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])


with open("make.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames = ["name" , "home"])
    writer.writerow({"name":name, "home":home})

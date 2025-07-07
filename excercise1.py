####################################################

colors = [
{
"colors": "red",
"values": "#f00"
},
{
"colors": "green",
"values": "#0f0"
},
{
"colors": "blue",
"values": "#00f"
},
{
"colors": "cyan",
"values": "#0ff"
},
{
"colors": "magenta",
"values": "#f0f"
},
{
"colors": "yellow",
"values": "#ff0"
},
{
"colors": "black",
"values": "#000"
}
]




# write a program to display all the colors and its values.

# sample output :

# red #f00
# green #0f0
# yellow  #ff0
# magenta #f0f
# ..
# ..
# ..
# Solution
for var in colors:
    print(var['colors'], end=" ")
    print(var['values'])

###############################################################################################################################


# Write a program to display all employee names and their departments.

employees = {
    "E001": {"name": "Alice", "department": "Finance"},
    "E002": {"name": "Bob", "department": "IT"},
    "E003": {"name": "Charlie", "department": "HR"}
}


# sample output:

# Alice  Finance
# Bob    IT


for item in employees.values():
    print(item['name'], " ",  item['department'])

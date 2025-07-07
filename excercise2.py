###############################################################################################################################

# Write a program to print team names and player names.

teams = {
    "TeamA": [
        {"name": "Alice", "role": "Batsman"},
        {"name": "Bob", "role": "Bowler"}
    ],
    "TeamB": [
        {"name": "Charlie", "role": "Allrounder"},
        {"name": "Dave", "role": "Wicketkeeper"}
    ]
}


for item in teams.keys():
    print(item)
    print("----")
    for var in teams[item]:
        print(var['name'])


# sample output:

# TeamA
# -----
# Alice
# Bob

# TeamB
# -----
# Charlie
# Dave



###############################################################################################################################

# write a program to read the below dictionary and display the expected output

info = {
"id": "0001",
"type": "donut",
"name": "Cake",
"image":
{
"url": "images/0001.jpg",
"width": 200,
"height": 200
},
"thumbnail":
{
"url": "images/thumbnails/0001.jpg",
"width": 32,
"height": 32
}
}


# sample output:

# ID              : 0001
# TYPE            : donut
# NAME            : Cake
# IMAGE URL       :"images/0001.jpg
# IMAGE WIDTH     : 200
# IMAGE HEIGHT    : 200
# THUMBNAIL URL   : "images/thumbnails/0001.jpg"
# THUMBNAIL WIDTH : 32
# THUMBNAIL HEIGHT:  32

for key, value in info.items():
    if isinstance(value, str):
        print(key.ljust(20), " : ", value)
    elif isinstance(value, dict):
        for skey, svalue in value.items():
            finalkey = key + ':' + skey
            print(finalkey.ljust(20), " : ", svalue)


###############################################################################################################################

data = {
    'Sales': {
        'North': {
            'Alice': 'Manager',
            'Bob': 'Sales Executive',
            'Eve': 'Sales Coordinator',
            'John': 'Account Manager'
        },
        'South': {
            'Charlie': 'Sales Executive',
            'Grace': 'Regional Sales Manager',
            'Mallory': 'Business Development Associate'
        },
        'West': {
            'Oscar': 'Sales Executive',
            'Peggy': 'Account Executive',
            'Victor': 'Territory Sales Manager'
        }
    },
    'Marketing': {
        'Digital': {
            'David': 'SEO Specialist',
            'Hannah': 'Content Strategist',
            'Irene': 'Social Media Manager'
        },
        'Offline': {
            'Eve': 'Event Coordinator',
            'Jake': 'Brand Manager',
            'Liam': 'Public Relations Specialist'
        },
        'Research': {
            'Mia': 'Market Research Analyst',
            'Noah': 'Customer Insights Manager'
        }
    },
    'IT': {
        'Infrastructure': {
            'Quinn': 'Network Engineer',
            'Riley': 'System Administrator',
            'Sam': 'Cloud Architect'
        },
        'Development': {
            'Tina': 'Software Engineer',
            'Uma': 'Backend Developer',
            'Walter': 'Full Stack Developer'
        }
    },
    'HR': {
        'Recruitment': {
            'Yara': 'Recruitment Specialist',
            'Zane': 'Talent Acquisition Manager',
            'Nina': 'HR Coordinator'
        },
        'Employee Relations': {
            'Oliver': 'Employee Relations Specialist',
            'Sophia': 'HR Business Partner'
        }
    },
    'Finance': {
        'Accounting': {
            'Xander': 'Accountant',
            'Yvette': 'Accounts Payable Specialist',
            'Zara': 'Financial Analyst'
        },
        'Audit': {
            'Luna': 'Internal Auditor',
            'Mason': 'Compliance Officer'
        }
    }
}


# write a program to display the below output:


# Sales
# -----
# North
# South
# West


# Marketing
# --------
# Digital
# Offline
# Research


# IT
# ---
# Infrasturcture
# Development

# HR
# ---
# Recruitment
# Employee Relations

###############################################################################################################################

# code:


for key,value in data.items():
    print(key)
    print("---------")
    for skey in value.keys():
        print(skey)
    print()


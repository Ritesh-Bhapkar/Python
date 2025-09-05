state_list=[
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal"
]
print(state_list[13])
print(state_list[-1])

## append ##
state_list.append("Partur")
print(state_list)

## insert at specific position ##
state_list.insert(-1,"Jalna")
print(state_list)

## adding multiple items at end ##
state_list.extend(["Sambhjingar","Parbhani"])
print(state_list)

## chnage the position of any item and replace it ##
state_list[2]="assam"
print(state_list)

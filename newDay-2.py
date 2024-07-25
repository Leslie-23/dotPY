myCars = ['camry','corolla','lamborghini','aventador','trotro']
print(myCars)

# the append() adds new elements at the end of the list
myCars.append('audi')
print(myCars)

# the insert() adds a new element to the 
myCars.insert(0,"bmw")
print(myCars)

# removing elements from the back of the list in a reusable way.
poppedCar = myCars.pop()
print(myCars)
print(poppedCar)

# remove() this method allows for rremoving stuff from the list
myCars.remove('camry')
print(myCars)


# deleting lists in .py
del myCars
# print(myCars) // will  not work as it has been deleted

# invite 10 people to a party ad store names in a list then print out 10 invites with the names in the list;

invitees = ['mary','joseph','joyce','enoch','joshua','peter','pan','kwaku','kwasi','miriam']

for i in invitees:
    print(f" Dear {i},  you are cordially invited")
    
removedGuest = invitees.pop(-1)
print(f"I am sorry, but we have received word that {removedGuest} can't make it today")

invitees.append('new1')
invitees.append('new2')
invitees.append('new3')
invitees.append('new4')
invitees.append('new5')
for i in invitees:
    print(f" Dear {i},  you are cordially invited")
myCars = ['camry','corolla','lamborghini','aventador','trotro']
print(myCars)

# the append() adds new elements at the end of the list
myCars.append('audi')
print(myCars)

# the insert() adds a new element to the 
myCars.insert(0,"bmw")
print(myCars)

# removing elements from the back of the list in a reusable way.
poppedCar = myCars.pop()
print(myCars)
print(poppedCar)

# remove() this method allows for rremoving stuff from the list
myCars.remove('camry')
print(myCars)


# deleting lists in .py
del myCars
# print(myCars) // will  not work as it has been deleted

# invite 10 people to a party ad store names in a list then print out 10 invites with the names in the list;

invitees = ['mary','joseph','joyce','enoch','joshua','peter','pan','kwaku','kwasi','miriam']

for i in invitees:
    print(f" Dear {i},  you are cordially invited")
    
removedGuest = invitees.pop(-1)
print(f"I am sorry, but we have received word that {removedGuest} can't make it today")

invitees.append('new1')
invitees.append('new2')
invitees.append('new3')
invitees.append('new4')
invitees.append('new5')

for i in invitees:
    print(f" Dear {i},  you are cordially invited")
# --------------
# --------------
# Code starts here
# Create the lists 
class_1=['Geroffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary  Mason','Carla Gentry','Corinna Cortes']
# Concatenate both the strings
new_class=class_1+class_2
print("New Class: ",new_class)
# Append the list
new_class.append("Peter Warden")
# Print updated list
print("Updated new class: ",new_class)
# Remove the element from the list
new_class.remove("Carla Gentry")
# Print the list
print("List: ",new_class)

# Create the Dictionary
#courses={'Math':65,'English':70,'History':80,'French':70,'Science':60}
courses={65,70,80,70,60}
# Slice the dict and stores  the all subjects marks in variable
# Store the all the subject in one variable `Total`
total=sum(courses)
# Print the total
print(total)
# Insert percentage formula
percentage=(total/500)*100
# Print the percentage
print(percentage)

# Create the Dictionary
mathematics={'Geroffrey Hinton':78,' Andrew Ng ':95,'Sebastian Raschka':65,'Yoshua Benjio':50,'Hilary Mason':50,'Corinna Cortes':66,'Peter Warden':75}
topper=max(mathematics,key=mathematics.get)
print(topper)

# Given string
topper.split()
print(topper)
# Create variable first_name 
first_name=topper.split()[0]
print("First name:\r",first_name)
# Create variable Last_name and store last two element in the list
last_name=topper.split()[1]
print("Last name:",last_name)
# Concatenate the string
c=' '
full_name=last_name+c+first_name
# print the full_name
print(full_name)
# print the name in upper case
certificate_name=full_name.upper()
print(certificate_name)
# Code ends here



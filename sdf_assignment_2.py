#Jasleen kaur

#SIMPLE DATA TYPES
Name = "Jasleen"
print(Name)
 
Mantioba_Driving_licene = "No"
print(Mantioba_Driving_licene)

Current_year = "2024"
print(Current_year)
                

#CALCULATIONS
# constants for Federal Goods and Services Tax (GST)
GST_RATE = 5
print(f"Federal Tax (GST) at {GST_RATE}%")

# constant for Manitoba Provisional tax (PST)
PST_RATE = 7
print(f"Provincial Tax (PST) at {PST_RATE}%")


# variable for the price of the vehicle
vehicle_price = 70000.00 
print(f"Vehicle Price: ${vehicle_price:.2f}")

#calculation of vehicle ,provincial and federal taxs.
vehicle_price = 70000.00
PST_RATE = 5
GST_RATE = 7
total_value = vehicle_price + PST_RATE + GST_RATE

print(f"vehicle_price: {vehicle_price}\nProvincial Tax: { PST_RATE}\nFederal Tax: {GST_RATE}\nTotal: {total_value}")


#LISTS

# A lists of values
list =1 ,2,3,4,5,6,7,8,9,10
print(type(list)) #type=values

# Add frist name between 5 and 6
list = [1,2,3,4,5,6,7,8,9,10]
Name = "Jasleen"
list.insert(5,Name)
print(list)

# Remove the number 9 from the list
list = [1,2,3,4,5,6,7,8,9,10]
list.remove(9)
print(list)

#A list of character A,B,C
character_list = [ 'A' , 'B' , 'C']
print(character_list)

# combined list 
combined_list = list + character_list
print(combined_list)


#TUPLES

#  initialize a tuple with the names of 4 Canadian provinces
canadian_provinces = ("Manitoba", "Ontario", "British Columbia", "Alberta")
print(canadian_provinces)


# Verify the data type of the tuple
print(type(canadian_provinces))

#DICTIONARIES

#SETS


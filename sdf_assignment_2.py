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
#  initialize a dictionary with keys 'nickel', 'dime', and 'quarter'
canadian_currency = {'nickel': 0.05, 'dime': 0.10, 'quarter': 0.25}
print(canadian_currency)


# Verify the data type of the dictionary
print(type(canadian_currency))


# Modify the values to use whole numbers
canadian_currency['nickel'] = 5
canadian_currency['dime'] = 10
canadian_currency['quarter'] = 25
print(canadian_currency)

# Add two items to the dictionary representing the loonie and toonie
canadian_currency['loonie'] = 100
canadian_currency['toonie'] = 200
print(canadian_currency)


#SETS

# A set containing even numbers between 2 and 20 inclusive
even_numbers_set = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
print(even_numbers_set)

# Verify the data type of the set
print(type(even_numbers_set))

# A set containing multiples of 5 between 5 and 20 inclusive
multiples_of_5_set = {5, 10, 15, 20}
print(multiples_of_5_set)

# Declare a set containing each unique value of the two sets created above
unique_values_set = even_numbers_set.union(multiples_of_5_set)
print(unique_values_set)

# A set containing only those values that appear in both sets
intersection_set = even_numbers_set.intersection(multiples_of_5_set)
print(intersection_set)

# A set containing only those values that appear in the first set but not in the second set
difference_set_1 = even_numbers_set.difference(multiples_of_5_set)
print(difference_set_1)

# A set containing only those values that appear in the second set but not in the first set
difference_set_2 = multiples_of_5_set.difference(even_numbers_set)
print(difference_set_2)



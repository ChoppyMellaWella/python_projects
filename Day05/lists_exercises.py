# 1. Declare an empty list
empty_list = list()
print(empty_list)

# 2. Declare a list with more than 5 items
network_device = ['router', 'firewall', 'access point', 'switch', 'pc']
print(network_device)

# 3. Find the length of your list
print(len(network_device))

# 4. Get the first item, the middle item and the last item of the list.
print(network_device[0], network_device[len(network_device)//2], network_device[-1])

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['gabuki', 100, 6.2, True, 'memory']
print(mixed_data_types)

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)

# 7. Print the list using print()
print(it_companies)

# 8. Print the number of companies in the list
print(len(it_companies))

# 9. Print the first, middle and last company
print(it_companies[0], it_companies[len(it_companies)//2], it_companies[len(it_companies)-1])

# 10. Print the list after modifying one of the companies
it_companies[0] = 'Nvidia'
print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append('AMD')
print(it_companies)

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies)//2, 'OpenAI')
print(it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
upper_case_apple = it_companies[it_companies.index('Apple')].upper() # get 'Apple' from list, uppercase all the letters, save to variable
it_companies.insert(it_companies.index('Apple'), upper_case_apple) # adds 'APPLE' before 'Apple' index
it_companies.remove('Apple') # removes 'Apple'
print(it_companies) # print out it_companies

# 14. Join the it_companies with a string '#;  '
    # Unsure what that means. Appending string to list
weird_string = '#;  '
it_companies.append(weird_string)
print(it_companies)

# 15. Check if a certain company exists in the it_companies list.
print('IBM' in it_companies) # True
print('Anthropic' in it_companies) # False

# 16. Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# 18. Slice out the first 3 companies from the list

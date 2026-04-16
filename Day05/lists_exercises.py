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
print(it_companies[:3:])

# 19. Slice out the last 3 companies from the list
print(it_companies[-1:-4:-1]) # reversed
print(it_companies[len(it_companies)-3:]) # last 3 left-to-right

# 20. Slice out the middle IT company or companies from the list
print(it_companies[len(it_companies)//2])

# 21. Remove the first IT company from the list
del it_companies[0]
print(it_companies)

# 22. Remove the middle IT company or companies from the list
del it_companies[(len(it_companies)-1)//2]
print(it_companies)

# 23. Remove the last IT company from the list
del it_companies[-1]
print(it_companies)

# 24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# 25. Destroy the IT companies list
del (it_companies)

"""
26. Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

"""
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print(front_end)

# 27. After joining the lists in question 26. Copy the joined list and 
# assign it to a variable full_stack, then insert Python and SQL after Redux.

full_stack = front_end
full_stack.insert(full_stack.index('Node'),'Python')
full_stack.insert(full_stack.index('Node'),'SQL')
print(full_stack)

# LEVEL 2

"""
1. 
    The following is a list of 10 students ages:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

    Sort the list and find the min and max age
    Add the min age and the max age again to the list
    Find the median age (one middle item or two middle items divided by two)
    Find the average age (sum of all items divided by their number )
    Find the range of the ages (max minus min)
    Compare the value of (min - average) and (max - average), use abs() method

"""

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(ages)
ages.sort()
print(f"sorted ages: {ages}")
print(f"min age: {ages[0]}\nmax age: {ages[-1]}")
print(f"median age: {ages[len(ages)//2]}")
print(f"average age: {sum(ages)//len(ages)}") # sum() not part of course
print(f"range age: {ages[-1] - ages[0]}")
print(f"(min - average): {-(ages[0] - (sum(ages)//len(ages)))}\n(max - average): {ages[-1] - (sum(ages)//len(ages))}") # added - as the suffix for min - average

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];

"""
1. Find the middle country(ies) in the countries list
2. Divide the countries list into two equal lists if it is even if not one more country for the first half.
3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

"""

# 1. Find the middle country(ies) in the countries list
print(countries[len(countries)//2], countries[(len(countries)//2)-1])

# 2. Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_half, second_half = countries[:len(countries)//2], countries[len(countries)//2]
print(first_half)
print()
print(second_half)
# 3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
these_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first, second, third, *scandic = these_countries
print(first, second, third, scandic)

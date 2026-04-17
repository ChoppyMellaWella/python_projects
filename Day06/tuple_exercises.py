# 1. Create an empty tuple
empty_tuple = ()

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
fake_siblings = ('john', 'jane', 'jack')
print(fake_siblings)

# 3. Join brothers and sisters tuples and assign it to siblings
brothers = ('john','jack')
sisters = ('jane', 'jackie')
siblings = brothers + sisters
print(siblings)

# 4. How many siblings do you have?
print(len(siblings))

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ('jonathan', 'joanna')
family_members = siblings + parents
print(family_members)

# 6. Unpack siblings and parents from family_members
sib1,sib2,sib3,sib4,dad,mom = family_members

# 7. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple','orange','kiwi','pineapple','tomato')
vegetables = ('brocoli','asparagus','kale','lettuce')
food_stuff_tp = fruits + vegetables
print(food_stuff_tp)

# 8. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# 9. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print(food_stuff_lt[len(food_stuff_lt)//2])

# 10. Slice out the first three items and the last three items from food_stuff_lt list
print(food_stuff_lt[:3],food_stuff_lt[len(food_stuff_lt)-3:])

# 11. Delete the food_stuff_tp tuple completely
del food_stuff_tp

"""
    Check if an item exists in tuple:

    Check if 'Estonia' is a nordic country

    Check if 'Iceland' is a nordic country

    nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
    
"""

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
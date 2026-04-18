# 1. Find the length of the set it_companies
it_companies = {'Apple','Microsoft','NVIDIA','Google','Amazon'}
print(len(it_companies))

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['Meta','Broadcom','IBM'])
print(it_companies)

# 4. Remove one of the companies from the set it_companies
it_companies.remove('Microsoft')
print(it_companies)

# 5. What is the difference between remove and discard
print("the difference between remove and discard is whether or not they " \
"output any errors if the function fails")

# LEVEL 2
# didnt see these sets before
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Join A and B
print(A | B)

# 2. Find A intersection B
print(A & B) # ampersand
print(A.intersection(B)) # intersection

# 3. Is A subset of B
print(A.issubset(B))

# 4. Are A and B disjoint sets
    # In Python, the term disjoint set typically refers
    # to one of two things: a relationship between sets
    # with no common elements or a specialized data 
    # structure used for tracking those relationships efficiently. 
print(A.isdisjoint(B))
print(B.isdisjoint(A))

# 5. Join A with B and B with A
A.union(B)
B.union(A)
print(A,B)

# 6. What is the symmetric difference between A and B
print(A.symmetric_difference(B))

# 7. Delete the sets completely
del A
del B

# LEVEL 3

# 1. Convert the ages to a set and compare the 
# length of the list and the set, which one is bigger?
set_age = set(age)
print(len(set_age))
print(len(age))

# 2. Explain the difference between the following 
# data types: string, list, tuple and set
print("Strings are a sequence of characters- Immutable\n" \
"Lists are an ordered and mutable collection allowing for duplicate elements\n" \
"Tuples are an ordered immutable collection allowing for duplicate elements\n" \
"Sets are an unordered mutable collection of unique elements")

# 3. I am a teacher and I love to inspire and 
# teach people. How many unique words have been 
# used in the sentence? Use the split methods 
# and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people'
split_sentence = sentence.split() # each word in list
set_sentence = set(split_sentence)
print(set_sentence)


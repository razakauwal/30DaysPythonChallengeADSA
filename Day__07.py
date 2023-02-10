#Day 7





it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}

length = len(it_companies)

print("The length of the set is:", length)





it_companies.add('Twitter')

print("The set after adding Twitter:", it_companies)





it_companies.update(['FlexiSAF', 'Instagram', 'Tik Tok', 'SanhaTech', 'Microsoft'])

print(it_companies)





it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}

del it_companies





print('''In Python, both remove and discard methods are used to remove elements from a set (a collection of unique elements).

The difference between the two methods lies in how they behave when trying to remove an element that does not exist 

in the set.



Therefore, it is recommended to use discard when you want to remove an element from a set

and do not care about raising an error if the element does not exist. On the other hand,

you should use remove if you want to ensure that the element you are trying to remove is in the set''')





A = {19, 22, 24, 20, 25, 26}

B = {19, 22, 20, 25, 26, 24, 28, 27}

age = [22, 19, 24, 25, 26, 24, 25, 24]





C = A.union(B)

print (C)





D = A.intersection(B)

print (D)





E = A.isdisjoint(B)

print (E)







F = A.union(B)



G = B.union(A)

# Print the results

print("Union of sets A and B:", F)

print("Union of sets B and A:", G)





H = A.symmetric_difference(B)

print(H)





# Delete set A

del A

# Delete set B

del B









ages = [22, 19, 24, 25, 26, 24, 25, 24]



unique_ages = set(ages)



print("Length of the list:", len(ages))

print("Length of the set:", len(unique_ages))





print ('''Strings: Strings are sequences of characters and are used to represent text data. They are defined using single quotes (') or double quotes ("). Strings are immutable, which means that you cannot modify individual characters within a string after it has been created.



Lists: Lists are ordered, mutable sequences of elements. You can add, remove, or modify elements within a list after it has been created. Lists are defined using square brackets ([]).



Tuples: Tuples are also ordered sequences of elements, but unlike lists, they are immutable. Once a tuple is created, you cannot modify its elements. Tuples are defined using parentheses (()).



Sets: Sets are unordered collections of unique elements. Sets are similar to lists and tuples, but unlike these data types, sets do not allow duplicates. Sets are defined using curly braces ({}).''')





sentence = "I am a teacher and I love to inspire and teach people."



words = sentence.split(" ")



unique_words = set(words)



count = len(unique_words)



print("Number of unique words:", count)


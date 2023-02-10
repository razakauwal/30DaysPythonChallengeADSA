#Day 6





tppl = ()

print ('Empty Tuple :', tppl)





male_siblings = ('Hanif', 'Munir', 'Imran')

female_siblings = ('Habiba', 'Zainab', 'Halima')

print(male_siblings)

print(female_siblings)





siblings = male_siblings + female_siblings

print("My Siblings are:", siblings) 





no_of_siblings = len(siblings)

print(no_of_siblings)





father_name = "Auwal"

mother_name = "Fatima"

family_members = siblings + (father_name, mother_name)

print(family_members)











siblings, parents = family_members[:7], family_members[7:]

print("Siblings:", siblings)

print("Parents:", parents)





fruits = ('mango', 'banana', 'udara')

vegetables = ('tomato', 'moringa', 'onions')

animal_products = ('milk', 'cheese', 'eggs')

food_stuff_tp = fruits + vegetables + animal_products

print(food_stuff_tp)





food_stuff_tp = fruits + vegetables + animal_products

food_stuff_lt = list(food_stuff_tp)

print(food_stuff_lt)







food_stuff_tp = fruits + vegetables + animal_products

middle_items_tp = food_stuff_tp[len(food_stuff_tp)//2-1:len(food_stuff_tp)//2+2]

print(middle_items_tp)





food_stuff_tp = fruits + vegetables + animal_products

food_stuff_lt = list(food_stuff_tp)



first_three = food_stuff_lt[:3]

last_three = food_stuff_lt[-3:]

print("First three items:", first_three)

print("Last three items:", last_three)





food_stuff_tp = fruits + vegetables + animal_products

del food_stuff_tp





nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')



if 'Estonia' in nordic_countries:

    print("Estonia is a nordic country.")

else:

    print("Estonia is not a nordic country.")



if 'Iceland' in nordic_countries:

    print("Iceland is a nordic country.")

else:

    print("Iceland is not a nordic country.")


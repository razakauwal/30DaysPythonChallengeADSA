#Day 5



empty = ()

print (empty)





languages = ['Hausa', 'Yoruba', 'Igbo', 'English', 'Malay']

print(languages)





print(len(languages))





first_item = languages [0] 

print("First item is:", first_item)

middle_item = languages [2]

print("Middle item is:", middle_item)

last_item =  languages [- 1]

print("Last Item is:", last_item)





mixed_data_types = ["Abdulrazak", 24, 183, "single", "Nigeria"]

print(mixed_data_types)





it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(it_companies)





number_of_companies = len(it_companies)

print("Number of companies:", number_of_companies)





first_item = it_companies [0] 

print("First item is:", first_item)

middle_item = it_companies [2]

print("Middle item is:", middle_item)

last_item =  it_companies [- 1]

print("Last Item is:", last_item)





it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

it_companies[3] = 'Tesla'

print(it_companies)





it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

it_companies.insert(3, 'IT Company')

print(it_companies)





it_companies[0] = it_companies[0].upper()

print(it_companies)





it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

joined_companies = "#".join(it_companies)

print(joined_companies)





it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

company = "Google"

if company in it_companies:

  print("The company exists in the list")

else:

  print("The company does not exist in the list")







it_companies.sort()

print(it_companies)





it_companies.reverse()

print(it_companies)





first_three_item = it_companies [0:3]

print(first_three_item)





last_three_item = it_companies [4:]

print(last_three_item)





it_companies = ['Facebook', 'Google', 'Microsoft', 'IT Company', 'Apple', 'IBM', 'Oracle', 'Amazon']

middle_item = it_companies [3]

print(middle_item)





del it_companies [3]

print(it_companies)





front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']

back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end

print(full_stack)





full_stack = front_end + back_end

full_stack.insert(5, 'Python')

full_stack.insert(6, 'SQL')

print(full_stack)









ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()

min_age = ages[0]

max_age = ages[-1]

print("Sorted ages:", ages)

print("Minimum age:", min_age)

print("Maximum age:", max_age)





ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()

n = len(ages)

if n % 2 == 0:

    median = (ages[n//2 - 1] + ages[n//2])/2

else:

    median = ages[n//2]

print(median)





ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

average_age = sum(ages) / len(ages)

print("The average age is:", average_age)





ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

min_age = min(ages)

max_age = max(ages)

range_of_ages = max_age - min_age

print("The range of ages is:", range_of_ages)





min_age = min(ages)

max_age = max(ages)

average = sum(ages)/len(ages)

print(abs(min_age - average))

print(abs(max_age - average))





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

  'Cambodia',

  'Cameroon',

  'Canada',

  'Cape Verde',

  'Central African Republic',

  'Chad',

  'Chile',

  'China',

  'Colombi',

  'Comoros',

  'Congo (Brazzaville)',

  'Congo',

  'Costa Rica',

  "Cote d'Ivoire",

  'Croatia',

  'Cuba',

  'Cyprus',

  'Czech Republic',

  'Denmark',

  'Djibouti',

  'Dominica',

  'Dominican Republic',

  'East Timor (Timor Timur)',

  'Ecuador',

  'Egypt',

  'El Salvador',

  'Equatorial Guinea',

  'Eritrea',

  'Estonia',

  'Ethiopia',

  'Fiji',

  'Finland',

  'France',

  'Gabon',

  'Gambia, The',

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

  'Macedonia',

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

  'Norway',

  'Oman',

  'Pakistan',

  'Palau',

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

  'Saint Vincent',

  'Samoa',

  'San Marino',

  'Sao Tome and Principe',

  'Saudi Arabia',

  'Senegal',

  'Serbia and Montenegro',

  'Seychelles',

  'Sierra Leone',

  'Singapore',

  'Slovakia',

  'Slovenia',

  'Solomon Islands',

  'Somalia',

  'South Africa',

  'Spain',

  'Sri Lanka',

  'Sudan',

  'Suriname',

  'Swaziland',

  'Sweden',

  'Switzerland',

  'Syria',

  'Taiwan',

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

  'Zimbabwe',

]



middle = len(countries)//2

middle_countries = countries[middle-1:middle+2]

print(middle_countries)





divide_countries_equally = len(countries)//2

print(divide_countries_equally)





countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

first_three = countries [0:3]

scandic_countries = countries [3:]

print("First Three Countries:", first_three)

print("Scandic Countries:", scandic_countries)


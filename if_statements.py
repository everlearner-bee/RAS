#if statements with lists

# countries = ['spain','england','germany', 'brazil','qatar','saudi arabia']

# for country in countries:
#     if country != 'saudi arabia'and "england":
#         print(f"this is the country is qualified play in the world cup, {country.upper()}")
#     else:
#         print(f"{country.title() }, is banned to play in the world cup")
 
 #using if else and elif else-elif is used only when you require one test to pass

student_marks = 389

if student_marks < 300:
    print("the student does not qualify to join junior sec")
elif student_marks >= 300 and student_marks <= 349:
    print("the student qualifies for junior sec ")
else:
     student_marks >= 350 and student_marks <500
     print("the student qualifies to join and deserves recognition")

#example with list of countries

# if 'saudi arabia' in countries:
#     print('this country qualifies for world cup')
# if 'germany' in countries:
#     print('this country qualifies for world cup')
# if 'rome' in countries:
#     print('this country qualifies for world cup')
# if 'england' in countries:
#     print('this country qualifies for world cup')

# print("\n find out which other teams qualify")

# checking for multiple conditions using two lists

countries = ['spain','england','germany','paraguay','chile' 'brazil','qatar','saudi arabia']

qualifying_countries = ['spain','england', 'brazil','qatar','saudi arabia']

for qualifying_countries in qualifying_countries:
    if qualifying_countries in countries:
        print(f"the mentioned country qualifies for world cup,{qualifying_countries.title()}" )
    else:
        print('the country does not qualify for the world cup')
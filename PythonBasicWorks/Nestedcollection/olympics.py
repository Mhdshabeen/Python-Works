olympic_medal_count = [
    {"country": "United States", "gold": 39, "silver": 41, "bronze": 33},
    {"country": "China", "gold": 38, "silver": 32, "bronze": 18},
    {"country": "Japan", "gold": 27, "silver": 14, "bronze": 17},
    {"country": "Great Britain", "gold": 22, "silver": 21, "bronze": 22},
    {"country": "Russia", "gold": 20, "silver": 28, "bronze": 23},
    {"country": "Australia", "gold": 17, "silver": 7, "bronze": 22},
    {"country": "Netherlands", "gold": 10, "silver": 12, "bronze": 14},
    {"country": "France", "gold": 10, "silver": 12, "bronze": 11},
    {"country": "Germany", "gold": 10, "silver": 11, "bronze": 16},
    {"country": "Italy", "gold": 10, "silver": 10, "bronze": 20}
]

# Q1 print the contry with most gold medal

# max_gold=max(olympic_medal_count,key=lambda con:con.get("gold"))

# print(max_gold.get("country"))

# Q2 each contries medal count

medal_count_list={country.get("country"):country.get("gold")+country.get("silver")+country.get("bronze") for country in olympic_medal_count}

# print(medal_count_list)

# Q3 contry with lest num of medals

least_medal_country=min(medal_count_list,key=lambda i:medal_count_list.get(i)) 

# print(least_medal_country)

# Q4 sort contries with medal count

for country in olympic_medal_count: # {"country": "United States", "gold": 39, "silver": 41, "bronze": 33}

    for i in medal_count_list: # 'United States': 113

        if country.get("country")==i: # united states==united states

            country["total"]=medal_count_list.get(i)

sorted_contries_on_medal_count=sorted(olympic_medal_count,key=lambda country:country.get("total"),reverse=True)

# print(sorted_contries_on_medal_count)

# Q5 sum of each medals in the list(gold,silver,bronze)

sum_of_medals={i:sum([country.get(i) for country in olympic_medal_count]) for country in olympic_medal_count for i in country if i=="gold" or i=="silver" or i=="bronze" }

print(sum_of_medals)

# Q6 sort the contries using bronze medal count

sort_country_on_bronze_medal=sorted(olympic_medal_count,key= lambda i:i.get("bronze"),reverse=True)

# print(sort_country_on_bronze_medal)

# Q7 print the contries with same gold medal count

# contries_with_same_gold_medal={country.get("gold"):country.get("country") for country in olympic_medal_count}
contries_with_same_gold_medal={}

for i in olympic_medal_count:

    if i.get("gold") in contries_with_same_gold_medal:

        contries_with_same_gold_medal[i.get("gold")]+= ", " + i.get("country")

    else:

        contries_with_same_gold_medal[i.get("gold")]=i.get("country")
    
# print(contries_with_same_gold_medal)

# Q8 print the second highest contry with most gold medal

sort_by_gold_medal_count=sorted(olympic_medal_count,key=lambda country:country.get("gold"),reverse=True)

# print(sort_by_gold_medal_count)

second_highest_goldmedal_country=sort_by_gold_medal_count[1]

# print(second_highest_goldmedal_country)

# Q9 total count of medals

totl_medal_count=sum([country.get("total") for country in olympic_medal_count])

# print(totl_medal_count)

# Q10 print contry name with their number of total medals

# for i in olympic_medal_count:

#     print(i.get("country"),">: ",i.get("total"))

# Q11 disply contries with more than 25 gold medals

contries_with_more_than={country.get("country"):country.get("gold") for country in olympic_medal_count if country.get("gold")>25}

print(contries_with_more_than)

# Q12 display contries with same number of gold and silver medals

same_numof_goldandsilver=[i ]

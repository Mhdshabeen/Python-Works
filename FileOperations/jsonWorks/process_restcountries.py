
from json import load

f=open("C:\\Users\\Lenovo\\Desktop\\WebDevelopment\\FileOperations\\jsonWorks\\restcountries.json",encoding="UTF-8")

countries=load(f)

# data of given country

def country_data(name):

    return [c for c in countries if c.get("name")==name][0]

country_filter=country_data("Belize")

# Q1 disply country names

countries_name=[dic.get("name") for dic in countries]

# print(countries_name)

# Q2 print countries with starting "I"

countries_starts_with_I=[dic.get("name") for dic in countries if dic.get("name").startswith("I")]

# print(countries_starts_with_I)

# Q3 disply list of countries names starts with 'Sa' or 'Ba'

countries_starts_with_Sa_Ba=[dic.get("name") for dic in countries if dic.get("name").startswith("Sa") or dic.get("name").startswith("Ba")]

# print(countries_starts_with_Sa_Ba)

# Q4 disply topLevelDomine of each country

countries_topLevelDomain=[{dic.get("name"):dic.get("topLevelDomain")[0]} for dic in countries]

# print(countries_topLevelDomain)

# Q5 display topLevelDomain of Mexico

countries_topLevelDomain_Mexico=[dic.get("topLevelDomain")[0] for dic in countries if dic.get("name")=="Mexico"]

# print(countries_topLevelDomain_Mexico)

# Q6 

#

# Q7 get country with higest population

contry_with_highest_population=max(countries,key= lambda dict:dict.get("population"))

# print(contry_with_highest_population.get("name"),contry_with_highest_population.get("population"))

# Q8 get contry with min population

contry_with_lowest_population=min(countries,key= lambda dict:dict.get("population"))

# print(contry_with_lowest_population.get("name"),":>",contry_with_lowest_population.get("population"))

# Bouvet=[dic.get("name") for dic in countries if dic.get("population")==contry_with_lowest_population.get("population")]

# print(Bouvet)

# Q9 contries in population range

contries_in_population_range=[dic.get("name") for dic in countries if dic.get("population") in range(10353442,114963584)]

# print(contries_in_population_range)

# Q10 display country with second highest population

second_highest_population=0

first_population=0

for dic in countries:

    population=dic.get("population")

    if population>first_population:

        second_highest_population=first_population

        first_population=population

    elif population<first_population and population>second_highest_population:

        second_highest_population=population

contry_with_second_highest_population=[dic.get("name") for dic in countries if dic.get("population")==second_highest_population]

# print(contry_with_second_highest_population)




# Q11 sort contries in decreasing population

sorted_in_dic_order=sorted(countries,key=lambda dic:dic.get("population"),reverse=True)

countries_in_dec_population_order=[{dic.get("name"):dic.get("population")} for dic in sorted_in_dic_order]

# print(countries_in_dec_population_order)

# Q12 print the other names of given country

len_of_othernames=len(country_filter.get("regionalBlocs"))

if "regionalBlocs" in country_filter:

    regionalBlocs=country_filter.get("regionalBlocs")

    # while(len_of_othernames<=0):

    for i in regionalBlocs:

        # print({"name":country_filter.get("name"),"regional acronym":i.get("acronym")},":>","othernames=",i.get("otherNames"))
        pass

# Q13 display country with max area
def get_area(dic):

    if "area" in dic:

        return dic.get("area")
    else:

        return 0

largest_area_country=max(countries,key=get_area) 

# print(largest_area_country.get("name"),largest_area_country.get("area"))

# Q14 contries with language english

for dic in countries:

    for l in dic.get("languages"):

        if l.get("name")=="English":

            # print(dic.get("name"))

            pass

# Q15  largest region by area

area_dic={}

for dic in countries:

    area=get_area(dic.get("name"))

    # if dic.get("area")!=None:

    if dic.get("region") in area_dic:

        area_dic[dic.get("region")]+=float(dic.get("area",0))
    else:

        area_dic[dic.get("region")]=float(dic.get("area",0))

largest_region_by_area=max(area_dic,key=lambda key:area_dic.get(key))

print(area_dic)

# Q16 get the count of countries in each region

count_of_countries_in_region={}

for dic in countries:

    if dic.get("region") in count_of_countries_in_region:

        count_of_countries_in_region[dic.get("region")]+=1

    else:

        count_of_countries_in_region[dic.get("region")]=1

# print(count_of_countries_in_region)

# Q17 get the capital of the given countries

list=["India","Japan","China","Pakistan"]

for co in list:

    for dic in countries:

        if dic.get("name")==co:

            pass

            # print(co,":>" , dic.get("capital"))

# Q18 coutries sharing border with india

india_border=["India"]

for dic in countries:

    if "borders" in dic:

        if "IND" in dic.get("borders"):

            india_border.append(dic.get("name"))

# print(india_border)

# Q19 languages speaked in india and near by contries

border_country_languages={}

for co in india_border:

    for dic in countries:

        if co==dic.get("name"):

            for lan in dic.get("languages"):

                if co in border_country_languages:

                    border_country_languages[co]+= ","+lan.get("name")

                else:

                    border_country_languages[co]=lan.get("name")

print(border_country_languages)
            



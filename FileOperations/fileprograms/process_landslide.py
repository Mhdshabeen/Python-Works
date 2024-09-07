
f=open("C:\\Users\\Lenovo\\Desktop\\WebDevelopment\\fileprograms\\land_slide.txt","r")
land_slide=[]

for line in f:

    word=line.strip("\n").split(" ")

    land_slide.append({"state":word[0],"year":(word[1]),"death":int(word[2])})

# Q1 total death count

# total_death=[dicts.get("death") for dicts in land_slide]

# total_death_count=sum(total_death)

# print(total_death_count)

# Q2 most death count state or death per state

death_by_state={}

# for i in land_slide: # {'state': 'Kerala', 'year': 2018, 'death': 14}

#     if i.get("state") in death_by_state:

#         death_by_state[i.get("state")]+=i.get("death")

#     else:

#         death_by_state[i.get("state")]=i.get("death")

# most_death_count_state=max(death_by_state,key=lambda key:death_by_state.get(key))

# print(death_by_state)
               

# death_count_of_each_state={i.get("state"): for i in land_slide}

# Q3 most death count year

death_by_year={}

# for dicts in land_slide:

#     if dicts.get("year") in death_by_year:

#         death_by_year[dicts.get("year")]+=dicts.get("death")

#     else:

#         death_by_year[dicts.get("year")]=dicts.get("death")

# print(death_by_year)

# Q4 list states effected land slide

# states_landslide={states.get("state") for states in land_slide}

# print(states_landslide)

#Q5 display how many deaths in kerala in 2020

# kerala_death_2020=[i.get("death") for i in land_slide if i.get("state")=="Kerala" and i.get("year")==2020]

# print(kerala_death_2020)

# Q6 compine multiple states to 1 entry


# Q7 state with more death in 2021

# land_slide_2021=[i for i in land_slide if i.get("year")=="2021"]

# max=max(land_slide_2021,key=lambda key:key.get("death"))

# print(max)

# Q8 in which of the years states caused landslide

# state_with_year_wise={}

# for i in land_slide:

#     if i.get("state") in state_with_year_wise:

#         state_with_year_wise[i.get("state")]+="," + str(i.get("year"))

#     else:
#         state_with_year_wise[i.get("state")]=str(i.get("year"))

# print(state_with_year_wise)

# Q9 in 2018 which state are suspect to landslide

# state_effected_landslide_in_2018=[states.get("state") for states in land_slide if states.get("year")==2018]

# print(state_effected_landslide_in_2018)

# Q10 land slide cause death more than 15

# land_slide_with_death_more_than_15=[state for state in land_slide if state.get("death")>=15]

# print(land_slide_with_death_more_than_15)

# sort land slides based on the siviarity of the land slide

# sorted_list=sorted(land_slide,key=lambda key:key.get("death"),reverse=True)

# for i in sorted_list:

#     print(i.get("death"),"death in",i.get("state"),i.get("year"),"landslide")

# print(sorted_list)
            









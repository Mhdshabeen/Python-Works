

movies=[
 
    {
        "title": "Drishyam",
        "year": 2013,
        "language": "Malayalam",
        "genres": ["Crime", "Drama", "Thriller"],
        "rating": 8.6
    },
    {
        "title": "Premam",
        "year": 2015,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    {
        "title": "Bangalore Days",
        "year": 2014,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    {
        "title": "Kaala",
        "year": 2018,
        "language": "Tamil",
        "genres": ["Action", "Drama"],
        "rating": 7.3
    },
    {
        "title": "Vikram Vedha",
        "year": 2017,
        "language": "Tamil",
        "genres": ["Action", "Crime", "Thriller"],
        "rating": 8.4
    },
    {
        "title": "Super Deluxe",
        "year": 2019,
        "language": "Tamil",
        "genres": ["Drama", "Mystery", "Thriller"],
        "rating": 8.3
    },
  
    {
        "title": "Dangal",
        "year": 2016,
        "language": "Hindi",
        "genres": ["Action", "Biography", "Drama"],
        "rating": 8.4
    },
    {
        "title": "3 Idiots",
        "year": 2009,
        "language": "Hindi",
        "genres": ["Comedy", "Drama"],
        "rating": 8.4
    },
    {
        "title": "Gully Boy",
        "year": 2019,
        "language": "Hindi",
        "genres": ["Drama", "Music"],
        "rating": 8.0
    }
]


# Q1 total number of movies

# total_number_of_movies= len(movies)

# # print(total_number_of_movies)

# # Q2 movie with genere drama

# genere_drama=[mov.get("title") for mov in movies if "Drama" in mov.get("genres")]

# # print(genere_drama)

# #Q3 latest movie


# latest=max(movies,key=lambda mov:mov.get("year"))

# latest_movies=[mov.get("title") for mov in movies if mov.get("year")==latest.get("year")]

# # print(latest)

# #Q4 movie with highest rating

# rating=max(movies,key=lambda mov:mov.get("rating"))

# highest_rating_movies=[mov.get("title") for mov in movies if mov.get("rating")==rating.get("rating")]

# # print(highest_rating_movies)

# # Q5 movie with language malyalam

# malayalm_movie=[mov.get("title") for mov in movies if mov.get("language")=="Malayalam"]

# # print(malayalm_movie)

# #Q6 movie relesed after 2016

# latest=max(movies,key=lambda mov:mov.get("year"))

# movies_after_2016=[mov.get("title") for mov in movies if mov.get("year") in range(2016,latest.get("year")+1)]

# # print(movies_after_2016)


# # Q7 movie with lower rating

# rating=min(movies,key=lambda mov:mov.get("rating"))

# lowest_rating_movies=[mov.get("title") for mov in movies if mov.get("rating")==rating.get("rating")]

# # print(lowest_rating_movies)

# # Q8 malayalam movie with genere action

# mal_movie_genre_action=[mov.get("title") for mov in movies if mov.get("language")=="Malayalam" and "Action" in mov.get("genres")]

# print(mal_movie_genre_action)

# Q9 Movies release in same years

# years=set(mov.get("year") for mov in movies)

# years=list(years)

# movies_in_same_year={}

# for yr in years:

    # for mov in movies:

    #     if mov.get("year")==yr:

    #         if yr in movies_in_same_year:

    #             movies_in_same_year[yr]+= ", " + mov.get("title")

    #         else:

    #             movies_in_same_year[yr]=mov.get("title")

# for i in movies_in_same_year:

    # print(i,movies_in_same_year.get(i))


# # Q10 oldest movie

# oldest=min(movies,key=lambda mov:mov.get("year"))

# oldest_movie=[mov.get("title") for mov in movies if mov.get("year")==oldest.get("year")]

# # print(oldest_movie)

# # Q11 movie name with generes either Drama or Comedy

# movie_with_genere_dramaorcomedy=[mov.get("title")for mov in movies if "Drama" in mov.get("genres") or "Action" in mov.get("genres")]

# # print(movie_with_genere_dramaorcomedy)

# Q12 numbers of movie released in each year

# years=[mov.get("year") for mov in movies]

# count_of_movies_released={yr:years.count(yr) for yr in years}

# print(count_of_movies_released)

# Q13 print all type of genres

# generes={g for mov in movies for g in mov.get("genres")}

# print(generes)

# Q14 print count of movies in each geners

geners_list=[g for mov in movies for g in mov.get("genres")]

# print(geners_list)

genres_movie_count={g:geners_list.count(g) for g in geners_list}

# print(genres_movie_count)

# Q15 sort movie data using name of the movie

sorted_list=sorted(movies,key=lambda mov:mov.get("title"))



print([sr.get("title") for sr in sorted_list])



# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 18:04:42 2022

@author: puniaa
"""

import json

def get_movies(min_year,max_year,movies):
    movie_dict = movies.copy();
    for movie in movies:

        if int(movies[movie]['movie_year']) < min_year or int(movies[movie]['movie_year']) > max_year:
            del movie_dict[movie]
            
    return movie_dict

def compute_average(ratings,movie,w1,w2, movie_name):
    irating = movies[movie_name]["rating"]
    twitr = ratings[movie_name]
    if len(twitr) >= 3:
        average_twitter_rating = sum(twitr)/len(twitr)
        avg = (w1 * irating + w2 * average_twitter_rating) / (w1 + w2)
    else:
        avg = -1
    return avg



if __name__ == "__main__":
    
    movies = json.loads(open("movies.json").read())
    ratings = json.loads(open("ratings.json").read())
    min_year = input("Min year => ").strip()
    print(min_year)
    min_year = int(min_year)
    max_year = input("Max year => ").strip()
    print(max_year)
    max_year = int(max_year)
    w1 = float(input("Weight for IMDB => "))
    print(w1)
    w2 = float(input("Weight for Twitter => "))
    print(w2)
    movie_list = get_movies(min_year,max_year,movies)
    new_list = []
    i = 0
    movies_with_ratings = []
    movies_list1 = list(movie_list.values())
    movies_list2 = list(movie_list)
    i = 0
    for movie in movies_list1:
        if movies_list2[i] in ratings:
                avg = compute_average(ratings,movie,w1,w2, movies_list2[i])
                movies_with_ratings.append((movie, avg))
        i+=1
        
    for j in range(len(movies_with_ratings)-1, -1, -1):
        if movies_with_ratings[j][1] == -1:
            movies_with_ratings.pop(j)
            
            
    movies_with_ratings.sort(key = lambda x: x[1])
    while True:
        final_list = []
        User_input = input("What genre do you want to see? ")
        print(User_input)
        if("-" in User_input):
            User_input = User_input.split("-")
            User_input1 = User_input[0].lower();
            User_input1 = User_input1.capitalize();
            User_input2 = User_input[1].lower();
            User_input2 = User_input2.capitalize();
            genre = User_input1 + "-" + User_input2
            User_input = genre;
        else:
            User_input = User_input.lower();
            User_input = User_input.capitalize();
        
        
        
        
        if User_input == "Stop":
            break
        else: 
            for movie in range(len(movies_with_ratings)):
                if User_input in movies_with_ratings[movie][0]["genre"]:
                    final_list.append(movies_with_ratings[movie])
                    #print(final_list)
                    #best one##
                    name = final_list[-1][0]["name"]
                    rating = final_list[-1][1]
                    year = final_list[-1][0]["movie_year"]
                    ##worse one##
                    name1 = final_list[0][0]["name"]
                    rating1 = final_list[0][1]
                    year1 = final_list[0][0]["movie_year"]
            print("Best:")
            print("        Released in ",year,",",name, "has a rating of",round(rating,2))
            print("Worse:")
            print("        Released in ",year1,",",name1, "has a rating of",round(rating1,2))
                
capitals={
    "France": "Paris",
    "Germany": "Berlin",
    "Australia": "Melbourne",
}

#Nested list in a dictionary
travel_log={
    "France":["Paris","Lille","Dijon"],
    "Germany":["Stuttgart","Berlin"]
}
print(travel_log)
for city in travel_log:
    print(travel_log[city])

#To print Lille from travel_log
print(travel_log["France"][1])

nested_list=["A","B",["C","D"]]
#To print D out of nested_list
print(nested_list[2][1])

#Dictionary in a dictionary
travel_city={
    "France":{
        "cities_visited":["Paris","Lille","Dijon"],
        "num_times_visited":8,
    },
    "Germany":{
        "cities_visited":["Berlin","Hamburg","Stuttgart"],
        "num_times_visited":5,
    },
}
#To print "Stuttgart" out of travel_city dictionary
print(travel_city["Germany"]["cities_visited"][2])

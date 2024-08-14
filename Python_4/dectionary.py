travel_log =[
{
    "country":"France",
    "vistis": 12,
    "cities":["Paris" ,"Lille","Dijon"]
},
{
    "country":"Germen",
    "vistis": 12,
    "cities":["Berlin" ,"Humberg","Stuttgard"]
}

]

def add_new_country (country_visited , time_visited , cities_visited):
     new_country = {}
     new_country["country"] = country_visited
     new_country["vistis"] = time_visited
     new_country["cities"]  = cities_visited
     travel_log.append(new_country)


add_new_country(
     input("which country you visited ? \n"),
     input("Hom mamy times ? \n"),
     input("which cities ? ")
)
print (travel_log)
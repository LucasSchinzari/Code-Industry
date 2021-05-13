#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered, changeable and does not allow duplicates.

skate_colors = (
    {"Red Gazelle": "Red", "Truck": "Carver"},
    {"Hyper Speeder": "Black", "Truck": "Street"},
    {"Charger Daytona": "Orange", "Truck": "Long"}

)

print(skate_colors[2]["Charger Daytona"])

#changing the value of a key:
band_songs = {"Das Kombinat": "Zusammenbruch", "KMFDM": "Welcome"}

band_songs ["Das Kombinat"] = "Zukunft"
print(band_songs)

my_friends = {
    'Jose': {'last_seen': 6},
    'Rolf': {'surname': 'Smith'},
    'Anne': 6
}

print(my_friends['Jose'])
print(my_friends['Jose']['last_seen']) # my_friends['Jose'] gives us a dictionary, and we're then accessing the 'last_seen'
                                       # property of that dictionary, which gives us the value 6.


players = [
    {
        'name': 'Rolf',
        'numbers': (13, 22, 3, 6, 9)
    },
    {
        'name': 'John',
        'numbers': (22, 3, 5, 7, 9)
    }
]

#We're first printing the 'numbers' property of element 0 in the list, which gives us the tuple.
# Then we're also printing out the first element of that tuple.
print(players[0]['numbers'])
print(players[0]['numbers'][0])
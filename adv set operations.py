#difference statement will show the difference between two variables
#exemple of the difference statement:

skate_friends = {'toubo','Victor','Lucas'}
beach_tennis_friends = {'Gustavo','Camila','Lucas'}

skate_but_not_beach_tennis = skate_friends.difference(beach_tennis_friends)
beach_tennis_but_not_skate = beach_tennis_friends.difference(skate_friends)

print('Skate but not beach tennis:', skate_but_not_beach_tennis)
print('Beach tennis but not skate:',beach_tennis_but_not_skate)
print("===================================================")


#Symmetric_difference will show everything thats not duplicated between two variables
#Exemple of the symmetric_difference statement:

skate_friends = {'toubo','Victor','Lucas'}
beach_tennis_friends = {'Gustavo','Camila','Lucas'}

skate_not_in_both = skate_friends.symmetric_difference(beach_tennis_friends)

print('Not in both:',skate_not_in_both)
print("===================================================")

#Intersection shows the elements that are duplicated (exists in both variables,lists,etc)
#exemple of the intersection statement:

skate_friends = {'toubo','Victor','Lucas'}
beach_tennis_friends = {'Gustavo','Camila','Lucas'}

in_both = skate_friends.intersection(beach_tennis_friends)

print('In both',in_both)
print("===================================================")

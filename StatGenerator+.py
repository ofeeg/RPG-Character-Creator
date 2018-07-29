import os.path
save_path = "C:/Users/the/Desktop/"


characterID = str(input("Who is this character"))

completeName = os.path.join(save_path, characterID + ".txt")

Character = open(completeName, "w")


Stats = ['HP' , 'JP'  , 'STR' , 'INT' , 'DEX'  , 'END' , 'WIS'  , 'ACC' ]


count = 0
for stat in enumerate(Stats):
    newstat = input("Please enter the amount for %s " % (Stats[count]))
    Stats[count] = newstat
    count += 1
#writes info into GDScript language(python-like)
Character.write("""#BaseStats
var HP = %s
var JP = %s
var STR = %s
var INT = %s
var DEX = %s
var END = %s
var WIS = %s
var ACC = %s
#Stats are in an array
Stats = [HP, JP , STR, INT, DEX, END, WIS, ACC]""" % (Stats[0], Stats[1], Stats[2] , Stats[3] , Stats[4], Stats[5], Stats[6], Stats[7])
 )
Character.close()
input("Press enter to continue")



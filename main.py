from room import Room
from character import Enemy, Friend
from item import Item


shore = Room("Shore")
beach = Room("Beach")
camp = Room("Camp")
forest = Room("Forest")
clearing = Room("Clearing")
palace = Room("Palace")
cage = Room("Cage")

shore.set_description("A pale sandy beach with clear blue waves swishing up and down.")
beach.set_description("A long stretch of beach with wild shrubs growing along the dunes")
camp.set_description("A camp full of menacing soldiers. You don't like the look of them so you sneak around the edge to the large cage behind all the tents")
cage.set_description("a large cage with a gloomy woman held prisoner inside")
forest.set_description("A dark forest with venoumus flowering vines and trees that block out all the light.")
clearing.set_description("a small sundappled clearing with an aura of mischievousness")
palace.set_description("A vast palace with vines on every doorway, the nymphs inside scatter as you arrive")

shore.link_room(beach, "East")
beach.link_room(camp, "East")
beach.link_room(shore, "West")
beach.link_room(forest, "South")
camp.link_room(beach, "West")
camp.link_room(cage, "East")
cage.link_room(camp, "West")
cage.link_room(beach, "South")
forest.link_room(beach, "North")
forest.link_room(clearing, "South")
clearing.link_room(forest, "North")
clearing.link_room(palace, "South")
palace.link_room(clearing, "North")

cage.lock()
forest.lock()
clearing.lock()

moly = Item("Moly")
moly.set_description("a pink and yellow moly flower with nine petals.")
clearing.set_item(moly)

key = Item("key")
key.set_description("a rusty key that shaped like a blue police box")
shore.set_item(key)

carrots = Item("Carrots")
carrots.set_description("a bunch of wild carrots ready for the taking")
beach.set_item(carrots)

sunglasses = Item("Sunglasses")
sunglasses.set_description("some ancient greek shades that probably belonged to Pythagoras at some point")
cage.set_item(sunglasses)

circe = Enemy("Circe", "A tall sorceress with magic sparking along her skin")
circe.set_conversation("You've made your one wrong move now you're done for. It's time to die young traveler")
circe.set_weakness("Moly")
palace.set_character(circe)

pigs = Enemy("Pigs", "A group of large pigs that swarm you, blocking your path forward")
pigs.set_conversation("Oink oink")  
pigs.set_weakness("Carrots")
forest.set_character(pigs)

odyseuss = Friend("Odyseuss", "A ragged man standing ankle deep in the water")
odyseuss.set_conversation("Hello young traveller, I am as stuck on this island as you are. You must defeat Circe so we can leave this place. There is a key in the sand over there. Take it to aid your quest")
shore.set_character(odyseuss)

hermes = Friend("Hermes", "A tall god with a long fur coat. He holds a bag in his hands")
hermes.set_conversation("Be careful with Circe. Its only one wrong move and you're done for. Take this Moly and good luck!")
clearing.set_character(hermes)

medea = Friend("Medea", "A gloomy woman with red rimmed eyes")
medea.set_conversation("thank you for releasing me. These men have killed my brother and imprisoned me. As a thank you please take those sunglasses of immunity in the corner of the cage they will allow you to get past the forest to defeat circe")
cage.set_character(medea)

current_room = shore
backpack = []

dead = False
while dead == False:

    if key in backpack:
        cage.unlock()

    if sunglasses in backpack:
        forest.unlock()


        
    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")


    if command in ["North", "South", "East", "West"]:
        current_room = current_room.move(command)

    elif command == "Talk":
        if inhabitant is not None:
            inhabitant.talk()

        else:
            print("There is no one here to talk to")
    
    
    elif command == "Take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)
    
    elif command == "Fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("What will you fight with?")
            fight_with = input()
            if fight_with in backpack:
                if inhabitant.fight(fight_with) == True:
                    print("Hooray, you won the fight!")
                    current_room.set_character(None)
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
      

    

    else: 
         print("I don't understand that command")
    



    

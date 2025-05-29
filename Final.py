total_points = 0

def area_prompt():
    area_def = input("What woulr your ideal place be? Choose one: rural, city, in between")
    print(area_def)
    return area_def
area_choice = area_prompt()

if area_choice == "rural":
    total_points +=1
elif area_choice == "city":
    total_points +=3
elif area_choice == "in between":
    total_points += 2
else:
    print("incorrect please try again")

input("what weather would you like? choose one: tropical,warm,cold,nuetral")
if "warm":
    total_points +=1
elif "cold":
    total_points+=7
elif "tropical":
    total_points +=5
elif "neutral":
    total_points +=4
else:
    print("incorrect answer")

input("would you like to go out of the country? choose one:yes, no, no but close to far")
if "yes":
    total_points +=2
elif "no":
    total_points +=5
elif "no but close to far":
    total_points +=3
else:
    print("incorrect answer")

input("What is your buget-choose one:$1000-$3000,$3000-$5000,$5000-$7000")
if "$1000-$3000":
    total_points +=3
elif "$3000-$5000":
    total_points +=4
elif "$5000-$7000":
    total_points +=5
else:
    print("incorrect answer please try again")

input ("type of vacation, choose one: friends, family, work vacation, duo trip with partner")
if "family":
    total_points +=2
elif "friends":
    total_points +=8
elif "work vacation":
    total_points +=10
elif "duo trip with partner":
    total_points +=6

print(" The points that you have collected are", total_points)
rural= ["Chattanooga", "Tennessee", "Molokai", "Hawaii, Ozarks", "Missouri & Arkansas", "Steamboat Springs", "Colorado"]
tropical = ["Belize", "Riviera Maya", "Mexico", "Bali", "Indonesia", "Maui", "Hawaii", "Bora Bora", "French Polynesia", "Fiji", "Phuket", "Thailand"]
city = ["New York City", "USA", "Tokyo", "Japan", "London", "UK", "Paris", "France", "Dubai"]
if total_points <= 10 and total_points >= 1:
    print ( "based on your results you plan on going to more of an urban vacation with your friends and family. You want the climate to be a little bit more cooler and not spend to much money. This is a great vacation to save money. I would recoment doing to mnay places where you do not need to be to hot and can have a good feel for nature like")
    print (rural)
if total_points <= 20 and total_points >=11:
    print (" based on your results your vacation is similar to mnay vacation online. You have a good budget to go out of the country or close. The weather you would like is more neutra, but on the warmer type. I would recomend going tropical resorts like ")
    print (tropical)
if total_points <= 30 and total_points >=21:
    print("based on your selections I have concluded that your want to go to warmer resorts when you can really feel the heat. You are not afraid on a little heat and are willing to spend a good amount of money for a great vacation, I would recomend going to a city like ")
    print(city)
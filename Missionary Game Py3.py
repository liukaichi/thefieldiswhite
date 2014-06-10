import random
import time
import datetime


print ("<<<<<<Welcome to the Missionary Game!>>>>>")
class Person(object):
    """Has the attributes of a missionary"""
    def __init__(self, name, age, gender, convert, years_baptized, hobby):
        self.name = name        
        self.age = age
        self.gender = gender
        self.convert = convert
        self.years_baptized = years_baptized
        self.hobby = hobby
    
    def stats(faith, hope, charity, obedience, patience, knowledge, humility, spirit, endurance, charisma ):
        self.FTH = faith
        self.HOP = hope
        self.CHA = charity
        self.OBD = obedience
        self.PAT = patience
        self.KNW = knowledge
        self.HUM= humility
        self.SPR = spirit
        self.END= endurance
        self.CHR= charisma
    
    #Faith - main "attack" power of discussions. Influenced by obedience and study
    #Hope - more likely to receive random good things, such as referrals or gifts
    #Charity - Controls criticals and blocks
    #Obedience - Determined by certain rules/conditions the misisonary must follow. Doing so boosts his other stats.
    #Patience - Controls hit points
    #Knowledge - Determines how many scripture mastery you can memorize at one time
    #Humility - main "defense" power of disussions. Perhaps can also affect memorization/learning ability
    #Spirit - Gives you random tips/things to do according to the lvl of Spirit
    #Endurance - Perhaps some kind of physical limitation must be realized. You can go longer before eating lunch or something? Or you can go farther places because you don't get as tired.
    #Charisma - Changes likelihood of people stopping for you to initiate discussion.
        
    def skills(scripture_mastery, testify_topics, chat):
        self.scripture_mastery = script_mastery
        self.testify_topics = testify_topics
        self.chat = chat
        
    def print_stats(self):
        stats_list = {"Faith" : self.FTH, "Hope" : self.HOP, "Charity" : self.CHA, "Obedience" : self.OBD, "Patience" : self.PAT, "Knowledge" : self.KNW, "Humility" : self.HUM, "Spirit" : self.SPR, "Endurance" : self.END, "Charisma" : self.CHR}
        return stats_list    
        
class Potential(Person):
    """Potential Investigators need their own special stuff"""
    def conversion(interest, offense, trials, pride):
        
        self.interest = interest
        self.offense = offense
        self.trials = trials
        
hobby_list = ["Basketball", "Computers", "Music", "Art", "League of Legends"]
trial_list = ["Family Opposition", "Financial Need", "No Time", "Not interested"]
script_mastery_list = ["1 Ne 3:7", "Alma: 32:21", "2 Ne 8:3"]

def intro():
    #First determines gender/title
    response = False
    title = ""
    while response == False:
        gender = input("Are you Male of Female? (M/F): ")
        if gender == "M" or gender == "m":
            title = "Elder"
            break
        elif gender == "F" or gender == "f":
            title = "Sister"
            break
        else:
            response = False
    
    #asks last name, creates name combined with title                   
    response = False    
    while response == False:
        name = str("{}".format(title) + " " + input("What's your last name, {}? ".format(title)))
        if len(name) == 0:
            pass
        else:
            confirm_name = input ("You said " + name + ", was it? (y/n) ")
            if confirm_name == "Y" or confirm_name == "y":
                response = True
            elif confirm_name == "N" or confirm_name == "n":
                response = False
            else:
                print ("I'm sorry, can you respond with (y/n)?")
    print ("Hello, %s! thanks for trying out the missionary game!" % name)
    print ("So we need to ask you some questions before you can embark on your journey!")
 
    #This part determines Age
    eligible = False
    while eligible == False:
        age = int(input("How old are you?:"))
        if age < 18:
            print ("Wait, come again? Have you even graduated high school?")
            eligible = False
        elif age == 18:
            print ("A youngster, huh? Thanks for being willing to serve!")
            eligible = True
        elif age <= 27:
            print ("Thank you for being willing to serve!")
            eligible = True
        elif age > 27:
            print ("I'm sorry, you might be a little too old...")
            eligible = False
        else:
            pass
    
    #This part determines if they are a convert
    convert_confirm = False
    years_baptized_counter = 0
    while convert_confirm == False:
        convert = input("Are you a convert to the church?(y/n) ")
        if convert == "n":
            convert = False
            print ("That's wonderful! We're glad to have you here!")
            years_baptized_counter = age - 8
            break
        elif convert == "y":
            convert = True
            years_baptized_counter = int(input("How many years ago did you get baptized?"))
            print ("Wow!", end=" ")
            
            if years_baptized_counter == 1:
                print ("1 year, huh?"),
            elif years_baptized_counter < age - 8:
                print (str(years_baptized_counter) + " years? ", end="")
            print ("You'll bring a lot of fire to the mission for sure!")
           
            break
        else:
            print ("I'm sorry, can you respond with (y/n)?")
    #Choosing a hobby
    chosen = False
    while chosen is False:
        number_counter = 1       
        for choice in hobby_list:
            print (number_counter, choice)
            number_counter += 1
        hobby = int(input("So what do you like to do for fun?: (1-5)")) 
        if hobby > 5 or hobby < 1:
            print ("Can you say that again?")
            pass
        else:
            hobby = hobby_list[hobby-1]
            if len(hobby) > 0:
                chosen = True
    
    #This last part creates the character
    player = Person(name, age, gender, convert, years_baptized_counter, hobby)
    player.FTH = 5
    player.HOP = 5
    player.CHA= 5
    player.OBD = 5
    player.PAT= 5
    player.KNW = 5
    player.HUM = 5
    player.SPR = 5
    player.END = 5
    player.CHR = 5
    
    return player
player = intro()



#calculating beginning stats from intro() data. 
def calculate_stats(guy):
    #This is for age stats
    if guy.age == 18:
        guy.HOP += 2
        guy.KNW -= 1
        guy.HUM += 1
        guy.SPR -= 1
        guy.CHR += 1
       

    elif guy.age <= 21:
        guy.CHA += 1
        guy.KNW += 1
        guy.HUM -= 1
        guy.PAT += 1
        guy.CHR -= 1
        
        
    elif guy.age <= 28:
        guy.HOP -= 1
        guy.CHA += 1
        guy.PAT += 2
        guy.CHR -= 2
        guy.SPR += 1
        guy.END -= 1
        
    #This is for the converts stats
    if guy.years_baptized <= 3:        
        guy.FTH += 4 - guy.years_baptized
        guy.KNW -= 4 - guy.years_baptized
    elif guy.years_baptized <= 8:
        pass
    else:
        guy.FTH -= 1
        guy.KNW += 2
calculate_stats(player)

player_stats = player.print_stats()

for stat in player_stats:
    print (stat, player_stats[stat])




#Gameplay

def discuss():
    """Basic Gameplay Discussions"""
    street_guy = make_Potential()
    print ("You talk to someone on the street!")
    print ("They look like they are around", street_guy.age, "years old.")
    setup = False
    while setup == False:        
        print ("What will you do?")
        print ('A. Search your scriptures')
        print ('B. Discuss about the Gospel')
        print ('C. Testify Hardcore')
        print ('D. Let your companion speak')
        print ('E. Observe the investigator')
        print ('Q. Leave the seed to grow')
        print ("Player's Faith is", player.FTH, ", while other guy's offense is", street_guy.offense)
        response = input()
        if response == "A" or response == "a":
            if player.FTH > street_guy.offense:
                print("What scriptures do you want to use?")
                print(scripture_pool)
                return True
            else:
                print ("You planted a seed of faith!...but they left.")
                break
        elif response == "B" or response == "b":
            if player.FTH < street_guy.offense:
                print ("Yeah, they didn't seem interested anyway...")
                print ("Battle Won!")
            else:
                print ("You leave...but you feel that you should have stayed...")
                break
        else:
            pass
        
        
#NEEDS EDITING
def study(topic):
    pass

def make_Potential():
    """Makes a Potential for you to convert"""
    random_potential_list = ["Bobby", "Tommy", "Deeda", "Eugene", "Roz Encrantz"]
    creation_name = str(random_potential_list[random.randrange(0,5,1)])
    creation = Potential(creation_name, random.randrange(14,72,1), "Male", False, 0, hobby_list[random.randrange(0,5,1)])
    creation.interest = random.randrange(0,5,1)
    creation.offense = random.randrange(0,5,1)
    creation.trials = trial_list[random.randrange(0,4,1)]

  
    #Testing purposes:
    print ("My name is", creation.name)
    print ("I love", creation.hobby)
    print ("Right now my interest level is", creation.interest)
    print ("I am", creation.offense, "on the offended scale")
    print ("Right now I'm facing", creation.trials)

    if creation.hobby == player.hobby:
        creation.interest += 1
        print ("Whoa, you like", creation.hobby + ", too?")    
    return creation


#Day System
print ("Umm....so I forget, what day is today again?")
def set_date():
    correct_date = False    
    while correct_date == False:
        month, day, year = int(input("Month (MM): ")), int(input("Day (DD): ")), int(input("Year (YYYY): "))   
        if month == False or day == False or year == False:
            print ("Okay, this isn't very good")
            correct_date = False
        t = (year, month, day, 17, 3, 38, 1, 48, 0)
        t = time.mktime(t)
        confirm = input ("So you're saying today is " + time.strftime("%b %d %Y", time.gmtime(t)) + ", is that right? (y/n): ")
        if confirm == "y":
            correct_date = True
            print ("Wonderful. I'll remember that.")
        elif confirm == "n":
            print ("Oh, I'm sorry, I must have misheard you. What did you say?")
        else:
            print ("I'm sorry, can you respond with (y/n)?") 
        date = t      
        return date
t = set_date()
gmtime = time.gmtime(t)

day_counter = 1
number_of_converted = 0
setup = False
while day_counter <= 10:
    print ("<<<<<<<DAY", str(day_counter) + ">>>>>>>>", time.strftime("%b %d %Y", time.gmtime(t)))    
    print ()
    print ("A. Go Finding!")
    print ("B. Study!")
    print ("C. Sleep in...")
    print ("D. Visit some members!")
    response = input("It's bright and early! What will you do today? ")
    if response == "A" or response == "a":
        setup = discuss()
        if setup == True:
            number_of_converted += 1
        print ("So far you've converted {} people! Keep it up!".format(number_of_converted))
    elif response == "B" or response == "b":
        print ("So I guess we have a few things we can study...")
        print ("A. Stuff on Faith")
        print ("B. Stuff on Obedience")
        print ("C. Stuff on Humility")
        topic = input("So what do you want to study, then?")
        if topic == "A" or topic == "a":
            study(FTH)
        if topic == "B" or topic == "b":
            study(OBD)
        if topic == "C" or topic == "c":
            study(HUM)
    
    t += 86400.0 #This is how many seconds in one day. One epoch day passes.
    day_counter += 1
    
print ("Congrats! During your short-term mission you've converted {} people! You're awesome!".format(number_of_converted))




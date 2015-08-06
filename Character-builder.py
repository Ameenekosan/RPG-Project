print """You're about to create a new character
ready? yes/no"""
answer = raw_input()

print "\nwhat is the name of your character?"
caracter_name = raw_input()

print "\nWhat's your name?"
name = raw_input()

print "\nHow old are you?"
age = raw_input()

print "\nwhat is the color of your hair?"
hair_color = raw_input()

print "\nWhat is the color of your eyes?"
eye_color = raw_input()

genders = ['male','female']
while True:
    gender = raw_input("What is your gender ?").lower()
    if gender in genders:
        print "\nYour gender is:" + gender
        break
    print "\nSorry I could not understand you."

races = ['dwarves','elves','gnomes','half-elves','halflings','half-orcs','human']
while True :
    print """The races are :
    [Dwarves,Elves,Gnomes,Half-Elves,Halflings,Half-Orcs,Human]"""
    race = raw_input("what is your race?").lower()
    if race in races:
        print "\nYour race is :" + race
        break
    print "\nSorry I could not understand you."


classes = [ "barbarian","bard","cleric","fighter",
            "monk","paladin", "ranger","rogue",
            "sorcerer","wizard"]
while True:
    print "\nThe classes are :"
    print "[Barbarian,Bard,Cleric,Druid,Fighter,Monk,Paladin,Ranger,Rogue,\
        Sorcerer,Wizard]"
    classe = raw_input("What is your class?").lower()
    if classe in classes:
        print "\nYour classe is:" + classe
        break
    print "\nSorry I could not understand you."

alignments = [ 'lawful good','neutral good','chaotic good','lawful neutral',
            'neutral','chaotic neutral','lawful evil','neutral evil',
            'chaotic evil']
while True:
    print "\nThe Alignments are :"
    print "[Lawful Good,Neutral Good,Chaotic Good,Lawful Neutral,Neutral,\
    Chaotic Neutral,Lawful Evil,Neutral Evil,Chaotic Evil]"
    alignment = raw_input("What is your alignment?").lower()
    if alignment in alignments:
        print "\nYour alignment is:" + alignment
        break
    print "\nSorry I could not understand you."


sizes = ['small','medium','large']
while True:
    size = raw_input("what is your size ?(Small,Medium,large?)").lower()
    if size in sizes:
        print "\nYour size is:" + size
        break
    print "\nSorry I could not understand you."

import random
def roll_ability_score():
    return random.randint(1,6) + random.randint(1,6) + random.randint(1,6)

print """ Each character has six ability scores that represent \
his character's most basic attributes. They are his raw talent and prowess.\
While a character rarely rolls a check using just an ability score, these scores,\
and the modifiers they create, affect nearly every aspect of a character's \
skills and abilities. Each ability score generally ranges from 3 to 18, \
although racial bonuses and penalties can alter this; an average ability score is 10.
\nTo do so , Here are 6 random numbers. Put each number to the appropriate \
ability for your character. Choose wisely !"""

for x in range(0, 6):
    print roll_ability_score()

Strength = int(raw_input("Enter Strength score here :"))
Dexterity = int(raw_input("Enter Dexterity score here :"))
Constitution = int(raw_input("Enter Constitution score here :"))
Intelligence = int(raw_input("Enter Intelligence score here :"))
Wisdom = int(raw_input("Enter Wisdom score here :"))
Charisma = int(raw_input("Enter Charisma score here :"))

#print race
if race == "dwarves":
    aStr_modifier = 0
    aDex_modifier = 0
    aCon_modifier = 2
    aInt_modifier = 0
    aWis_modifier = 2
    aCha_modifier = - 2

    if  gender == "male":
        base_height_male = 3 * 12 + 9 + (random.randint(1,4)) + (random.randint(1,4))
        base_weight_male = 150 + 7 * ((random.randint(1,8)) + (random.randint(1,8)))
        print "\nYour character is %r inches tall and it's weight is %r pounds" %(base_height_male, base_weight_male)

    elif gender == "female":
        base_height_female = 3 * 12 + 7 + (random.randint(1,4)) + (random.randint(1,4))
        base_weight_female = 120 + 7 * ((random.randint(1,8)) + (random.randint(1,8)))
        print "\nYour character is %r inches tall and it's weight is %r pounds." %(base_height_female, base_weight_female)

    STR = Strength + aStr_modifier
    DEX = Dexterity + aDex_modifier
    CON = Constitution + aCon_modifier
    INT = Intelligence + aInt_modifier
    WIS = Wisdom + aWis_modifier
    CHA = Charisma + aCha_modifier

    print "\nStrenght: %d" %(STR)
    print "Dexterity: %d" %(DEX)
    print "Constitution: %d" %(CON)
    print "Intelligence: %d" %(INT)
    print "Wisdom: %d" %(WIS)
    print "Charisma: %d" %(CHA)

#print race
if race == "elves":
    bStr_modifier = 0
    bDex_modifier = 2
    bCon_modifier = - 2
    bInt_modifier = 2
    bWis_modifier = 0
    bCha_modifier = 0

    if  gender == "male":
        bbase_height_male = 5 * 12 + 4 + (random.randint(1,8)) + (random.randint(1,8))
        bbase_weight_male = 110 + 3 * ((random.randint(1,8)) + (random.randint(1,8)))
        print "\nYour character is %r inches tall and it's weight is %r pounds" %(bbase_height_male, bbase_weight_male)

    elif gender == "female":
        bbase_height_female = 5 * 12 + 4 + (random.randint(1,6)) + (random.randint(1,6))
        bbase_weight_female = 90 + 3 * ((random.randint(1,6)) + (random.randint(1,6)))
        print "\nYour character is %r inches tall and it's weight is %r pounds." %(bbase_height_female, bbase_weight_female)

    STR = Strength + bStr_modifier
    DEX = Dexterity + bDex_modifier
    CON = Constitution + bCon_modifier
    INT = Intelligence + bInt_modifier
    WIS = Wisdom + bWis_modifier
    CHA = Charisma + bCha_modifier

    print "\nStrenght: %d" %(STR)
    print "Dexterity: %d" %(DEX)
    print "Constitution: %d" %(CON)
    print "Intelligence: %d" %(INT)
    print "Wisdom: %d" %(WIS)
    print "Charisma: %d" %(CHA)

#race_3 = Gnomes
if race == "gnomes":
    cStr_modifier = - 2
    cDex_modifier = 0
    cCon_modifier = 2
    cInt_modifier = 0
    cWis_modifier = 0
    cCha_modifier = 2

    if  gender == "male":
        cbase_height_male = 3 * 12 + (random.randint(1,4)) + (random.randint(1,4))
        cbase_weight_male = 35 + ((random.randint(1,4)) + (random.randint(1,4)))
        print "\nYour character is %r inches tall and it's weight is %r pounds" %(cbase_height_male, cbase_weight_male)

    if gender == "female":
        cbase_height_female = 2 * 12 + 10 + (random.randint(1,4)) + (random.randint(1,4))
        cbase_weight_female = 30 + ((random.randint(1,4)) + (random.randint(1,4)))
        print "\nYour character is %r inches tall and it's weight is %r pounds." %(cbase_height_female, cbase_weight_female)

    STR = Strength + cStr_modifier
    DEX = Dexterity + cDex_modifier
    CON = Constitution + cCon_modifier
    INT = Intelligence + cInt_modifier
    WIS = Wisdom + cWis_modifier
    CHA = Charisma + cCha_modifier

    print "\nStrenght: %d" %(STR)
    print "Dexterity: %d" %(DEX)
    print "Constitution: %d" %(CON)
    print "Intelligence: %d" %(INT)
    print "Wisdom: %d" %(WIS)
    print "Charisma: %d" %(CHA)

#race_4 = Half-Elves
if race == "half-elves":
    dStr_modifier = 0
    dDex_modifier = 2
    dCon_modifier = 0
    dInt_modifier = 0
    dWis_modifier = 0
    dCha_modifier = 0

    if  gender == "male":
        dbase_height_male = 5 * 12 + 2 + (random.randint(1,8)) + (random.randint(1,8))
        dbase_weight_male = 100 + 5 * ((random.randint(1,8)) + (random.randint(1,8)))
        print "\nYour character is %r inches tall and it's weight is %r pounds" %(dbase_height_male, dbase_weight_male)

    if gender == "female":
        dbase_height_female = 5 * 12 + (random.randint(1,8)) + (random.randint(1,8))
        dbase_weight_female = 90 + 5 * ((random.randint(1,8)) + (random.randint(1,8)))
        print "\nYour character is %r inches tall and it's weight is %r pounds." %(dbase_height_female, dbase_weight_female)

    STR = Strength + dStr_modifier
    DEX = Dexterity + dDex_modifier
    CON = Constitution + dCon_modifier
    INT = Intelligence + dInt_modifier
    WIS = Wisdom + dWis_modifier
    CHA = Charisma + dCha_modifier

    print "\nStrenght: %d" %(STR)
    print "Dexterity: %d" %(DEX)
    print "Constitution: %d" %(CON)
    print "Intelligence: %d" %(INT)
    print "Wisdom: %d" %(WIS)
    print "Charisma: %d" %(CHA)

#race_5 = Halflings
if race == "halflings":
    eStr_modifier = - 2
    eDex_modifier = 2
    eCon_modifier = 0
    eInt_modifier = 0
    eWis_modifier = 0
    eCha_modifier = 2

    if  gender == "male":
        ebase_height_male = 2 * 12 + 8 + (random.randint(1,4)) + (random.randint(1,4))
        ebase_weight_male = 30 + ((random.randint(1,8)) + (random.randint(1,8)))
        print "\nYour character is %r inches tall and it's weight is %r pounds" %(ebase_height_male, ebase_weight_male)

    if gender == "female":
        ebase_height_female = 2 * 12 + 6 * (random.randint(1,4)) + (random.randint(1,4))
        ebase_weight_female = 25 + ((random.randint(1,4)) + (random.randint(1,4)))
        print "\nYour character is %r inches tall and it's weight is %r pounds." %(ebase_height_female, ebase_weight_female)

    STR = Strength + eStr_modifier
    DEX = Dexterity + eDex_modifier
    CON = Constitution + eCon_modifier
    INT = Intelligence + eInt_modifier
    WIS = Wisdom + eWis_modifier
    CHA = Charisma + eCha_modifier

    print "\nStrenght: %d" %(STR)
    print "Dexterity: %d" %(DEX)
    print "Constitution: %d" %(CON)
    print "Intelligence: %d" %(INT)
    print "Wisdom: %d" %(WIS)
    print "Charisma: %d" %(CHA)

#race_6 = Half-Orcs
if race == "half-orcs":
    fStr_modifier = 2
    fDex_modifier = 0
    fCon_modifier = 0
    fInt_modifier = 0
    fWis_modifier = 0
    fCha_modifier = 0

    if  gender == "male":
        fbase_height_male = 4 * 12 + 10 + (random.randint(1,12)) + (random.randint(1,12))
        fbase_weight_male = 150 + 7 * ((random.randint(1,12)) + (random.randint(1,12)))
        print "\nYour character is %r inches tall and it's weight is %r pounds" %(fbase_height_male, fbase_weight_male)

    if gender == "female":
        fbase_height_female = 4 * 12 + 5 + (random.randint(1,12)) + (random.randint(1,12))
        fbase_weight_female = 110 + 7 * ((random.randint(1,12)) + (random.randint(1,12)))
        print "\nYour character is %r inches tall and it's weight is %r pounds." %(fbase_height_female, fbase_weight_female)
    STR = Strength + fStr_modifier
    DEX = Dexterity + fDex_modifier
    CON = Constitution + fCon_modifier
    INT = Intelligence + fInt_modifier
    WIS = Wisdom + fWis_modifier
    CHA = Charisma + fCha_modifier

    print "\nStrenght: %d" %(STR)
    print "Dexterity: %d" %(DEX)
    print "Constitution: %d" %(CON)
    print "Intelligence: %d" %(INT)
    print "Wisdom: %d" %(WIS)
    print "Charisma: %d" %(CHA)
#race_7 = Human
if race == "humans":
    gStr_modifier = 0
    gDex_modifier = 0
    gCon_modifier = 0
    gInt_modifier = 0
    gWis_modifier = 0
    gCha_modifier = 0

    if  gender == "male":
        gbase_height_male = 4 * 12 + 10 + (random.randint(1,10)) + (random.randint(1,10))
        gbase_weight_male = 120 + 5 * ((random.randint(1,10)) + (random.randint(1,10)))
        print "\nYour character is %r inches tall and it's weight is %r pounds" %(gbase_height_male, gbase_weight_male)

    if gender == "female":
        gbase_height_female = 4 * 12 + 5 + (random.randint(1,10)) + (random.randint(1,10))
        gbase_weight_female = 85 + 5 * ((random.randint(1,10)) + (random.randint(1,10)))
        print "\nYour character is %r inches tall and it's weight is %r pounds." %(gbase_height_female, gbase_weight_female)

    STR = Strength + gStr_modifier
    DEX = Dexterity + gDex_modifier
    CON = Constitution + gCon_modifier
    INT = Intelligence + gInt_modifier
    WIS = Wisdom + gWis_modifier
    CHA = Charisma + gCha_modifier

    print "\nStrenght: %d" %(STR)
    print "Dexterity: %d" %(DEX)
    print "Constitution: %d" %(CON)
    print "Intelligence: %d" %(INT)
    print "Wisdom: %d" %(WIS)
    print "Charisma: %d" %(CHA)

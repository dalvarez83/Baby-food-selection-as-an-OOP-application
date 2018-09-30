""" Project Title: Choosing Foods for a Happy Baby
    Author: Daniel Alvarez
    Date: July 2018
    Class: MIDS-W200-Summer2018
"""
"""
Description:
For this project, I will build a baby food menu whereby each food item on the
menu triggers a response from the baby. Some food is agreeable, some food is
sometimes agreeable and some food is just disagreeable to the baby. You are
the parent trying to feed the baby a varied menu of foods over the course of
a day (breakfast, lunch and dinner). You will encounter that the baby will find
some foods agreeable when mixed with certain other foods, yet may sometimes find
the same foods disagreeable when mixed with other foods. Objects will be the
food items on the menu and responses to those foods. The goal is to choose the
right set of foods to have a happy baby at the end of the day.
"""

""" Import libraries and packages """
import sys
import random

### Main program
print('\nHello, Welcome parent!')
print('\nYou are presented with a menu of food options to feed your baby')
print('\nEach food item on its own solicits a different response from your baby (agreeable, maybe agreeable, disagreeable)')
print('\nEach food item can be mixed with another food item that may solicit a different response from your baby after each meal.')
print('\nYou cannot feed the baby the same food item within the same day. Want a varied food menu for your baby.')
print('\nThe goal is to be creative with your food menu for your baby without soliciting disagreeable responses.')


### Prompt
if __name__ == "__main__":
    #Initialization
    print("Welcome to 'Choosing Foods for a Happy Baby'\n")
    while True:
        cmd = input("Please enter [b] to enter your [b]aby's details, or [q] to [q]uit the application or [h] for [h]elp\n")
        if cmd == "h":
            print("[b]aby - enter your baby information details")
            print("[q]uit - close the application")
        elif cmd == "baby" or cmd=="b":
            #Enter identifying information for you and your baby
            name = input("Enter your baby's name:\n")
            weight = input("Enter your baby's weight (in lbs):\n")
            print("...\n")
            print("It is time to start feeding " + name)
            break
        elif cmd == "quit" or cmd =="q":
            sys.exit()

# dictionary of all possible foods for baby with associated agreeability values for baby
dict_of_foods = {"bananas":3, "plain yogurt":3, "cheese":3, "puffs":3, "bread":2, "puffs":3,
                "peas":3, "cheerios":3, "eggs":3, "peeled grapes":3, "hummus":3, "oatmeal with peanut butter":3,
                "pasta with cheese":3, "apples with broccoli":2, "sweet potatoes":2, "pears":2,
                "oatmeal":2, "carrots":2, "oranges":2, "avocado":2, "carrots":2, "flavored yogurt":2,
                "pasta without cheese": 2, "apples":1, "mangos":1, "fish":1, "green beans":1, "meat":1,
                "chicken":1, "cantaloupe":1, "blueberries":1, "beets":1, "broccoli":1}

# Lists of different meal types

breakfast = ["bananas","plain yogurt","cheerios","peeled grapes","oatmeal with peanut butter","pears","oatmeal","oranges","flavored yogurt","apples","strawberries","blueberries"]
lunch = ["cheese","bread","puffs","peas","eggs","hummus","pasta with cheese","apples with broccoli","avocado","green beans","meat","chicken","sweet potatoes"]
dinner = ["pasta without cheese","mangos","fish","cantaloupe","beets","broccoli","hummus","peas","plain yogurt","pears","peeled grapes","green beans"]
allmeals = ["bananas","plain yogurt","cheerios","peeled grapes","oatmeal with peanut butter","pears","oatmeal","oranges","flavored yogurt","apples","strawberries","blueberries",
            "cheese","bread","puffs","peas","eggs","hummus","pasta with cheese","apples with broccoli","avocado","green beans","meat","chicken","sweet potatoes",
            "pasta without cheese","mangos","fish","cantaloupe","beets","broccoli","hummus","peas","plain yogurt","pears","peeled grapes","green beans"]

# Dictionary of food qualities for each baby food item that inform the baby's reaction to the food
    # Assign values from 1 (lowest) to 5 (highest) for each foodquality
bananas = {"food":"bananas", "sweet":5,"sour":1,"soft":4,"chewy":2,"foul":1,"breakfast":"Yes","lunch":"No","dinner":"Yes"}
plainyogurt = {"food":"plain yogurt", "sweet":2,"sour":4,"soft":5,"chewy":1,"foul":1,"breakfast":"Yes","lunch":"No","dinner":"Yes"}
cheese = {"food":"cheese", "sweet":3,"sour":2,"soft":3,"chewy":2,"foul":1,"breakfast":"No","lunch":"Yes","dinner":"No"}
bread = {"food":"bread", "sweet":1,"sour":1,"soft":3,"chewy":4,"foul":1,"breakfast":"No","lunch":"Yes","dinner":"No"}
puffs = {"food":"puffs", "sweet":2,"sour":1,"soft":1,"chewy":5,"foul":1,"breakfast":"No","lunch":"Yes","dinner":"No"}
peas = {"food":"peas", "sweet":3,"sour":1,"soft":2,"chewy":4,"foul":1,"breakfast":"No","lunch":"Yes","dinner":"Yes"}
cheerios = {"food":"cheerios", "sweet":2,"sour":1,"soft":1,"chewy":5,"foul":1,"breakfast":"Yes","lunch":"No","dinner":"No"}
eggs = {"food":"eggs", "sweet":1,"sour":1,"soft":4,"chewy":3,"foul":1,"breakfast":"No","lunch":"Yes","dinner":"No"}
peeledgrapes = {"food":"peeled grapes", "sweet":5,"sour":1,"soft":2,"chewy":2,"foul":1,"breakfast":"Yes","lunch":"No","dinner":"Yes"}
hummus = {"food":"hummus", "sweet":1,"sour":1,"soft":5,"chewy":1,"foul":1,"breakfast":"No","lunch":"Yes","dinner":"Yes"}
oatmealwithpeanutbutter = {"food":"oatmeal with peanut butter", "sweet":3,"sour":1,"soft":5,"chewy":2,"foul":1,"breakfast":"Yes","lunch":"No","dinner":"No"}
pastawithcheese = {"food":"pasta with cheese", "sweet":1,"sour":1,"soft":1,"chewy":5,"foul":1,"breakfast":"No","lunch":"Yes","dinner":"No"}
sweetpotatoes = {"food":"sweet potatoes", "sweet":3,"sour":1,"soft":4,"chewy":3,"foul":1,"breakfast":"No","lunch":"Yes","dinner":"No"}
pears = {"food":"pears", "sweet":5,"sour":1,"soft":3,"chewy":3,"foul":1,"breakfast":"Yes","lunch":"No","dinner":"Yes"}
oatmeal = {"food":"oatmeal", "sweet":1,"sour":1,"soft":5,"chewy":1,"foul":1,"breakfast":"Yes","lunch":"No","dinner":"No"}
carrots = {"food":"carrots", "sweet":3,"sour":1,"soft":1,"chewy":5,"foul":1,"breakfast":"No","lunch":"Yes","dinner":"No"}
oranges = {"food":"oranges", "sweet":5,"sour":1,"soft":2,"chewy":3,"foul":1,"breakfast":"Yes","lunch":"No","dinner":"No"}
avocado = {"food":"avocado", "sweet":2,"sour":1,"soft":4,"chewy":2,"foul":1,"breakfast":"No","lunch":"Yes","dinner":"No"}
flavoredyogurt = {"food":"flavored yogurt", "sweet":3,"sour":3,"soft":5,"chewy":1,"foul":1,"breakfast":"Yes","lunch":"No","dinner":"No"}
pastawithoutcheese = {"food":"pasta without cheese", "sweet":1,"sour":1,"soft":1,"chewy":5,"foul":1,"breakfast":"No","lunch":"No","dinner":"Yes"}
apples = {"food":"apples", "sweet":5,"sour":1,"soft":5,"chewy":1,"foul":1,"breakfast":"Yes","lunch":"No","dinner":"No"}
mangos = {"food":"mangos", "sweet":3,"sour":3,"soft":3,"chewy":3,"foul":1,"breakfast":"No","lunch":"No","dinner":"Yes"}
fish = {"food":"fish", "sweet":1,"sour":1,"soft":4,"chewy":2,"foul":4,"breakfast":"No","lunch":"No","dinner":"Yes"}
greenbeans = {"food":"green beans", "sweet":1,"sour":3,"soft":2,"chewy":4,"foul":3,"breakfast":"No","lunch":"Yes","dinner":"Yes"}
meat = {"food":"meat", "sweet":1,"sour":1,"soft":2,"chewy":3,"foul":1,"breakfast":"No","lunch":"Yes","dinner":"No"}
chicken = {"food":"chicken", "sweet":1,"sour":1,"soft":2,"chewy":3,"foul":1,"breakfast":"No","lunch":"Yes","dinner":"No"}
cantaloupe = {"food":"cantaloupe", "sweet":5,"sour":1,"soft":3,"chewy":3,"foul":1,"breakfast":"No","lunch":"No","dinner":"Yes"}
strawberries = {"food":"strawberries", "sweet":5,"sour":1,"soft":3,"chewy":3,"foul":1,"breakfast":"Yes","lunch":"No","dinner":"No"}
beets = {"food":"beets", "sweet":3,"sour":3,"soft":2,"chewy":4,"foul":1,"breakfast":"No","lunch":"No","dinner":"Yes"}
broccoli = {"food":"broccoli", "sweet":1,"sour":2,"soft":3,"chewy":4,"foul":1,"breakfast":"No","lunch":"No","dinner":"Yes"}


# Define the base class for baby meals

class BabyMeals():

    def __init__(self, meal, foodselected):
        """ Generates the food menu for the particular meal """
        self.meal = meal
        self.allmeals = allmeals
        self.foodselected = foodselected

    def __food__(self):
        """ Renders the menu of foods available to the screen """
        print(self.meal)
        return

    def __repr__(self):
        """ Print the menu of foods nicely """
        return " ".join(str(x) for x in self.meal)

    def get_food(self):
        """ Returns the food item selected by the user """
        return self.foodselected

    def remove_from_menu(self):
        """ Removes the food item selected from the foods available """
        self.meal.remove(self.foodselected)
        self.allmeals.remove(self.foodselected)
        print(self.foodselected + " removed from the available foods on the baby food menu")
        return

    def set_food(self, foodselected):
        """ Raises exception if food chosen is not among the available foods on the menu
            or if two foods have not been chosen"""
        self.foodselected = foodselected
        if self.foodselected not in self.meal:
            raise Exception ("Sorry, food selected is not among the available foods on the menu. Choose another food item.")
            print("Sorry, food selected is not among the available foods on the menu. Choose another food item.")
        else:
            print("Good choice, "+ self.foodselected + " is among the available food items on the menu.")
            return

 # Define class for baby response upon serving meals

class ServeMeal:
    """ This class displays the baby's emotional response to the meal selected"""

    def __init__(self, meal, fooditem1, fooditem2):
        self.meal = meal
        self.fooditem1 = fooditem1
        self.fooditem2 = fooditem2
        self.dict_of_foods = {"bananas":3, "plain yogurt":3, "cheese":3, "puffs":3, "bread":2, "puffs":3,
                    "peas":3, "cheerios":3, "eggs":3, "peeled grapes":3, "hummus":3, "oatmeal with peanut butter":3,
                    "pasta with cheese":3, "apples with broccoli":2, "sweet potatoes":2, "pears":2,
                    "oatmeal":2, "carrots":2, "oranges":2, "avocado":2, "carrots":2, "flavored yogurt":2,
                    "pasta without cheese": 2, "apples":1, "mangos":1, "fish":1, "green beans":1, "meat":1,
                    "chicken":1, "cantaloupe":1, "blueberries":1, "beets":1, "broccoli":1}

    def emotion(self):
        """ Returns whether the two food items selected in combination are agreeable, maybe agreeable or disagreeable"""

        # initiate an empty dictionary to add selected food items to
        self.foodselected = {}

        # Add food items to empty dictionary
        if self.fooditem1 in self.dict_of_foods:
            self.foodselected.get(self.fooditem1)
            self.foodselected[self.fooditem1]=self.dict_of_foods[self.fooditem1]
        if self.fooditem2 in self.dict_of_foods:
            self.foodselected.get(self.fooditem2)
            self.foodselected[self.fooditem2]=self.dict_of_foods[self.fooditem2]

        self.foodresponse = sum(self.foodselected.values())

        if sum(self.foodselected.values()) > 4:
            babyreaction = "Agreeable"
        elif sum(self.foodselected.values()) == 4:
            babyreaction = "Maybe Agreeable"
        else:
            babyreaction = "Disagreeable"
        return babyreaction

    def emotion_message_to_parent(self):
        """ Returns message to user 'Happy baby' or 'Unhappy baby' """
        if sum(self.foodselected.values()) > 4:
            print("Happy baby!")
        elif sum(self.foodselected.values()) == 4:
            print("Perhaps happy baby or perhaps not!")
        else:
            print("Unhappy baby!")
        return

# Produces a message for parent for whether food item chosen is or is not in the menu

class Foodsavailable():
    """ This class tells the parent is foods are available to create baby meals """

    def __init__(self, meal, fooditem1, fooditem2):
        self.meal = meal
        self.fooditem1 = fooditem1
        self.fooditem2 = fooditem2

    def message_to_parent(self):
        """ Produces message for parent if food item chosen is not in the menu for the given meal """
        if self.fooditem1 not in self.meal:
            print("Cannot choose " + self.fooditem1 + " It is not an available food for your baby!")
            return

        elif self.fooditem2 not in self.meal:
            print("Cannot choose " + self.fooditem2 + " It is not an available food for your baby!")
            return
        else:
            print("Congrats. Both " + self.fooditem1 + " and " + self.fooditem2 + " are available meal food items for your baby.")
            return

    def __repr__(self):
        return (str(self.fooditem1) + ' and '+ str(self.fooditem2)+ ' chosen')

""" Define classes for food qualities """

class FoodQualities():
    """ This class assigns food qualities to food items """

    def __init__(self, fooditem):
        self._fooditem = fooditem.get("food")
        self._sweet = fooditem.get("sweet")
        self._sour = fooditem.get("sour")
        self._soft = fooditem.get("soft")
        self._chewy = fooditem.get("chewy")
        self._foul = fooditem.get("foul")
        self._breakfast = fooditem.get("breakfast")
        self._lunch = fooditem.get("lunch")
        self._dinner = fooditem.get("dinner")

    def get_fooditem(self):
        return self._fooditem

    def get_sweet(self):
        return self._sweet

    def get_sour(self):
        return self._sour

    def get_soft(self):
        return self._soft

    def get_chewy(self):
        return self._chewy

    def get_foul(self):
        return self._foul

    def get_breakfast(self):
        return self._breakfast

    def get_lunch(self):
        return self._lunch

    def get_dinner(self):
        return self._dinner

    def __str__(self):
        return "FOOD ITEM: {}\nsweet: {}\nsour: {}\nsoft: {}\nchewy: {}\nfoul: {} \nbreakfast: {} \nlunch: {} \ndinner: {}"\
            .format(self._fooditem, self._sweet, self._sour, self._soft, self._chewy, self._foul, self._breakfast, self._lunch, self._dinner)

################################################################################
""" Secondary main prompt that gets initiated once the parent user has entered in
    the baby's details """

if __name__ == "__main__":
    while True:
    #Initialization
        if name != None and weight != None:
            # Prompt parent to enter first food
            print("Here are the available foods for breakfast for " + name + ":")
            print(breakfast)

            foodselected1 = input("Please enter a single food item from the available menu items for " + name + "'s breakfast:\n")
            parentchoice1 = BabyMeals(breakfast,str(foodselected1))
            print("You have selected " + foodselected1 + " for " + name)
            print("\n")

            # Tell parent that item has been removed from the menu
            parentchoice1.remove_from_menu()

            # Tells parent of foods available on the menu
            print("Here are the menu of foods available for breakfast: ")
            parentchoice1.__food__()

            # Tells parent to enter second food
            foodselected2 = input("Please enter a second food item selection for " + name + "'s breakfast:\n")
            parentchoice1 = BabyMeals(breakfast,str(foodselected2))
            print("You have selected " + foodselected2)
            print("\n")

            # Tells parent if food item is among the available foods on the menu
            parentchoice1.set_food(str(foodselected2))

            # Tell parent that second food item has been removed from the menu
            parentchoice1.remove_from_menu()
            print("")
            # Tells parent of baby's reaction to food's chosen
            breakfastchoice = ServeMeal(breakfast,str(foodselected1),str(foodselected2))
            print("Your breakfast food selection was " + breakfastchoice.emotion() + " with " + name + "\n")


            print("After breakfast you have a: ")
            breakfastchoice.emotion_message_to_parent()

            ######################################################################
            # Now time to move onto lunch. Iterate same steps as above for breakfast
            print("\nIt is now time to feed " + name + " lunch.\n")

            # Prompt parent to enter first food for lunch
            print("Here are the available foods for lunch for " + name + ":")
            print(lunch)

            foodselected3 = input("Please enter a single food item from the available menu items for " + name + "'s lunch:\n")
            parentchoice3 = BabyMeals(lunch,str(foodselected3))
            print("You have selected " + foodselected3 + " for " + name)
            print("\n")

            # Tell parent that item has been removed from the menu
            parentchoice3.remove_from_menu()

            # Tells parent of foods available on the menu
            print("Here are the menu of foods available for lunch: ")
            parentchoice3.__food__()

            # Tells parent to enter second food
            foodselected4 = input("Please enter a second food item selection for " + name + "'s lunch:\n")
            parentchoice4 = BabyMeals(lunch,str(foodselected4))
            print("You have selected " + foodselected4)
            print("\n")

            # Tells parent if food item is among the available foods on the menu
            parentchoice4.set_food(str(foodselected4))

            # Tell parent that second food item has been removed from the menu
            parentchoice4.remove_from_menu()
            print("")
            # Tells parent of baby's reaction to food's chosen
            lunchchoice = ServeMeal(lunch,str(foodselected3),str(foodselected4))
            print("Your lunch food selection was " + lunchchoice.emotion() + " with " + name + "\n")


            print("After lunch you have a: ")
            lunchchoice.emotion_message_to_parent()

            ######################################################################
            # Now time to move onto dinner. Iterate same steps as above for breakfast
            print("\nIt is now time to feed " + name + " dinner.\n")

            # Prompt parent to enter first food for lunch
            print("Here are the available foods for dinner for " + name + ":")
            print(dinner)

            foodselected5 = input("Please enter a single food item from the available menu items for " + name + "'s dinner:\n")
            parentchoice5 = BabyMeals(dinner,str(foodselected5))
            print("You have selected " + foodselected5 + " for " + name)
            print("\n")

            # Tell parent that item has been removed from the menu
            parentchoice5.remove_from_menu()

            # Tells parent of foods available on the menu
            print("Here are the menu of foods available for dinner: ")
            parentchoice5.__food__()

            # Tells parent to enter second food
            foodselected6 = input("Please enter a second food item selection for " + name + "'s dinner:\n")
            parentchoice6 = BabyMeals(dinner,str(foodselected6))
            print("You have selected " + foodselected6)
            print("\n")

            # Tells parent if food item is among the available foods on the menu
            parentchoice6.set_food(str(foodselected6))

            # Tell parent that second food item has been removed from the menu
            parentchoice6.remove_from_menu()
            print("")
            # Tells parent of baby's reaction to food's chosen
            dinnerchoice = ServeMeal(dinner,str(foodselected5),str(foodselected6))
            print("Your dinner food selection was " + dinnerchoice.emotion() + " with " + name + "\n")


            print("After dinner you have a: ")
            dinnerchoice.emotion_message_to_parent()

            #######################################################################
            # Tell parent end of day message after all three meals have been served
            print("\nYour end of day message is: ")
            if breakfastchoice.emotion_message_to_parent() == "Happy baby!" and lunchchoice.emotion_message_to_parent() == "Happy baby!" and dinnerchoice.emotion_message_to_parent() == "Happy baby!":
                print("Congratulations you have a happy baby! Good luck feeding tomorrow!")
            else:
                print("Sorry, you have an unhappy baby! Better luck feeding tomorrow!")

            ######################################################################

            break

        else:
            cmd = input("Please enter your [b]aby's details, [q]uit the application of 'h' for help\n")

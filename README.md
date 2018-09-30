# Baby-food-selection-as-an-OOP-application

DESCRIPTION:
For this project, I will build a baby food menu whereby each food item on the
menu triggers a response from the baby. Some food is agreeable, some food is
sometime agreeable and some food is just disagreeable to the baby. You are the
parent trying to feed the baby a varied menu of foods over the course of a day
(breakfast, lunch and dinner). You will encounter that the baby will find some
foods agreeable when mixed with certain other foods, yet may sometimes find
the same foods disagreeable when mixed with other foods. Objects will be the
food items on the menu and responses to those foods. The goal is to choose the
right set of foods to have a happy baby at the end of the day.

FEATURES:
• You are presented with a menu of food options to feed your baby

• Each food item on its own solicits a different response from your baby
(agreeable, maybe agreeable, disagreeable)

• Each food item can be mixed with another food item that may solicit a
different response from your baby.

• You need to feed the baby two different items at each of the three
feedings of the day (breakfast, lunch and dinner).

• You cannot feed the baby the same food item within the same day. Want
a varied food menu for your baby. However, baby does like similar
types of foods (sweet, sour, soft, chewy, but never foul).

• The goal is to be creative with your food menu for your baby without
soliciting disagreeable responses. Don’t want unhappy baby!

• Parent can use “q” to quit and “h” for help at any point of the game.

The baby food game could go as follows:
1. Feeding: Breakfast
Choose first food item from menu: plain yogurt
Baby response to first food item from menu: Agreeable
Choose second food item from the menu: carrots
Baby response to first food item from menu: Agreeable
Return result to parent: Happy baby!

2. Feeding: Lunch
Message: Cannot choose plain yogurt, carrots
Choose first food item from menu: Cheese
Baby response to first food item from menu: Agreeable
Choose second food item from the menu: Pasta
Baby response to first food item from menu: Agreeable
Return result to parent: Happy baby!

3. Feeding: Dinner
Message: Cannot choose plain yogurt, carrots, cheese, pasta
Choose first food item from menu: Sweet potatoes
Baby response to first food item from menu: Maybe agreeable
Choose second food item from the menu: Apples
Baby response to first food item from menu: Disagreeable
Return result to parent: Unhappy baby!
Message: Sorry you have an unhappy baby! Better luck feeding tomorrow!

DESIGN
The baby feeding game is thought of a parent taking actions through a series of
feeding time nodes, whereby each feeding time affects the next by limiting the
food item set.
Each feeding time node (breakfast, lunch and dinner) prompts the user (the
parent) for an action (the food item). Each action, including the food and
response classes and mixing attributes of each food affects the response from
the baby.
The classes are foods particular to feeding time nodes (breakfast, lunch and
dinner). The particular foods are attributes and may or may not be mutually
exclusive to each feeding time node. The functions for each class output to the
user whether the food selected in agreeable, maybe agreeable or disagreeable
based on the attributes of the foods. A final method returns the
message_to_parent which tells parent if (s)he has a happy baby.

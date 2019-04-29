"""

This program contains the simulation of the extended Combat game.
It is an extension of the basic game with two advancements of Medics and
Expanded armies respectively.

The code contains two major functions, as briefly explained below:

1. get_team(amount_rem): This function has been made generic enough to create
any team given their remaining balance which is passed as an argument. The
function asks for the choices to the players to choose from (Archer, Knight,
Soldier, Siege and Wizard).

2.  combat_logic( army1, army2, amount1, amount2) : This function implements
the combat logic when each unit of first player fights against the unit of
player 2. The Medics part is also very smartly taken care by a minor modification
in this function itself. Check the comments in the function to see the implementation
of Medics.

"""


# Following are the variables for all the units possible in the army.
archer = "Archer"
knight = "Knight"
soldier = "Soldier"
siege = "Siege"
wizard = "Wizard"

# This dictionary maintains the cost of each unit.
cost_unit = {archer: 1, knight: 1, soldier: 1, siege: 2, wizard: 3}


# Variables to keep track of the spending of each player
player_1_amt = 10
player_2_amt = 10

# Lists to store the army of the two players
player_1_army = []
player_2_army = []


def get_team(amount_rem):
    """Logic to create the team of any player
    Parameters
    -----------
    amount_rem: amount that is remaining with the player

    Returns
    -----------
    army: army created
    amount_rem: remaining amount of the player

    """
    army = []

    # The below loop is to keep asking the choices to the player
    while(1):
        # The below if condition is responsible for the breaking of the loop.
        if(amount_rem == 0):
            print("You have exhausted all the budget. Here's your army: ", army)
            print("Lets begin the battle!! ")
            return army, amount_rem

        # Below are the choices presented to the player to choose from
        print("-------------------------------------------------------")
        print("Your remaining balance is: $" + str(amount_rem))
        print("Your current army is: ", army)
        print("For Archer (costs $1), enter 1")
        print("For Soldier (costs $1), enter 2")
        print("For Knight (costs $1), enter 3")
        print("For Siege Equipment (costs $2), enter 4")
        print("For Wizard (costs $3), enter 5")
        print("I am ready to fight!! Bring it on!! Enter 6")
        choice = input("Enter your choice: ")

        # Below if-else condition appends a unit to the army list
        # and reduces the remaining amount by the cost of that unit.
        if (choice == "1"):
            army.append(archer)
            amount_rem = amount_rem - cost_unit[archer]
        elif (choice == "2"):
            army.append(soldier)
            amount_rem = amount_rem - cost_unit[soldier]
        elif (choice == "3"):
            army.append(knight)
            amount_rem = amount_rem - cost_unit[knight]
        elif (choice == "4"):
            # First check if the player has sufficient balance left to buy. If not,
            # prompt appropriate error message.
            if(amount_rem >= cost_unit[siege]):
                army.append(siege)
                amount_rem = amount_rem - cost_unit[siege]
            else:
                print("You do not have enough budget to buy a Siege. Please choose some other unit!!")
        elif (choice == "5"):
            if (amount_rem >= cost_unit[wizard]):
                army.append(wizard)
                amount_rem = amount_rem - cost_unit[wizard]
            else:
                print("You do not have enough budget to buy a Wizard. Please choose some other unit!!")
        elif (choice == "6"):
            return army, amount_rem
        else:
            print("Incorrect choice. Please enter the right choice.")


def combat_logic(army1, army2, amount1, amount2):
    """Logic for the fight of the armies of the two players
    Parameters
    -----------
    army1: Army of Player 1
    army2: Army of Player 2
    amount1: Remaining amount of Player 1
    amount2: Remaining amount of Player 2

    Returns
    -----------
    0: Match is tied
    "Player 1": Player 1 wins
    "Player 2": Player 2 wins
    """

    # Below are the variables to keep track of the current position of the army lists.
    # Although, these variables have never been updated in the code,
    # but its always a good practice to use the index of a list by a variable,
    # rather than hard coding it to 0.
    pos1, pos2 = 0, 0

    # The below if condition returns 0(tied match) if both the armies are empty.
    if (len(army1) == 0 and len(army2) == 0):
        return 0

    # The below while loop runs until one of the army gets emptied, hence making
    # the other player as a winner.
    while(len(army1) !=0 and len(army2) != 0):

        # The variable unit1 and unit2 store the units that would fight from
        # both the teams.
        unit1 = army1[pos1]
        unit2 = army2[pos2]

        # The below two variables store the unit that would die in the battle.
        # This is to take care of the medics module of the extended game.
        # These are initialised as None at the start of each battle.
        army1_died, army2_died = None, None
        print("-------------------------------------------------------")
        print("Battle between Player 1's "+unit1 + " and player 2's "+unit2)

        # The below if-else logic is for the battle as per the requirement.
        # Whenever a unit dies, pop() method is used to remove an element from the list
        # so that the removed element is returned.
        # The logic suitably prints which player's unit has died after each battle.

        # The battle logic is as per the requirements given. Please refer to the
        # requirements document for the details. Commenting that here would be highly
        # redundant.
        if(unit1 == archer):
            if(unit2 == archer):
                print("Its a tie. Both unit dies.")
                army1_died = army1.pop(pos1)
                army2_died = army2.pop(pos2)
            elif(unit2 == soldier):
                print("Player 1's", archer, "has won.")
                army2_died = army2.pop(pos2)
            elif(unit2 == knight):
                print("Player 2's", knight, "has won.")
                army1_died = army1.pop(pos1)
            elif(unit2 == siege):
                print("Player 2's", siege, "has won.")
                army1_died = army1.pop(pos1)
            elif (unit2 == wizard):
                print("Player 1's", archer, "has won.")
                army2_died = army2.pop(pos2)
            else:
                print("ABORT!!!!!! SOMETHING IS WRONG")
                exit(0)
        elif (unit1 == soldier):
            if (unit2 == archer):
                print("Player 2's", archer, "has won.")
                army1_died = army1.pop(pos1)
            elif (unit2 == soldier):
                print("Its a tie. Both unit dies.")
                army1_died = army1.pop(pos1)
                army2_died = army2.pop(pos2)
            elif (unit2 == knight):
                print("Player 1's", soldier, "has won.")
                army2_died = army2.pop(pos2)
            elif (unit2 == siege):
                print("Player 2's", siege, "has won.")
                army1_died = army1.pop(pos1)
            elif (unit2 == wizard):
                print("Player 2's", wizard, "has won.")
                army1_died = army1.pop(pos1)
            else:
                print("ABORT!!!!!! SOMETHING IS WRONG")
        elif (unit1 == knight):
            if (unit2 == archer):
                print("Player 1's", knight, "has won.")
                army2_died = army2.pop(pos2)
            elif (unit2 == soldier):
                print("Player 2's", soldier, "has won.")
                army1_died = army1.pop(pos1)
            elif (unit2 == knight):
                print("Its a tie. Both unit dies.")
                army1_died = army1.pop(pos1)
                army2_died = army2.pop(pos2)
            elif (unit2 == siege):
                print("Player 1's", knight, "has won.")
                army2_died = army2.pop(pos2)
            elif (unit2 == wizard):
                print("Player 2's", wizard, "has won.")
                army1_died = army1.pop(pos1)
            else:
                print("ABORT!!!!!! SOMETHING IS WRONG")
        elif (unit1 == siege):
            if (unit2 == archer):
                print("Player 1's", siege, "has won.")
                army2_died = army2.pop(pos2)
            elif (unit2 == soldier):
                print("Player 1's", siege, "has won.")
                army2_died = army2.pop(pos2)
            elif (unit2 == knight):
                print("Player 2's", knight, "has won.")
                army1_died = army1.pop(pos1)
            elif (unit2 == siege):
                print("Its a tie. Both unit dies.")
                army1_died = army1.pop(pos1)
                army2_died = army2.pop(pos2)
            elif (unit2 == wizard):
                print("Player 2's", wizard, "has won.")
                army1_died = army1.pop(pos1)
            else:
                print("ABORT!!!!!! SOMETHING IS WRONG")
        elif (unit1 == wizard):
            if (unit2 == archer):
                print("Player 2's", archer, "has won.")
                army1_died = army1.pop(pos1)
            elif (unit2 == soldier):
                print("Player 1's", wizard, "has won.")
                army2_died = army2.pop(pos2)
            elif (unit2 == knight):
                print("Player 1's", wizard, "has won.")
                army2_died = army2.pop(pos2)
            elif (unit2 == siege):
                print("Player 1's", wizard, "has won.")
                army2_died = army2.pop(pos2)
            elif (unit2 == wizard):
                print("Its a tie. Both unit dies.")
                army1_died = army1.pop(pos1)
                army2_died = army2.pop(pos2)
            else:
                print("ABORT!!!!!! SOMETHING IS WRONG")
        else:
            print("ABORT!!!!!! SOMETHING IS WRONG")


        # If the unit of player 1 died and the player had amount remaining
        # for medics, the unit would be appended at the back and $1 would
        # be reduced from the army's balance.
        if (army1_died and amount1 > 0):
            print("\nApplying Medics to " + army1_died + " of Team 1.")
            print("Medics applied to " + army1_died + " and pushed back to team 1")
            army1.append(army1_died)
            amount1 = amount1 - 1

        # If the unit of player 2 died and the player had amount remaining
        # for medics, the unit would be appended at the back and $1 would
        # be reduced from the army's balance.
        if (army2_died and amount2 > 0):
            print("\nApplying Medics to " + army2_died + " of Team 2.")
            print("Medics applied to " + army2_died + " and pushed back to team 2")
            army2.append(army2_died)
            amount2 = amount2 - 1

        print("-------------------------------------------------------")

    # Once we are outside the loop, the battle is over.
    print("BATTLE OVER")

    # If both the armies have no units left, its a draw, hence returning 0.
    if (len(army1) == 0 and len(army2) == 0):
        return 0

    # Otherwise returning the player whoever has units left in the army.
    return "Player 1" if len(army1) > 0 else "Player 2"


# Input the first army
print("-------------------------------------------------------")
print("Time to enter the first team!!")
player_1_army, player_1_amt = get_team(10)

print("Team 1 is ready to fight. Their army is: ", player_1_army)
print("-------------------------------------------------------")
print("\nPlayer 1 has $" + str(player_1_amt) + " remaining for medics.")
print("-------------------------------------------------------")
print("-------------------------------------------------------")
print("-------------------------------------------------------")


# Input the second army
print("Time to enter the second team!!")
player_2_army, player_2_amt = get_team(10)
print("Team 2 is ready to fight. Their army is: ", player_2_army)
print("-------------------------------------------------------")
print("\nPlayer 2 has $" + str(player_2_amt) + " remaining for medics.")
print("-------------------------------------------------------")
print("-------------------------------------------------------")
print("-------------------------------------------------------")

print("\n \n-------------------------------------------------------")
print("Both the teams are ready to fight. LETS BEGIN THE BATTLE!!!!!!!")
print("-------------------------------------------------------\n \n")

print("Here are both the teams:")
print("Team 1: ", player_1_army)
print("Team 2: ", player_2_army)

print("\n\n-------------------------------------------------------")
print("-------------------------------------------------------")
input("Press Enter to start the battle!!!!!")

print("-------------------------------------------------------")
print("-------------------------------------------------------\n\n")

# Calling the function for the battle.
winner = combat_logic(player_1_army, player_2_army, player_1_amt, player_2_amt)

# If the returned value is 0, it means the match has tied, otherwise
# the winner is displayed on the screen.
if(winner == 0):
    print("The match has tied!!!")
else:
    print(winner, " is the winner.... CONGRATULATIONS!!!! ")



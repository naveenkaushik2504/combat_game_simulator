# Combat Battle Simulator Project

## simple_game:
At the start of the game, each commander is given a starting total of $10. Units are purchased
and stored in their army. The commanders may spend as much or as little of their money as
they desire. After the armies are assembled, the units are then made to fight each other in
the order they were purchased in. Each unit in the standard game costs $1.
There are three types of units available:
- Archer
- Soldier
- Knight
Each unit has a weakness and a strength. Archers are good against Soldiers but are terrible
against Knights. Soldiers are good against Knights but can’t win against Archers. Knights
beat Archers, but fall short against Soldiers. If a unit comes up against a unit of the same
type, both lose.

After each fight, the winner is left on the battlefield to fight the next combatant. If both units
lose, then two new units are taken from the army and begin their fight.

Combat should be resolved automatically. The outcome of each fight is listed in the
console until one army is defeated. Once this occurs, the winner is listed and the game
ends.


## extended_game:

The extended_game is the extension of basic game with the following advancements.

1. Expanded Armies:
Add two new units for the commanders to choose from:
• Siege Equipment: who win against everyone except Knights and Wizards.
• Wizard: who can beat anything, but they can’t dodge Archer arrows.

2. Medics:
Money remaining after the purchasing of armies will be used to hire and outfit medics.
When a unit dies, it will be returned to the pool at the back of the army. Each time
this happens, supplies for the medics decreases. Once the medics have no supplies left,
they will be unable to save any more units.
Medics are hired and supplied at $1 per unit. All money at the end of army creation is
spent on Medics.


## Prerequisites
Python version 3.6

## Running

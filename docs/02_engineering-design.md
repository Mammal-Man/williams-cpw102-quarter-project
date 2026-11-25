# Engineering Design Document


## Overview

[Provide a system-level explanation of:

- major components of your application and how they interact.
- data flow at a high level

A friend should be able to read this section and, at a glance, understand how the application works. ]

The two major components are the Combat Loop and Dialogue Loop:
- The combat loop  alternates between player and enemy turns, following the action order of discarding unwanted cards, drawing up to a full hand, then playing cards equal to the player's available units
## System Diagrams

![alt text](<../Command Line RPG.drawio.png>)

[This document must include one or more of the following:

- block diagram of your proposed functions and modules, including external libraries
- flowchart of logic for critical flows
- mockups of any program-driven user interfaces, if applicable]

## Technical Details


### Inputs

Players will make selections via terminal following the prompt they are given

#### Handling bad inputs

When an input is given that does not follow the expected format, the game will prompt the player to provide a valid input until one is given.

### Logic

while loops for combat, alternating turns between player and enemy

lists containing players hand, draw deck, and discard pile, as well as npc dialogue and enemy hands, draw decks, and discard piles

dictionaries will hold all possible cards, so when a card is played its effects can be pulled from the dictionary

### Functions

[How will you break your flow of logic up into functions? Write some psuedo code for your `main()` function to show how your app will coordinate its duties.]

``` python
def main():
    while missions_available > total_missions:
        mission = input("SELECT MISSION: ")
        if mission in new_missions:
            begin_dialogue(mission)
    pass

main()
```

### Libraries
 
The game will utilize the random library native to python to draw cards randomly for the player and ai to use.

### Output

Dialogue and important information relating to combat will be outputted to the terminal during each turn. Both the options and the effects of their chosen option will be displayed to the player in combat.

```
Begin Player Turn:
Cards Drawn: Card1, Card3, Card6
Player Hand: Card1, Card2, Card3, Card6, Card7
Would you like to know the effects of one of your cards? yes
Which card? Card7
Card7 attacks the opponent for 8-10 damage
You have 2 Units
Play Card? no
Player Hand: Card1, Card2, Card3, Card6, Card7
Would you like to know the effects of one of your cards? no
You have 2 Units
Which card would you like to play?
```
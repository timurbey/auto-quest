# `dummy` combat system

A simple combat system with customizable logic.

## character overview

The `dummy` system provides an abstract `Character` meant for inheritance.

`Characters` have a health, armor, and threat value. When a character's health reaches 0, they are dead and cannot act or be targeted. When dealt damage, characters lose armor before health.

`Characters` use a choice function to select targets from a group. The choice function consumes a list of `Characters` and returns a `Character` from that list. The default choice function randomly selects a character from a cumulative distribution based on threat.

`Characters` use self-evaluation to decide actions. The evaluation function consumes a list of `Characters` and returns a `State`, which is used as a switch for logic. Currently, there are `DANGER`, `THREAT`, and `NORMAL` states. The default evaluation function returns `DANGER` if the character targets itself and has below 30 health, `THREAT` if the character targets itself, and `NORMAL` otherwise.

A user can also provide custom logic for the choice and evaluation functions. These are passed as parameters to the constructor.

## dummy tournament

The `dummy` system also implements a `tournament` game. There are four provided classes (`Cleric`, `Fighter`, `Mage`, `Rogue`) that can be built using the customizable logic described above.

## TODO

 - improve existing classes
 - implement more classes
 - customization of health and action values
 - improve "tournament" system
 - add custom logic hook-ins
 - improve logging and log processing

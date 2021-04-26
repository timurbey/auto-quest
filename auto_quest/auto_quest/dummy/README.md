# `dummy` combat system

Simple combat system

## overview

The `dummy` system uses a simple character called a `DummyCharacter`. `DummyCharacters` have a health, armor, and threat value. When a character's health reaches 0, they are dead and cannot act or be targeted.

`DummyCharacters` make decisions based on a choice function and an evaluation function.

The choice function returns a member of a group of characters. The default choice function randomly selects a character based on threat (`p_c_k = c_k.t / sum(C)`).

The evaluation function returns true if the character is threatened, making the decision between the `on_threat` and `on_no_threat` actions. The default evaluation function returns true if the character selects itself with its choice function.

## TODO

 - expand states
 - write better hooks
 - implement more classes
 - improve "tournament" system

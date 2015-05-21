Tobias
======

##A open source, text based, RPG game made by a bunch of friends. More changes to come!

###Files, what they do, and *what we need to do*:
- items.py
    - Defines all of the items and weapons
    - **TODO**: Create 'specials' for weapons, allowing for extra damage, such as poison or burn damage.
- enemies.py
    - Defines all of the enemies, their armor, and their health
    - They use the weapons made in items.py
    - **TODO**: Remove 'specials', they have been obsoleted by weapons. Make more enemies? Perhaps add random taunts to make things interesting?
- player.py
    - Defines all player information, including how the player attacks
    - Uses weapons made in items.py
    - **TODO**: ~~Test if `PlayerAttack()` works.Implement a weapon choose action here or in `actions.py`. ~~ Add a experience and leveling system, which means also add stats such as speed, intelligence, etc to both player and enemies?
- actions.py
    - Actions a player can take, such as moving. Also defines hotkeys.
    - **TODO**: ~~Write all movement actions, attack actions,~~ and maybe a weapon switch action here.
- world.py
    - Generates a world from a tab-delimited file, example of a level file will be added soon.
    - **TODO**: Add multiple levels. ~~Add a `exitLevel()` tile.~~ Figure out random tile generation for some locations.
- **Other thing TODO**
    - ~~Create the actual game loop, figure out order of events~~
    - Sort out the story

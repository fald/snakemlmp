from classes.application import App
import pygame

# TODO: 
#   Just remake this in tkinter??
#   Alternatively, sort of map things out on paper first, though
#       that tends to lead to nothing happening at all instead of
#       just trash happening...hm.
#   Also currently collision and the like are handled in the grid window, not per unit, dunno if that's a good idea.
#   Probably just...ditch the whole grid thing, restart from last stable, but messy, point and clean up again without it.
#
#   windows add component to work with dictionary extends
#   Major cleanup needed.
#   Grid filling for collision and such.
#   Attach AI to snake instead of application
#   Map objects instead of whatever this is.
#   Implement ML AI
#   Train ML AI
#   sliders/settings
#   Separate controls between ai/player
#   Have stuff on sub windows do stuff
#   Set controls to only work in correct game state
#   Game over when no more apples to eat
#   Make use of roguelike style components?
#   Put collisions elsewhere than in application loop
#   Fix new game and application mixups
#   Game state handling (not just crashing on game over lol)
#   Menus - scoreboard, option settings
#   Refactor everything once it works, ick.
#   Work with multiplayer or multiple snakes, whatever
#   AI control, AI options on-screen
#   Add render order
#   Stop the clusterfuck, I want off Mr Firas' Wild Ride 
#   Sanity checks?
# This shit is too overengineered and I haven't even got to the fucking AI yet.

if __name__ == "__main__":
    window = App()
    window.on_execute()

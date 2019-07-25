from classes.application import App
import pygame

# TODO: 
#   Just remake this in tkinter??
#   Have stuff on sub windows do stuff
#   Set controls to only work in correct game state
#   Add render order
#   Control setup
#   Game over when no more apples to eat
#   Put collisions elsewhere than in application loop
#   Fix new game and application mixups
#   Game state handling (not just crashing on game over lol)
#   Menus - scoreboard, option settings
#   Roll around walls
#   Work with multiplayer or multiple snakes, whatever
#   AI control, AI options on-screen
#   Stop the clusterfuck, I want off Mr Firas' Wild Ride 
#   Sanity checks?
# This shit is too overengineered and I haven't even got to the fucking AI yet.

if __name__ == "__main__":
    window = App()
    window.on_execute()
from classes.application import App
import pygame

# TODO: 
#   Control setup
#   Game over when no more apples to eat
#   Put collisions elsewhere than in application loop
#   Game state handling (not just crashing on game over lol)
#   Menus - scoreboard, option settings
#   init.new_game
#   Roll around walls
#   AI control, AI options on-screen
#   Player control schemes
#   Sanity checks?

if __name__ == "__main__":
    window = App()
    window.on_execute()
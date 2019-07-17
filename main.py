from classes.application import App
import pygame

# TODO: 
#   Self-crashing
#   Out of bounds handling
#   Control setup
#   New apple location not to interfere with snake body

if __name__ == "__main__":
    window = App()
    window.on_execute()
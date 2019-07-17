from classes.application import App
import pygame

# TODO: 
#   Self-crashing
#   Out of bounds handling
#   Control setup
#   New apple location not to interfere with snake body
#   Game over when no more apples to eat

if __name__ == "__main__":
    window = App()
    window.on_execute()
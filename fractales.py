import pygame
import sys
import math
import colorsys

pygame.init()

WIDTH = 1920
HEIGHT = 1080

start = int(1100), int(750)
length = int(50)
ratio = float(0.8)

axiom = "F+F+F"

num_rules = int(1)
rules = {
        "F" : "F+FF-F"
        }
 #   for i in range(num_rules):
 #       rule = f.readline().split(' ')
 #       rules[ru

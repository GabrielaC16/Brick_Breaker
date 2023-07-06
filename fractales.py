import pygame
import sys
import math
import colorsys

pygame.init()

WIDTH = 800
HEIGHT = 600

start = int(100), int(600)
length = int(50)
ratio = float(0.8)


axiom = "F+F+F"

num_rules = int(1)
rules = {
        "F" : "F+F-F+F"
        }

 #   for i in range(num_rules):
 #       rule = f.readline().split(' ')
 #       rules[rule[0]] = rule[1]
angle = 120


class LSystem():
    def __init__(self, axiom, rules, angle, start, length, ratio):
        self.sentence = axiom
        self.rules = rules
        self.angle = angle
        self.start = start
        self.x, self.y = start
        self.length = length
        self.ratio = ratio
        self.theta = math.pi / 2
        self.positions = []
        self.draw_postion = set()
        self.deep = 2

    def __str__(self):
        return self.sentence

    def generate(self):
        self.x, self.y = self.start
        self.theta = math.pi / 2
        self.length *= self.ratio
        new_sentence = ""
        for char in self.sentence:
            mapped = char
            try:
                mapped = self.rules[char]
            except:
                pass
            new_sentence += mapped
        self.sentence = new_sentence

    
    def draw(self):
        hue = 0
        for char in self.sentence:
            if char == 'F':
                x2 = self.x - self.length * math.cos(self.theta)
                y2 = self.y - self.length * math.sin(self.theta)
                #pygame.draw.line(screen, (hsv2rgb(hue, 1, 1)), (self.x, self.y), (x2, y2), 2)
                self.x, self.y = x2, y2
                e = 0.85
                self.draw_postion.add((e*x2, e*y2))


            elif char == '+':
                self.theta += self.angle
            elif char == '-':
                self.theta -= self.angle
            elif char == '[':
                self.positions.append({'x': self.x, 'y': self.y, 'theta': self.theta})
            elif char == ']':
                position = self.positions.pop()
                self.x, self.y, self.theta = position['x'], position['y'], position['theta']
            hue += 0.00005
    
    def get_positions(self):
        return self.draw_postion


def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))


deep = 3

def gen_positions():

    fractal = LSystem(axiom, rules, angle, start, length, ratio)
    running = True

    for i in range(deep):
        fractal.generate()

    fractal.draw()
    v = fractal.get_positions()
    return v
 
#main()

# William-McWorter-Maze01          python fractals.py fractals/William_McWorter_Maze01.txt 1100 750 50 0.8


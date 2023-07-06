import pygame
import sys
import math
import colorsys

pygame.init()

WIDTH = 800
HEIGHT = 700
ERROR = 40
COTA_INF = 250

start = (400, 250)
length = int(53)
ratio = float(0.52)

axiom = "F++++F"
rules = {"F":"F+F+F++++F+F+F"}
angle = math.radians(int(45))

deep = 2

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
        self.deep = deep
        self.save_position = set()

    def __str__(self):
        return self.sentence

    def generate(self):
        self.x, self.y = self.start
        self.theta = math.pi / 2
        self.length *= self.ratio
        new_sentence = ""


        for _ in range(self.deep):
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
                self.save_position.add((self.x, self.y))
                self.save_position.add((x2, y2))
                self.x, self.y = x2, y2

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
        pos = set()

        for e in (self.save_position) :
            x = e[0]
            y = e[1]
            if x >=0 and x <WIDTH-ERROR and y>COTA_INF and y< HEIGHT-2*ERROR:
                pos.add((x,y))

        return pos


def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))


def gen_positions():

    fractal = LSystem(axiom, rules, angle, start, length, ratio)
    fractal.generate()
    fractal.draw()
    v = fractal.get_positions()
    return v
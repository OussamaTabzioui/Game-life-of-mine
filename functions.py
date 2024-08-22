import random
import pygame
from settings import *

def gen0(width, height, array):
    for x in range(width):
        for y in range(height):
            array[x][y] = random.randint(0, 1)
            # array[x][y] = 0

def checkNeighbors(array, x, y):
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            nx, ny = (x + i + len(array)) % len(array), (y + j + len(array[0])) % len(array[0])
            neighbors.append(array[nx][ny])
    return neighbors

def count(neighbors):
    n1 = sum(1 for n in neighbors if n == 1)
    return n1

def rules(current_state, n1):
    if current_state == 1:
        if n1 < 2 or n1 > 3:  # Underpopulation or overpopulation
            return 0
        elif 2 <= n1 <= 3:  # Survival
            return 1
    elif current_state == 0:
        if n1 == 3:  # Reproduction
            return 1
    return current_state


def nextGen(array):
    new_array = [row[:] for row in array]
    for x in range(len(array)):
        for y in range(len(array[0])):
            neighbors = checkNeighbors(array, x, y)
            n1 = count(neighbors)
            new_array[x][y] = rules(array[x][y], n1)
    return new_array


def addToArray(array, cor_x, cor_y):
    array[cor_y][cor_x] = 1

def removeFromArray(array, cor_x, cor_y):
    array[cor_y][cor_x] = 0

def add_glider(array, x, y):
    pattern = [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    for dx, dy in pattern:
        array[(y + dy) % len(array)][(x + dx) % len(array[0])] = 1

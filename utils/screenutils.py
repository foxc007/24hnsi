import pygame


def get_width():
    return pygame.display.Info().current_w


def get_heigth():
    return pygame.display.Info().current_h


def compute_x_coeff():
    return get_width() / 1920


def compute_y_coeff():
    return get_heigth() / 1080


def responsive_x(game, x):
    return round(x * game.x_coeff)


def x(game, x):
    responsive_x(game, x)


def responsive_y(game, y):
    return round(y * game.y_coeff)


def y(game, y):
    responsive_y(game, y)


def responsive_size(game, size: tuple or list):
    return (round(size[0] * game.x_coeff), round(size[1] * game.y_coeff))


def size(game, size: tuple or list):
    return responsive_size(game, size)

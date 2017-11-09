from config import *


def uint_to_rgb(RGBint):
    Blue = RGBint & 255
    Green = (RGBint >> 8) & 255
    Red = (RGBint >> 16) & 255
    return (1.0 / 255) * Red, (1.0 / 255) * Green, (1.0 / 255) * Blue


def shape_to_mesh(shape, color):
    r, g, b = uint_to_rgb(color)
    verts = []
    indicies = []
    last_index = -1
    for row_index, row in enumerate(shape):
        for col_index, col in enumerate(row):
            if col == 1:
                verts += [
                    (BLOCK_SIZE * col_index), (BLOCK_SIZE * row_index), r, g, b,
                    (BLOCK_SIZE * col_index) + BLOCK_SIZE, (BLOCK_SIZE * row_index), r, g, b,
                    (BLOCK_SIZE * col_index) + BLOCK_SIZE, (BLOCK_SIZE * row_index) + BLOCK_SIZE, r, g, b,
                    (BLOCK_SIZE * col_index), (BLOCK_SIZE * row_index) + BLOCK_SIZE, r, g, b,
                ]
                indicies += [last_index + 1, last_index + 2, last_index + 3, last_index + 3, last_index + 4, last_index + 1]
                last_index = last_index + 4
    return verts, indicies

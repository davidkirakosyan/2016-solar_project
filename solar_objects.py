# coding: utf-8
# license: GPLv3

class CelestialBody:
    """
    Kласс, описывающий любое космическое тело.
    Содержит массу, координаты, скорость объекта,
    а также визуальный радиус в пикселах и его цвет.
    """

    def __init__(self, type, m, x, y, Vx, Vy, Fx, Fy, R, color, image):
        self.type = type
        self.m = m
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.Fx = Fx
        self.Fy = Fy
        self.R = R
        self.color = color
        self.image = image

    def move(self, dt):
        """
        Изменяет координаты и скорости тело за малое время dt.

        Параметры:
        dt - шаг по времени.
        """
        self.x += self.Vx * dt
        self.y += self.Vy * dt
        self.Vx += self.Fx / self.m * dt
        self.Vy += self.Fy / self.m * dt

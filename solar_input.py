# coding: utf-8
# license: GPLv3

from solar_objects import CelestialBody


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов
    Параметры:
    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":  # FIXME: Добавь данные с файла
                star = CelestialBody(
                    "star",
                    1000,
                    1,
                    2,
                    0.03,
                    0.04,
                    0,
                    0,
                    10,
                    "red",
                    None
                )
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = CelestialBody(
                    "planet"
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    5,
                    "green",
                    None
                    )
                parse_planet_parameters(line, planet)
                objects.append(planet)
                # FIXME: Делай тоже самое для планет
            else:
                print("Unknown space object")

    return objects


def parse_celestialbodies_parameters(line, object_type):
    """Считывает данные о звезде/планете из строки.
    Входная строка должна иметь слеюущий формат:
    Star/Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Здесь (x, y) — координаты тела, (Vx, Vy) — скорость.
    Пример строки:
    Star/Planet 10 red 1000 1 2 3 4
    Параметры:
    **line** — строка с описание звезды.
    **star/planet** — объект звезды.
    """
    line = line.split()
    object_type.R = float(line[1])
    object_type.color = float(line[2])
    object_type.m = float(line[3])
    object_type.x = float(line[4])
    object_type.y = float(line[5])
    object_type.Vx = float(line[6])
    object_type.Vy = float(line[7])
    pass  # FIXME: not done yet...


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Параметры:
    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            print(out_file, "%s %d %s %f" % ('type',  #!!!
                                             obj.R,
                                             obj.color,
                                             obj.m, 
                                             obj.x, 
                                             obj.y, 
                                             obj.Vx, 
                                             obj.Vy
                                             )
                  )
            # FIXME: should store real values


# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл...

if __name__ == "__main__":
    print("This module is not for direct call!")
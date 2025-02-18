# coding: utf-8
# license: GPLv3

v = []
r = []

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.

    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!
        rx = obj.x - body.x
        ry = obj.y - body.y
        r = (rx**2 + ry**2)**0.5
        r = max(r, body.R)
        force = gravitational_constant * body.m * obj.m / (r ** 2)
        body.Fx += force * rx/r
        body.Fy += force * ry/r


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """

    ax = body.Fx / body.m    
    ay = body.Fy / body.m
    body.Vx += ax * dt
    body.Vy += ay * dt
    body.x += body.Vx * dt
    body.y += body.Vy * dt


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.

    **dt** — шаг по времени
    """

    global v, r
    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)
        if body == space_objects[1]:
            v.append((body.Vx**2+body.Vy**2)**0.5)
            dx = body.x - space_objects[0].x
            dy = body.y - space_objects[0].y
            r.append((dx**2+dy**2)**0.5)


if __name__ == "__main__":
    print("This module is not for direct call!")

# coding: utf-8
# license: GPLv3

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""

FF = 0
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
    
      # FIXME: Вывести формулы для ускорения, скоростей и координат
    ax = body.Fx / body.m    
    ay = body.Fy / body.m
    body.Vx += ax * dt
    body.Vy += ay * dt
    body.x += body.Vx * dt
    body.y += body.Vy * dt
    # body.T = body.T + dt
    '''
    сохраняем в файл тройки значений в каждый момент времени
    <модуль скорости>   <расстояние от планеты до звезды>  <время>
    '''
    # if body.type == 'planet':
    #     if len(objects) == 2:
    #         with open('stats.txt', 'w') as out_file:
    #             out_file.write(str((body.Vx**2 + body.Vy**2)**0.5) + ' ' + str(((body.x - star.x)**2 + (body.y - star.y)**2)**0.5) + ' ' + str(body.T))
    #

def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.

    **dt** — шаг по времени
    """
    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")

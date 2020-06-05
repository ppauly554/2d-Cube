import pygame

pygame.init()

W, H = 900, 900


window = pygame.display.set_mode((W, H))


class Cube:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.center = (x, y)

    def line(self, joint):
        pygame.draw.line(window, (255, 255, 255), (self.x, self.y), (joint.x, joint.y), 5)

    def polygon(self, joint0, joint1, joint2, color):
        pygame.draw.polygon(window, color,
                            ((self.x, self.y), (joint0.x, joint0.y), (joint1.x, joint1.y), (joint2.x, joint2.y)))


points = [
    Cube(W * 1 / 8, H * 1 / 8),
    Cube(W * 5 / 8, H * 1 / 8),
    Cube(W * 1 / 8, H * 5 / 8),
    Cube(W * 5 / 8, H * 5 / 8),
    Cube(W * 1 / 4, H * 1 / 4),
    Cube(W * 3 / 4, H * 1 / 4),
    Cube(W * 1 / 4, H * 3 / 4),
    Cube(W * 3 / 4, H * 3 / 4)
]

links = [
    (points[0], points[1], points[2], points[4]),
    (points[1], points[0], points[3], points[5]),
    (points[2], points[0], points[3], points[6]),
    (points[3], points[1], points[2], points[7]),
    (points[4], points[0], points[5], points[6]),
    (points[5], points[1], points[4], points[7]),
    (points[6], points[2], points[4], points[7]),
    (points[7], points[3], points[5], points[6])
]

sides = [
    (points[2], points[0], points[1], points[3], (255, 0, 0)),
    (points[0], points[4], points[5], points[1], (0, 255, 0)),
    (points[4], points[6], points[7], points[5], (0, 0, 255)),
    (points[2], points[6], points[7], points[3], (255, 255, 0)),
    (points[0], points[4], points[6], points[2], (0, 255, 255)),
    (points[3], points[7], points[5], points[1], (255, 0, 255)),
]

clock = pygame.time.Clock()

run = True
while run:
    clock.tick(60)
    pygame.display.flip()
    window.fill((0, 0, 0))

    mpos = pygame.mouse.get_pos()

    for point in points:
        point.x, point.y = point.center

    for point in range(len(points)):
        if point % 2:
            points[point].x -= mpos[0] - W // 2
            points[point].y -= mpos[1] - H // 2
        else:
            points[point].x += mpos[0] - W // 2
            points[point].y += mpos[1] - H // 2

    for group in range(len(sides)):
        sides[group][0].polygon(sides[group][1], sides[group][2], sides[group][3], sides[group][4])

    for group in range(len(links)):
        for connection in range(3):
            links[group][0].line(links[group][connection + 1])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
pygame.quit()

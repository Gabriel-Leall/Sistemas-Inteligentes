import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import random


def generate_obstacles(num_obstacles, area_size, obstacle_size, start_pos, end_pos, margin):
  obstacles = []

  while len(obstacles) < num_obstacles:
    x = random.randint(0, area_size[0] - obstacle_size[0])
    y = random.randint(0, area_size[1] - obstacle_size[1])
    new_obstacle = (x, y, obstacle_size[0], obstacle_size[1])

    is_valid = True
    if is_point_in_rect(start_pos, new_obstacle) or is_point_in_rect(end_pos, new_obstacle):
        is_valid = False
    
    if is_valid and not any(intersect(new_obstacle, o, margin) for o in obstacles):
      obstacles.append(new_obstacle)

  return obstacles

def intersect(obstacle1, obstacle2, margin=0):
  x1, y1, w1, h1 = obstacle1 
  x2, y2, w2, h2 = obstacle2

  if (x1 + w1 < x2):
    return False

  if (x1 + w1 + margin < x2):
    return False

  if (x1 - margin > x2 + w2):
    return False

  if (y1 + h1 + margin < y2):
    return False

  if (y1 - margin > y2 + h2):
    return False

  return True

def is_point_in_rect(point, rect):

    point_x, point_y = point
    rect_x, rect_y, rect_width, rect_height = rect
    
    return (rect_x <= point_x <= rect_x + rect_width) and \
           (rect_y <= point_y <= rect_y + rect_height)

def points(obstacles, start, end):
  points = {start, end}
  for (x, y, w, h) in obstacles:
      points.add((x, y))
      points.add((x + w, y))
      points.add((x, y + h))
      points.add((x + w, y + h))
  return list(points) 

def visualize(obstacles, points, start_pos, end_pos, area_size):
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim(0, area_size[0])
    ax.set_ylim(0, area_size[1])

    for x, y, w, h in obstacles:
        ax.add_patch(Rectangle((x, y), w, h, color='gray', zorder=1))

    ax.scatter(*zip(*points), color='skyblue', s=20, zorder=2, label='Vértices')

    ax.scatter(start_pos[0], start_pos[1], color='black', s=50, zorder=2, label='Início')
    ax.scatter(end_pos[0], end_pos[1], color='red', s=50, zorder=2, label='Fim')

    plt.title("Mapa de Obstáculos e Pontos Estratégicos")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    AREA_SIZE = (1000, 1000)
    OBSTACLE_SIZE = (50, 50)
    NUM_OBSTACLES = random.randint(20, 50)
    MIN_MARGIN = 10  
    START_POS = (20, 20)
    END_POS = (980, 980)

    obstacles = generate_obstacles(NUM_OBSTACLES, AREA_SIZE, OBSTACLE_SIZE, START_POS, END_POS, MIN_MARGIN)
    strategic_points = points(obstacles, START_POS, END_POS)

    print(f"Gerados {len(obstacles)} obstáculos e {len(strategic_points)} pontos estratégicos.")
    
    visualize(obstacles, strategic_points, START_POS, END_POS, AREA_SIZE)
import matplotlib.pyplot as plt
from matplotlib.patches import circulo
import random
import math


def generate_obstacles(num_obstacles, area_size, min_radius, max_radius, start_pos, end_pos, margin):
  obstacles = []

  while len(obstacles) < num_obstacles:
    radius = random.randint(min_radius, max_radius)
    x = random.randint(radius, area_size[0] - radius)
    y = random.randint(radius, area_size[1] - radius)
    new_obstacle = (x, y, radius)

    if is_point_in_circulo(start_pos, new_obstacle) or is_point_in_circulo(end_pos, new_obstacle):
        continue
    
    if not any(circulos_intersect(new_obstacle, o, margin) for o in obstacles):
      obstacles.append(new_obstacle)

  return obstacles

def circulos_intersect(circulo1, circulo2, margin=0):
  x1, y1, r1 = circulo1
  x2, y2, r2 = circulo2

  distancia_quad = (x1 - x2)**2 + (y1 - y2)**2
  
  raio_quadrado = (r1 + r2 + margin)**2
  
  return distancia_quad <= raio_quadrado

def is_point_in_circulo(point, circulo):
  point_x, point_y = point
  circulo_x, circulo_y, radius = circulo
  
  distancia_quad = (point_x - circulo_x)**2 + (point_y - circulo_y)**2
  
  return distancia_quad <= radius**2

def get_strategic_points(obstacles, start, end):
  points = {start, end}
  for (x, y, r) in obstacles: # eixo x, eixo y, r raio
      points.add((x + r, y))
      points.add((x - r, y))
      points.add((x, y + r))
      points.add((x, y - r))
  return list(points) 

def visualizar_mapa(obstacles, points, start_pos, end_pos, area_size):
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim(0, area_size[0])
    ax.set_ylim(0, area_size[1])

    for x, y, r in obstacles:
        ax.add_patch(circulo((x, y), r, color='gray', zorder=1))

    ax.scatter(*zip(*points), color='skyblue', s=20, zorder=2, label='Vértices')

    ax.scatter(start_pos[0], start_pos[1], color='black', s=50, zorder=2, label='Início')
    ax.scatter(end_pos[0], end_pos[1], color='red', s=50, zorder=2, label='Fim')

    plt.title("Mapa de Obstáculos Circulares")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    ax.set_aspect('equal', adjustable='box')
    plt.show()

if __name__ == '__main__':
    AREA_SIZE = (1000, 1000)
    MIN_RADIUS = 25
    MAX_RADIUS = 70
    NUM_OBSTACLES = random.randint(20, 40)
    MIN_MARGIN = 15
    START_POS = (50, 50)  
    END_POS = (950, 950)

    obstacles = generate_obstacles(NUM_OBSTACLES, AREA_SIZE, MIN_RADIUS, MAX_RADIUS, START_POS, END_POS, MIN_MARGIN)
    strategic_points = get_strategic_points(obstacles, START_POS, END_POS)

    print(f"Gerados {len(obstacles)} obstáculos circulares e {len(strategic_points)} pontos estratégicos.")
    
    visualizar_mapa(obstacles, strategic_points, START_POS, END_POS, AREA_SIZE)
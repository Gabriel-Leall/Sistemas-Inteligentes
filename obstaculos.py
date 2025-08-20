import matplotlib.pyplot as plt
from matplotlib.patches import Circle as circulo
import random



def gerar_obj(num_obstacles, area_size, min_raio, max_raio, start_pos, end_pos, margin): 
  obstacles = []

  while len(obstacles) < num_obstacles:
    raio = random.randint(min_raio, max_raio)
    x = random.randint(raio, area_size[0] - raio)
    y = random.randint(raio, area_size[1] - raio)
    novo_obj = (x, y, raio)

    if ponto_no_circulo(start_pos, novo_obj) or ponto_no_circulo(end_pos, novo_obj):
        continue
    
    if not any(circulos_intersect(novo_obj, x, margin) for x in obstacles):
      obstacles.append(novo_obj)

  return obstacles

def circulos_intersect(circulo1, circulo2, margin=0): # se os circulos estão se chocando
  x1, y1, r1 = circulo1
  x2, y2, r2 = circulo2

  distancia_quad = (x1 - x2)**2 + (y1 - y2)**2
  
  raio_quadrado = (r1 + r2 + margin)**2
  
  return distancia_quad <= raio_quadrado

def ponto_no_circulo(point, circulo): # Verifica se o ponto inicial/final está dentro de um círculo
  point_x, point_y = point
  circulo_x, circulo_y, raio = circulo
  
  distancia_quad = (point_x - circulo_x)**2 + (point_y - circulo_y)**2
  
  return distancia_quad <= raio**2

def plotar_ponto(obstacles, start, end):
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

    plt.title("Mapa de Obstáculos")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    ax.set_aspect('equal', adjustable='box')
    plt.show()

if __name__ == '__main__':
    AREA_SIZE = (1000, 1000)
    MIN_raio = 25
    MAX_raio = 90
    NUM_OBSTACLES = random.randint(20, 40)
    MIN_MARGIN = 15
    START_POS = (50, 50)  
    END_POS = (950, 950)

    obstacles = gerar_obj(NUM_OBSTACLES, AREA_SIZE, MIN_raio, MAX_raio, START_POS, END_POS, MIN_MARGIN)
    plotar_pontos = plotar_ponto(obstacles, START_POS, END_POS)

    print(f"Gerados {len(obstacles)} circulos e {len(plotar_pontos)} pontos.")
    
    visualizar_mapa(obstacles, plotar_pontos, START_POS, END_POS, AREA_SIZE)
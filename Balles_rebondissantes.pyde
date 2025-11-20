
NB_BALLS = 12      # On définit le nombre de balles. 
RADIUS   = 20       # On définit le rayon des balles. 
balls    = []       # On créé une liste qui va contenir toutes nos balles. 


# ----------------------------------------------------------
# CLASSE BALL
# - gère position, vitesse, rayon, couleur
# - update() : mouvement + rebond sur les murs
# - draw()   : affichage
# ----------------------------------------------------------
class Ball: # On crée un type d'objet que l'on appelle "Ball" et on va donner différents paramètres à cet objet 
    def __init__(self, x, y, vx, vy, radius, col): #La fonction self sert à créer la balle elle-même. Les paramètres sont ensuite dans l'ordre d'écriture: Position X, Poisition Y, vx pour la vitesse sur l'axe des X
    # vy pour la vitesse sur l'axe des Y, radius pour la rayon et col pour la couleur. 
        self.x = x 
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.col = col

    def update(self):
        # La fonction update permet de faire bouger la balle, ici appelée self. 
        self.x += self.vx #On met la balle en mouvement sur l'axe des X
        self.y += self.vy #On met la balle en mouvement sur l'axe des Y

        # On utilise une condition qui va permettre de reconnaitre si la balle s'approche d'un mur EN HAUT OU EN BAS. 
        if self.x - self.radius < 0 or self.x + self.radius > width:
            self.vx *= -1 # On inverse la vitesse de la balle pour que celle-ci rebondisse. Je ne comprends pas encore comment ça se fait qu'elle fait ça selon un certain angle mais à mon avis ça marche avec la fonction collide.  

        # On utilise une condition qui va permettre de reconnaitre si la balle s'approche d'un mur A GAUCHE OU A DROITE. 
        if self.y - self.radius < 0 or self.y + self.radius > height:
            self.vy *= -1  # On inverse la vitesse de la balle pour que celle-ci rebondisse. Je ne comprends pas encore comment ça se fait qu'elle fait ça selon un certain angle mais à mon avis ça marche avec la fonction collide.

    def draw(self):
        fill(self.col)
        circle(self.x, self.y, self.radius * 2)


# ----------------------------------------------------------
# COLLISION ENTRE DEUX BALLES
# - test : distance < somme des rayons
# - si collision : échange des vitesses + séparation
# ----------------------------------------------------------
def collide(b1, b2):
    dx = b2.x - b1.x
    dy = b2.y - b1.y
    d  = (dx*dx + dy*dy) ** 0.5  # distance entre centres

    if d > 0 and d < b1.radius + b2.radius:
        # échange simple des vitesses (choc élastique approximatif)
        b1.vx, b2.vx = b2.vx, b1.vx
        b1.vy, b2.vy = b2.vy, b1.vy

        # séparation pour éviter qu'elles restent collées
        overlap = (b1.radius + b2.radius) - d
        nx = dx / d
        ny = dy / d
        b1.x -= nx * overlap / 2.0
        b1.y -= ny * overlap / 2.0
        b2.x += nx * overlap / 2.0
        b2.y += ny * overlap / 2.0


# ----------------------------------------------------------
# SETUP : appelé une seule fois au lancement
# ----------------------------------------------------------
def setup():
    size(800, 600)
    noStroke()
    frameRate(60)

    # création des balles avec positions / vitesses / couleurs aléatoires
    for i in range(NB_BALLS):
        x  = random(RADIUS, width - RADIUS)
        y  = random(RADIUS, height - RADIUS)
        vx = random(-3, 3)
        vy = random(-3, 3)
        col = color(random(50, 255), random(50, 255), random(50, 255))
        balls.append(Ball(x, y, vx, vy, RADIUS, col))


# ----------------------------------------------------------
# DRAW : boucle d'animation appelée en continu
# ----------------------------------------------------------
def draw():
    background(0)

    # mise à jour de toutes les balles
    for b in balls:
        b.update()

    # collisions entre toutes les paires de balles
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            collide(balls[i], balls[j])

    # affichage
    for b in balls:
        b.draw()

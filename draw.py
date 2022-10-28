#! /usr/bin/env python3
import approximate_pi
"""Module graphique du projet BPI"""


def genere_liste_points(n, taille):
    """Retourne une liste composée de ⌊n/10⌋ points(x,y)
    avec x appartenant à [-⌊taille/2⌋,⌊taille/2⌋] et y appartenant à [-⌊taille/2⌋,⌊taille/2⌋]
    x et y sont entiers
    Retourne aussi l'approximation de pi obtenue à partir de ces points"""
    liste_points = []
    compteur = 0  # compte les points dans le cercle
    for _ in range(int(n/10)):
        point = approximate_pi.point_aleatoire()
        compteur += int(approximate_pi.appartient_cercle(point))
        point = (round(point[0]*taille/2), round(point[1]*taille/2))
        liste_points.append(point)
    return liste_points, 4*compteur/int(n/10)


# ne pas passer par une liste intermédiaire: directement stocker les points dans la string utilisée par le fichier ppm

def generate_ppm_file(taille, n, nb_chiffre):
    """
    Génère un fichier ppm de fond blanc
    taille>=100
    n>=100
    1<=nb_chiffre<=5
    Les 3 paramètres sont des entiers"""
    liste_pi = []  # contient les valeurs estimées de pi
    for i in range(10):
        liste_points, approx_pi = genere_liste_points(n, taille)
        liste_pi.append(approx_pi)
        # on ne garde que le nombre de chiffres voulu
        approx_pi = int((approx_pi)e(nb_chiffre))e(-nb_chiffre)
        with open(f"img{i}_{int(approx_pi)-{approx_pi-int(approx_pi)}}", "w", encoding="UTF-8") as img:
            img.write(f"P3\n{taille} {taille}\n1")


print(genere_liste_points(100000, 6))

#! /usr/bin/env python3
"""Module d'approximation de pi du projet BPI"""
from random import uniform
from sys import argv


def point_aleatoire():
    """Génère et retourne les coordonnées d'un point (x,y)
    avec x appartenant à [-1,1] et y appartenant à [-1,1]
    sous la forme d'un couple"""
    return (uniform(-1, 1), uniform(-1, 1))


def appartient_cercle(point):
    """Retourne vrai si le point se situe dans le disque unitaire.
    point est un couple (x,y) avec x appartenant à [-1,1] et y appartenant à [-1,1]"""
    return (point[0]**2+point[1]**2) <= 1


def approximation_pi(n):
    """Approximation de pi à l'aide de la méthode de Monte-Carlo en utilisant n points"""
    compteur = 0
    for _ in range(n):
        compteur += int(appartient_cercle(point_aleatoire()))
    # compteur/n correspond à une approximation de l'aire du disque divisé par l'aire du carré,
    # soit pi/4 ici
    return 4*compteur/n


def main():
    """Renvoie une approximation de pi à l'aide de la méthode de Monte-Carlo
    en utilisant le nombre de points indiqués en argument"""
    if len(argv) != 2:
        print(
            "usage: approximate_pi.py n "
        )
        exit(1)
    else:
        print(approximation_pi(int(argv[1])))


if __name__ == "__main__":
    main()

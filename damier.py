import turtle
taille_case = 50
nb_lignes = 10
marge = 10

fenetre = turtle.Screen()
fenetre.title("Jeu De Dames")
tortue = turtle.Turtle()
tortue.speed(0)

def dessine_carre(x,y,couleur) :
	tortue.goto(x,y)
	tortue.pendown
	tortue.fillcolor(couleur)
	tortue.begin_fill()
	for _ in range(4):
		tortue.forward(taille_case)
		tortue.right(90)
	tortue.end_fill()
	tortue.penup()
def dessine_pion(x,y,couleur) :
	rayon = taille_case/2 - marge 
	centre_x = x + taille_case / 2
	centre_y = y + taille_case / 2
	tortue.goto(centre_x,centre_y-rayon)
	tortue.fillcolor(couleur)
	tortue.begin_fill()
	tortue.circle(rayon)
	tortue.end_fill()

for ligne in range(nb_lignes) :
	for colonne in range(nb_lignes) :
	
		if (ligne + colonne) % 2 == 0 :
			couleur = "brown"
		else :
			couleur = "black"
		x = colonne * taille_case - (nb_lignes * taille_case) / 2
		y = (nb_lignes * taille_case)/2 -  (ligne * taille_case)
		dessine_carre(x,y,couleur)
		if couleur == "white":
			if ligne < 3 :
				dessine_pion(x,y,"red")
			elif ligne > 6 :
				dessine_pion(x,y,"blue")
tortue.hideturtle()
fenetre.mainloop()

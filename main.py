import turtle

# Créer une fenêtre et une tortue
t = turtle.Turtle()
def escalier(taille,nb):
    for i in range(0,nb) :   
        t.forward(taille) #avance 
        t.left(90) #tourne gauche en degre 
        t.forward(taille) #avance 
        t.right(90) #tourne droit en degre
        # taille=taille-10
        taille-=10               
    t.forward(taille)

def carre(taille):
    for i in range(0,4):
        t.forward(taille)
        t.left(90) 
def carres(taille_depart,nb):
    for i in range (1,nb) :
        taille = i * taille_depart
        carre(taille)
        
    
   
# escalier(60,5)
carres(10,10)


# Garder la fenêtre ouverte
turtle.done()
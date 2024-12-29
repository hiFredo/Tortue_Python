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
    
escalier(60,5)
# Garder la fenêtre ouverte
turtle.done()

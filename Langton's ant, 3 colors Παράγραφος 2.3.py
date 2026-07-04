import turtle as tl
def lagton():
    #Δημιουργούμε το παράθυρο και το μυρμήγκι 
    tab=tl.Screen()
    tab.bgcolor("white")
    tab.title("Lagton's Ant")
    ant=tl.Turtle()
    ant.shape("square")
    ant.shapesize(0.2,0.2)
    ant.speed('fastest')        
    ant.penup() 
    #δημιουργούμε ενα λεξίκο στο οποίο αποθήκουμε το χρώμα το οποιο ερχει κάθε σημείο που έχει περάσει το μυρμήγκι 
    cordinates_of_the_ant={}
    #Προγραμματίζουμε τους κανόνες που έχει το παιχνίδι 
    while True:
        ants_position=coordinate(ant)
        if ants_position not in cordinates_of_the_ant or cordinates_of_the_ant[ants_position]=="white" :
            ant.fillcolor("#FF0000")
            ant.stamp()
            ant.right(90)   
            ant.forward(4)
            cordinates_of_the_ant[ants_position]="red"
        elif cordinates_of_the_ant[ants_position]=="red":
            ant.fillcolor("#000000")
            ant.stamp()
            ant.left(45)
            ant.forward(5.6568)#το νούμερο δεν ειναι τυχαίο αλλα ειναι το μηκός της υποτείνουσας που δημιουργείται απο τις δυο κάθετες πλεύρες(4)
            ant.left(45)
            cordinates_of_the_ant[ants_position]="black "
        elif cordinates_of_the_ant[ants_position]=="black ":
            ant.fillcolor("#FFFFFF")
            ant.stamp()
            ant.left(90)
            ant.forward(4)
            cordinates_of_the_ant[ants_position]="white"
#μια συνάρτηση η οποία μας δίνει τις συντεταγμένες του σημειου που βρίσκεται το μυρμίγκι 
def coordinate(ant): 
    return (round(ant.xcor()), round(ant.ycor())) 
lagton()
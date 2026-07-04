import turtle as tl
def lagton():
    #Δημιουργούμε το παράθυρο και το μυρμήγκι 
    tab=tl.Screen()
    tab.bgcolor("white")
    tab.title("Lagton's Ant")
    ant1=tl.Turtle()
    ant1.shape("square")
    ant1.shapesize(0.5,0.5)
    ant1.speed('fastest')          
    ant1.penup()
    ant2=tl.Turtle()
    ant2.penup()  
    ant2.left(0)#Aλλάζοντας την εντολη αυτην αλλάξαμε τον προσανατολισμο μεταξυ των 2 μυρμηγκίων 
    ant2.forward(70)#Αλλάζοντας την εντολή αυτην κάναμε τις διάφορεσ δοκιμές για το πόσο των τετραγώνων των οποίων μεταβάλονται μεταξυ των 2 μυρμηγκίων 
    ant2.left(0)#το αλλάζουμε οταν μετακοινούμε το μυρμήγκι ώστε να έχουν και τα δύο τον προσανατολίσμο που θέλούμε 
    ant2.shape("square")
    ant2.shapesize(0.5,0.5)
    ant2.speed('fastest')          
    
    #δημιουργούμε ενα λεξίκο στο οποίο αποθήκουμε το χρώμα το οποιο έχει κάθε σημείο που έχει περάσει το κάθε μυρμήγκι 
    cordinates_of_the_ant={}
    #Προγραμματίζουμε τους κανόνες που έχει το παιχνίδι 
    while True:
        ants_position1=coordinate(ant1)
        ants_position2=coordinate(ant2)
        if ants_position1 not in cordinates_of_the_ant or cordinates_of_the_ant[ants_position1]=="white" :
            ant1.fillcolor("#000000")
            ant1.stamp()
            ant1.right(90)   
            cordinates_of_the_ant[ants_position1]="black"
        elif cordinates_of_the_ant[ants_position1]=="black":
            ant1.fillcolor("#FFFFFF")
            ant1.stamp()
            ant1.left(90)
            cordinates_of_the_ant[ants_position1]="white"
        ant1.forward(10)
        
        if ants_position2 not in cordinates_of_the_ant or cordinates_of_the_ant[ants_position2]=="white" :
            ant2.fillcolor("#000000")
            ant2.stamp()
            ant2.right(90)   
            cordinates_of_the_ant[ants_position2]="black"
        elif cordinates_of_the_ant[ants_position2]=="black":
            ant2.fillcolor("#FFFFFF")
            ant2.stamp()
            ant2.left(90)
            cordinates_of_the_ant[ants_position2]="white"
        ant2.forward(10)
#μια συνάρτηση η οποία μας δίνει τις συντεταγμένες του σημειου που βρίσκεται το μυρμίγκι 
def coordinate(ant): 
    return (round(ant.xcor()), round(ant.ycor())) 
lagton()
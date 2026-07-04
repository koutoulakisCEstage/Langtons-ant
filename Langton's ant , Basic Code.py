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
    ant1.left(90)
    counter_turtle= tl.Turtle()
    counter_turtle.hideturtle()
    counter_turtle.penup()
    counter_turtle.goto(-tab.window_width()//2 + 20, tab.window_height()//2 - 40)
    #δημιουργούμε ενα λεξίκο στο οποίο αποθήκουμε το χρώμα το οποιο ερχει κάθε σημείο που έχει περάσει το μυρμήγκι 
    cordinates_of_the_ant={}
    counter_turtle.speed(999999999)
    steps=0
    #Προγραμματίζουμε τους κανόνες που έχει το παιχνίδι 
    while True:
        ants_position=coordinate(ant1)
        counter_turtle.clear() 
        counter_turtle.write(f"Steps: {steps}", align="left", font=("Arial", 16, "normal"))
        #Eλέχνει αν το χρώμα στο οποίο βρισκέται ειναι άσπρο 
        if ants_position not in cordinates_of_the_ant or cordinates_of_the_ant[ants_position]=="white" :
            #αλλαζει το χρώμα του μυρμηγκίου απο ασπρό σε μαύρο χρώμα  
            ant1.fillcolor("#000000")
            #γεμίζει το τετράγωνο με το χρώμα που εχει δώσει παραπανω στο μυρμηγκι 
            ant1.stamp()
            #στριβεί δεξία 90 μοίρες
            ant1.right(90)   
            #Εισάγει στο λεξίκο τήν θέση απο την οποία πέρασε και το χρώμα που της έδωσε 
            cordinates_of_the_ant[ants_position]="black"
        elif cordinates_of_the_ant[ants_position]=="black":
            ant1.fillcolor("#FFFFFF")
            ant1.stamp()
            ant1.left(90)
            cordinates_of_the_ant[ants_position]="white"
        ant1.forward(10)
        steps+=1
#μια συνάρτηση η οποία μας δίνει τις συντεταγμένες του σημειου που βρίσκεται το μυρμηγκι 
def coordinate(ant): 
    return (round(ant.xcor()), round(ant.ycor())) 
lagton()
import turtle, random
t=turtle.Turtle()
t.penup()
t.hideturtle()

#kolory przypisane do symboli

cclub = "black"
cheart = "red"
cspade = "black"
cdiamond = "red"

#variable przyjmujace kolor i symbol

kolor_graf = "" #kolor karty na grafice
symbol_graf = ""    #symbol karty na grafice

#variable ustawiajace koordynat X

x1 = "" #150
x2 = "" #200
x3 = "" #250
x4 = "" #220
x5 = "" #180
x6 = "" #185

#funkcje do rysowania symboli

def sclub():
    t.speed(100)
    t.pendown()
    t.left(180)
    t.circle(10)
    t.left(90)
    t.circle(10)
    t.left(45)
    t.forward(10)
    t.right(90)
    t.circle(10)
    t.left(45)
    t.forward(30)
    t.right(270)
    t.penup()


def sheart():
    t.speed(100)
    t.pendown()
    t.left(60)
    t.circle(10,200)
    t.right(150)
    t.circle(10,200)
    t.forward(30)
    t.left(109)
    t.forward(30)
    t.right(59)
    t.penup()


def sspade():
    t.speed(100)
    t.pendown()
    t.left(180)
    t.left(60)
    t.circle(10,200)
    t.right(170)
    t.forward(20)
    t.left(180)
    t.forward(20)
    t.right(160)
    t.circle(10,200)
    t.forward(30)
    t.left(109)
    t.forward(30)
    t.right(239)
    t.penup()


def sdiamond():
    t.speed(100)
    t.pendown()
    t.left(45)
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.left(45)
    t.penup()

def sjoker():
  t.goto(x4,50)
  t.pendown()
  t.forward(40)
  t.right(90)
  t.forward(100)
  t.right(90)
  t.penup()
  t.forward(40)
  t.left(90)
  t.pendown()
  t.circle(20,200)
  t.right(110)
  t.penup()

def sking():
  t.goto(x4,0)
  t.left(45)
  t.pendown()
  t.forward(60)
  t.right(180)
  t.forward(60)
  t.left(90)
  t.forward(60)
  t.right(180)
  t.forward(60)
  t.right(45)
  t.forward(45)
  t.right(180)
  t.forward(90)
  t.left(90)
  t.penup()

def squeen():
    t.goto(x5,20)
    t.left(90)
    t.pendown()
    t.circle(20,180)
    t.forward(40)
    t.circle(20,180)
    t.forward(40)
    t.penup()
    t.goto(x6,-35)
    t.right(135)
    t.pendown()
    t.forward(30)
    t.left(45)
    t.penup()


#funkcja rysujaca podany symbol

def rys_symbolu():
    
    if symbol_graf == "diamond":
        t.right(90)
        t.forward(10)
        t.left(90)
        t.pendown()
        sdiamond()

    elif symbol_graf == "spade":
        t.backward(20)
        t.pendown()
        sspade()

    elif symbol_graf == "heart":
        t.forward(15)
        t.pendown()
        sheart()

    elif symbol_graf == "club":
        t.backward(10)
        t.pendown()
        sclub()
    t.penup()

#funkcje zarzadzajace tym jak symbole beda rozmieszczone (na podstawie rodzaju)
#sX: X - rodzaj (ile symboli np 2,3 lub nazwa specjalna np. ace)

#2
def s2(): 
    t.color(kolor_graf)
    t.goto(x2,150)
    rys_symbolu()
    t.goto(x2,-150)
    rys_symbolu()



#3
def s3():
    t.color(kolor_graf)
    t.goto(x2,150)
    rys_symbolu()
    t.goto(x2,0)
    rys_symbolu()
    t.goto(x2,-150)
    rys_symbolu()

#4
def s4():
    t.color(kolor_graf)
    t.goto(x3,150)
    rys_symbolu()
    t.goto(x1,150)
    rys_symbolu()
    t.goto(x3,-150)
    rys_symbolu()
    t.goto(x1,-150)
    rys_symbolu()

#5
def s5():
    t.color(kolor_graf)
    t.goto(x3,150)
    rys_symbolu()
    t.goto(x1,150)
    rys_symbolu()
    t.goto(x3,-150)
    rys_symbolu()
    t.goto(x1,-150)
    rys_symbolu()
    t.goto(x2,0)
    rys_symbolu()

#6
def s6():
    t.color(kolor_graf)
    t.goto(x3,150)
    rys_symbolu()
    t.goto(x1,150)
    rys_symbolu()
    t.goto(x3,-150)
    rys_symbolu()
    t.goto(x1,-150)
    rys_symbolu()
    t.goto(x1,0)
    rys_symbolu()
    t.goto(x3,0)
    rys_symbolu()

#7
def s7():
    t.color(kolor_graf)
    t.goto(x3,150)
    rys_symbolu()
    t.goto(x1,150)
    rys_symbolu()
    t.goto(x3,-150)
    rys_symbolu()
    t.goto(x1,-150)
    rys_symbolu()
    t.goto(x1,0)
    rys_symbolu()
    t.goto(x3,0)
    rys_symbolu()
    t.goto(x2,75)
    rys_symbolu()
   

#8
def s8():
    t.color(kolor_graf)
    t.goto(x3,150)
    rys_symbolu()
    t.goto(x1,150)
    rys_symbolu()
    t.goto(x3,-150)
    rys_symbolu()
    t.goto(x1,-150)
    rys_symbolu()
    t.goto(x1,0)
    rys_symbolu()
    t.goto(x3,0)
    rys_symbolu()
    t.goto(x2,60)
    rys_symbolu()
    t.goto(x2,-60)
    rys_symbolu()

#9
def s9():
    t.color(kolor_graf)
    t.goto(x3,150)
    rys_symbolu()
    t.goto(x1,150)
    rys_symbolu()
    t.goto(x3,-150)
    rys_symbolu()
    t.goto(x1,-150)
    rys_symbolu()
    t.goto(x3,60)
    rys_symbolu()
    t.goto(x3,-60)
    rys_symbolu()
    t.goto(x1,60)
    rys_symbolu()
    t.goto(x1,-60)
    rys_symbolu()
    t.goto(x2,0)
    rys_symbolu()

#10
def s10():
    t.color(kolor_graf)
    t.goto(x3,150)
    rys_symbolu()
    t.goto(x1,150)
    rys_symbolu()
    t.goto(x3,-150)
    rys_symbolu()
    t.goto(x1,-150)
    rys_symbolu()
    t.goto(x3,60)
    rys_symbolu()
    t.goto(x3,-60)
    rys_symbolu()
    t.goto(x1,60)
    rys_symbolu()
    t.goto(x1,-60)
    rys_symbolu()
    t.goto(x2,105)
    rys_symbolu()
    t.goto(x2,-105)
    rys_symbolu()

#ace
def sA():
    t.color(kolor_graf)
    t.goto(x2,0)
    rys_symbolu()

#joker
def sJ():
  t.color(kolor_graf)
  t.goto(x3,150)
  rys_symbolu()
  t.goto(x1,-150)
  rys_symbolu()
  sjoker()

#king
def sK():
  t.color(kolor_graf)
  t.goto(x3,150)
  rys_symbolu()
  t.goto(x1,-150)
  rys_symbolu()
  sking()

#queen
def sQ():
    t.color(kolor_graf)
    t.goto(x3,150)
    rys_symbolu()
    t.goto(x1,-150)
    rys_symbolu()
    squeen()



#przypisywanie wybranego rodzaju do komendy rysujacej

def rodzaj_graf():
    if wybor_rodzaj == 2:
        s2()
    elif wybor_rodzaj == 3:
        s3()
    elif wybor_rodzaj == 4:
        s4()
    elif wybor_rodzaj == 5:
        s5()
    elif wybor_rodzaj == 6:
        s6()
    elif wybor_rodzaj == 7:
        s7()
    elif wybor_rodzaj == 8:
        s8()
    elif wybor_rodzaj == 9:
        s9()
    elif wybor_rodzaj == 10:
        s10()
    elif wybor_rodzaj == "Joker":
        sJ()
    elif wybor_rodzaj == "Queen":
        sQ()
    elif wybor_rodzaj == "King":
        sK()
    elif wybor_rodzaj == "Ace":
        sA()
        



#rysowanie templatow pod karty

#karta1
t.pendown()
t.speed(100)
t.penup()
t.goto(-300,-200)
t.left(90)
t.pendown()
t.forward(400)
t.right(90)
t.forward(200)
t.right(90)
t.forward(400)
t.right(90)
t.forward(200)
t.penup()

#srodek karty 1 = t.goto(-200,0)


#karta2
t.pendown()
t.speed(100)
t.penup()
t.goto(300,200)
t.left(90)
t.pendown()
t.forward(400)
t.right(90)
t.forward(200)
t.right(90)
t.forward(400)
t.right(90)
t.forward(200)
t.penup()

#srodek karty 2 = t.goto(200,0)

#funkcje ustawiajace koordynat x


#listy rodzajow i kolorow do losowania

rodzaje = [2,3,4,5,6,7,8,9,10,"Joker","Queen","King","Ace"]
kolor = ["club","heart","diamond","spade"]

#wybieranie 1 karty

t.penup()
wybor_kolor = random.choice(kolor)
wybor_rodzaj = random.choice(rodzaje)


if wybor_kolor == "club":
    print(wybor_rodzaj,"club")
       
    kolor_graf = cclub
    symbol_graf = "club"
    x1 = -150
    x2 = -200
    x3 = -250
    x4 = -220
    x5 = -180
    x6 = -185
    rodzaj_graf()

if wybor_kolor == "heart":
    print(wybor_rodzaj,"heart")

    kolor_graf = cheart
    symbol_graf = "heart"
    x1 = -150
    x2 = -200
    x3 = -250
    x4 = -220
    x5 = -180
    x6 = -185
    rodzaj_graf()


if wybor_kolor == "diamond":
    print(wybor_rodzaj,"diamond")

    kolor_graf = cdiamond
    symbol_graf = "diamond"
    x1 = -150
    x2 = -200
    x3 = -250
    x4 = -220
    x5 = -180
    x6 = -185
    rodzaj_graf()


if wybor_kolor == "spade":
    print(wybor_rodzaj,"spade")

    kolor_graf = cspade
    symbol_graf = "spade"
    x1 = -150
    x2 = -200
    x3 = -250
    x4 = -220
    x5 = -180
    x6 = -185
    rodzaj_graf()
   
#pobieranie karty (aby zapobiec powtorkom)
check1 = wybor_kolor
check2 = wybor_rodzaj

#wybieranie 2 karty

t.penup()
wybor_kolor = random.choice(kolor)
wybor_rodzaj = random.choice(rodzaje)

while wybor_kolor == check1 and wybor_rodzaj == check2:
    wybor_kolor = random.choice(kolor)
    wybor_rodzaj = random.choice(rodzaje)

if wybor_kolor == "club":
    print(wybor_rodzaj,"club")
       
    kolor_graf = cclub
    symbol_graf = "club"
    x1 = 150
    x2 = 200
    x3 = 250
    x4 = 180
    x5 = 225
    x6 = 220
    rodzaj_graf()

if wybor_kolor == "heart":
    print(wybor_rodzaj,"heart")

    kolor_graf = cheart
    symbol_graf = "heart"
    x1 = 150
    x2 = 200
    x3 = 250
    x4 = 180
    x5 = 225
    x6 = 220
    rodzaj_graf()


if wybor_kolor == "diamond":
    print(wybor_rodzaj,"diamond")

    kolor_graf = cdiamond
    symbol_graf = "diamond"
    x1 = 150
    x2 = 200
    x3 = 250
    x4 = 180
    x5 = 225
    x6 = 220
    rodzaj_graf()


if wybor_kolor == "spade":
    print(wybor_rodzaj,"spade")

    kolor_graf = cspade
    symbol_graf = "spade"
    x1 = 150
    x2 = 200
    x3 = 250
    x4 = 180
    x5 = 225
    x6 = 220
    rodzaj_graf()
    
turtle.exitonclick()
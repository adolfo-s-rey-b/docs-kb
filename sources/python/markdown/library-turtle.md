### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/development.html "Development Tools")
     |
*   [previous](https://docs.python.org/3/library/idle.html "IDLE — Python editor and shell")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [Graphical user interfaces with Tk](https://docs.python.org/3/library/tk.html)
     »
*   [`turtle` — Turtle graphics](https://docs.python.org/3/library/turtle.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`turtle` — Turtle graphics[¶](https://docs.python.org/3/library/turtle.html#module-turtle "Link to this heading")

==================================================================================================================

**Source code:** [Lib/turtle.py](https://github.com/python/cpython/tree/3.15/Lib/turtle.py)

* * *

Imagine a robotic turtle starting at (0, 0) in the x-y plane. After an `import turtle`, give it the command `turtle.forward(15)`, and it moves (on-screen!) 15 pixels in the direction it is facing, drawing a line as it moves. Give it the command `turtle.right(25)`, and it rotates in-place 25 degrees clockwise.

Turtle graphics is an implementation of [the drawing tools introduced in Logo](https://en.wikipedia.org/wiki/Turtle_(robot))
 in 1967. It was created as an educational tool, and its instant, visible feedback makes it an effective way for learners to encounter programming concepts. It is also a convenient way to produce simple graphical output without bringing in external libraries.

This document includes four main sections:

*   [Tutorial](https://docs.python.org/3/library/turtle.html#turtle-tutorial)
     teaches the basics of turtle drawing.
    
*   [Reference](https://docs.python.org/3/library/turtle.html#turtle-reference)
     describes the functions, methods and classes this module defines.
    
*   [How-to guides](https://docs.python.org/3/library/turtle.html#turtle-howtos)
     detail how to handle specific tasks.
    
*   [Explanation](https://docs.python.org/3/library/turtle.html#turtle-explanation)
     provides background on the object-oriented interface.
    

Note

Turtle graphics requires the [`tkinter`](https://docs.python.org/3/library/tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces")
 [optional module](https://docs.python.org/3/glossary.html#term-optional-module)
. The python.org installers for Windows and macOS include it, but some Linux distributions and other platforms may package it separately. If `import turtle` fails with an error mentioning `_tkinter`, look for documentation from your distributor (that is, whoever provided Python to you). Check this in advance if you’re planning to use turtle graphics with a learner.

Tutorial[¶](https://docs.python.org/3/library/turtle.html#tutorial "Link to this heading")

-------------------------------------------------------------------------------------------

New users should start here. In this tutorial we’ll explore some of the basics of turtle drawing.

### Starting a turtle environment[¶](https://docs.python.org/3/library/turtle.html#starting-a-turtle-environment "Link to this heading")

In a Python shell, import all the objects of the `turtle` module:

Copy

from turtle import \*

If you run into a `Standard library module '_tkinter' was not found` error, you’ll have to install the [`Tk interface package`](https://docs.python.org/3/library/tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces")
 on your system.

Nothing appears yet. To open the turtle window, make the turtle visible:

Copy

showturtle()

A new window opens, with the turtle in the middle, shown as an arrow heading East.

### Basic drawing[¶](https://docs.python.org/3/library/turtle.html#basic-drawing "Link to this heading")

Send the turtle forward 100 steps:

Copy

forward(100)

You should see a line drawn by the turtle, heading East. Change the direction of the turtle, so that it turns 120 degrees left (anti-clockwise):

Copy

left(120)

Let’s continue by drawing a triangle:

Copy

forward(100)
left(120)
forward(100)

Notice how the turtle, represented by an arrow, points in different directions as you steer it.

Experiment with those commands, and also with `backward()` and `right()`. Many commands also have shorter aliases, such as `fd()` for [`forward()`](https://docs.python.org/3/library/turtle.html#turtle.forward "turtle.forward")
.

#### Pen control[¶](https://docs.python.org/3/library/turtle.html#pen-control "Link to this heading")

Try changing the color - for example, `color('blue')` - and width of the line - for example, `width(3)` - and then drawing again.

You can also move the turtle around without drawing, by lifting up the pen: `up()` before moving. To start drawing again, use `down()`.

#### The turtle’s position[¶](https://docs.python.org/3/library/turtle.html#the-turtle-s-position "Link to this heading")

Send your turtle back to its starting-point (useful if it has disappeared off-screen):

Copy

home()

The home position is at the center of the turtle’s screen. If you ever need to know them, get the turtle’s x-y coordinates with:

Copy

pos()

Home is at `(0, 0)`.

And after a while, it will probably help to clear the window so we can start anew:

Copy

clearscreen()

### Making algorithmic patterns[¶](https://docs.python.org/3/library/turtle.html#making-algorithmic-patterns "Link to this heading")

Using loops, it’s possible to build up geometric patterns:

Copy

for steps in range(100):
    for c in ('blue', 'red', 'green'):
        color(c)
        forward(steps)
        right(30)

\- which of course, are limited only by the imagination!

Let’s draw the star shape at the top of this page. We want red lines, filled in with yellow:

Copy

color('red')
fillcolor('yellow')

Just as `up()` and `down()` determine whether lines will be drawn, filling can be turned on and off:

Copy

begin\_fill()

Next we’ll create a loop:

Copy

start \= pos()

while True:
    forward(200)
    left(170)
    if distance(start) < 1:
        break

`distance(start) < 1` is a good way to know when the turtle is back at its start position.

Finally, complete the filling:

Copy

end\_fill()

(Note that filling only actually takes place when you give the `end_fill()` command.)

Reference[¶](https://docs.python.org/3/library/turtle.html#reference "Link to this heading")

---------------------------------------------------------------------------------------------

### Turtle methods and functions[¶](https://docs.python.org/3/library/turtle.html#turtle-methods-and-functions "Link to this heading")

Most of the examples in this section refer to a Turtle instance called `turtle`.

#### Move and draw[¶](https://docs.python.org/3/library/turtle.html#move-and-draw "Link to this heading")

turtle.forward(_distance_)[¶](https://docs.python.org/3/library/turtle.html#turtle.forward "Link to this definition")

turtle.fd(_distance_)[¶](https://docs.python.org/3/library/turtle.html#turtle.fd "Link to this definition")

Parameters:

**distance** – a number

Move the turtle forward by the specified _distance_, in the direction the turtle is headed.

Copy

\>>> turtle.position()
(0.00,0.00)
\>>> turtle.forward(25)
\>>> turtle.position()
(25.00,0.00)
\>>> turtle.forward(\-75)
\>>> turtle.position()
(-50.00,0.00)

turtle.back(_distance_)[¶](https://docs.python.org/3/library/turtle.html#turtle.back "Link to this definition")

turtle.bk(_distance_)[¶](https://docs.python.org/3/library/turtle.html#turtle.bk "Link to this definition")

turtle.backward(_distance_)[¶](https://docs.python.org/3/library/turtle.html#turtle.backward "Link to this definition")

Parameters:

**distance** – a number

Move the turtle backward by _distance_, opposite to the direction the turtle is headed. The turtle’s heading does not change.

Copy

\>>> turtle.position()
(0.00,0.00)
\>>> turtle.backward(30)
\>>> turtle.position()
(-30.00,0.00)

turtle.right(_angle_)[¶](https://docs.python.org/3/library/turtle.html#turtle.right "Link to this definition")

turtle.rt(_angle_)[¶](https://docs.python.org/3/library/turtle.html#turtle.rt "Link to this definition")

Parameters:

**angle** – a number

Turn the turtle right by the specified _angle_. The angle is measured in degrees by default; the unit can be changed with [`degrees()`](https://docs.python.org/3/library/turtle.html#turtle.degrees "turtle.degrees")
 or [`radians()`](https://docs.python.org/3/library/turtle.html#turtle.radians "turtle.radians")
. How the heading is measured depends on the turtle mode, see [`mode()`](https://docs.python.org/3/library/turtle.html#turtle.mode "turtle.mode")
.

Copy

\>>> turtle.heading()
22.0
\>>> turtle.right(45)
\>>> turtle.heading()
337.0

turtle.left(_angle_)[¶](https://docs.python.org/3/library/turtle.html#turtle.left "Link to this definition")

turtle.lt(_angle_)[¶](https://docs.python.org/3/library/turtle.html#turtle.lt "Link to this definition")

Parameters:

**angle** – a number

Turn the turtle left by the specified _angle_. The angle is measured in degrees by default; the unit can be changed with [`degrees()`](https://docs.python.org/3/library/turtle.html#turtle.degrees "turtle.degrees")
 or [`radians()`](https://docs.python.org/3/library/turtle.html#turtle.radians "turtle.radians")
. How the heading is measured depends on the turtle mode, see [`mode()`](https://docs.python.org/3/library/turtle.html#turtle.mode "turtle.mode")
.

Copy

\>>> turtle.heading()
22.0
\>>> turtle.left(45)
\>>> turtle.heading()
67.0

turtle.goto(_x_, _y\=None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.goto "Link to this definition")

turtle.setpos(_x_, _y\=None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.setpos "Link to this definition")

turtle.setposition(_x_, _y\=None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.setposition "Link to this definition")

Parameters:

*   **x** – a number or a pair/vector of numbers
    
*   **y** – a number or `None`
    

Move the turtle to an absolute position. If _y_ is `None`, _x_ must be a pair of coordinates or a [`Vec2D`](https://docs.python.org/3/library/turtle.html#turtle.Vec2D "turtle.Vec2D")
, for example as returned by [`pos()`](https://docs.python.org/3/library/turtle.html#turtle.pos "turtle.pos")
. If the pen is down, a line is drawn. The turtle’s heading does not change.

Copy

\>>> tp \= turtle.pos()
\>>> tp
(0.00,0.00)
\>>> turtle.goto(60,30)
\>>> turtle.pos()
(60.00,30.00)
\>>> turtle.goto((20,80))
\>>> turtle.pos()
(20.00,80.00)
\>>> turtle.goto(tp)
\>>> turtle.pos()
(0.00,0.00)

turtle.teleport(_x\=None_, _y\=None_, _\*_, _fill\_gap\=False_)[¶](https://docs.python.org/3/library/turtle.html#turtle.teleport "Link to this definition")

Parameters:

*   **x** – a number or `None`
    
*   **y** – a number or `None`
    
*   **fill\_gap** – a boolean
    

Teleport, or instantly move, the turtle to an absolute position. Unlike [`goto()`](https://docs.python.org/3/library/turtle.html#turtle.goto "turtle.goto")
, no line is drawn. If _x_ or _y_ is not given, that coordinate is kept as it is. The turtle’s heading does not change.

If the turtle is filling a shape, the shape drawn so far is finished and filled before teleporting, and filling starts again at the new position. Pass `fill_gap=True` to keep filling one shape instead. The teleport then counts as an edge of the shape, as it would with [`goto()`](https://docs.python.org/3/library/turtle.html#turtle.goto "turtle.goto")
.

Copy

\>>> tp \= turtle.pos()
\>>> tp
(0.00,0.00)
\>>> turtle.teleport(60)
\>>> turtle.pos()
(60.00,0.00)
\>>> turtle.teleport(y\=10)
\>>> turtle.pos()
(60.00,10.00)
\>>> turtle.teleport(20, 30)
\>>> turtle.pos()
(20.00,30.00)

Added in version 3.12.

turtle.setx(_x_)[¶](https://docs.python.org/3/library/turtle.html#turtle.setx "Link to this definition")

Parameters:

**x** – a number

Set the turtle’s x coordinate to _x_. The y coordinate is unchanged.

Copy

\>>> turtle.position()
(0.00,240.00)
\>>> turtle.setx(10)
\>>> turtle.position()
(10.00,240.00)

turtle.sety(_y_)[¶](https://docs.python.org/3/library/turtle.html#turtle.sety "Link to this definition")

Parameters:

**y** – a number

Set the turtle’s y coordinate to _y_. The x coordinate is unchanged.

Copy

\>>> turtle.position()
(0.00,40.00)
\>>> turtle.sety(\-10)
\>>> turtle.position()
(0.00,-10.00)

turtle.setheading(_to\_angle_)[¶](https://docs.python.org/3/library/turtle.html#turtle.setheading "Link to this definition")

turtle.seth(_to\_angle_)[¶](https://docs.python.org/3/library/turtle.html#turtle.seth "Link to this definition")

Parameters:

**to\_angle** – a number

Set the turtle’s heading to _to\_angle_. Here are some common directions in degrees:

| standard mode | logo mode |
| --- | --- |
| 0 - east | 0 - north |
| 90 - north | 90 - east |
| 180 - west | 180 - south |
| 270 - south | 270 - west |

Copy

\>>> turtle.setheading(90)
\>>> turtle.heading()
90.0

turtle.home()[¶](https://docs.python.org/3/library/turtle.html#turtle.home "Link to this definition")

Move the turtle to the origin, coordinates (0,0). The turtle’s heading is set to its start orientation, which depends on the turtle mode, see [`mode()`](https://docs.python.org/3/library/turtle.html#turtle.mode "turtle.mode")
.

Copy

\>>> turtle.heading()
90.0
\>>> turtle.position()
(0.00,-10.00)
\>>> turtle.home()
\>>> turtle.position()
(0.00,0.00)
\>>> turtle.heading()
0.0

turtle.circle(_radius_, _extent\=None_, _steps\=None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.circle "Link to this definition")

Parameters:

*   **radius** – a number
    
*   **extent** – a number or `None`
    
*   **steps** – an integer or `None`
    

Draw a circle with the given _radius_. The center is _radius_ units left of the turtle; _extent_, an angle, determines which part of the circle is drawn. If _extent_ is not given, draw the entire circle. If _extent_ is not a full circle, one endpoint of the arc is the current pen position. Draw the arc in counterclockwise direction if _radius_ is positive, otherwise in clockwise direction. Finally, the turtle’s heading is changed by _extent_.

As the circle is approximated by an inscribed regular polygon, _steps_ determines the number of steps to use. If not given, it will be calculated automatically. May be used to draw regular polygons.

Copy

\>>> turtle.home()
\>>> turtle.position()
(0.00,0.00)
\>>> turtle.heading()
0.0
\>>> turtle.circle(50)
\>>> turtle.position()
(-0.00,0.00)
\>>> turtle.heading()
0.0
\>>> turtle.circle(120, 180)  \# draw a semicircle
\>>> turtle.position()
(0.00,240.00)
\>>> turtle.heading()
180.0

turtle.dot()[¶](https://docs.python.org/3/library/turtle.html#turtle.dot "Link to this definition")

turtle.dot(_size_)

turtle.dot(_color_, _/_)

turtle.dot(_size_, _color_, _/_)

turtle.dot(_size_, _r_, _g_, _b_, _/_)

Parameters:

*   **size** – a positive integer or `None`
    
*   **color** – a colorstring or a numeric color tuple
    

Draw a circular dot with diameter _size_, using _color_. If _size_ is not given, the larger of `pensize + 4` and `2 * pensize` is used. If _color_ is not given, the current pencolor is used.

Copy

\>>> turtle.home()
\>>> turtle.dot()
\>>> turtle.fd(50); turtle.dot(20, "blue"); turtle.fd(50)
\>>> turtle.position()
(100.00,-0.00)
\>>> turtle.heading()
0.0

turtle.stamp()[¶](https://docs.python.org/3/library/turtle.html#turtle.stamp "Link to this definition")

Stamp a copy of the turtle shape onto the canvas and return its id. The stamp is placed at the current turtle position. The returned id can be used to delete the stamp with [`clearstamp()`](https://docs.python.org/3/library/turtle.html#turtle.clearstamp "turtle.clearstamp")
.

Copy

\>>> turtle.color("blue")
\>>> stamp\_id \= turtle.stamp()
\>>> turtle.fd(50)

turtle.clearstamp(_stampid_)[¶](https://docs.python.org/3/library/turtle.html#turtle.clearstamp "Link to this definition")

Parameters:

**stampid** – an integer

Delete the stamp with the given _stampid_. _stampid_ must be the return value of a previous [`stamp()`](https://docs.python.org/3/library/turtle.html#turtle.stamp "turtle.stamp")
 call.

Copy

\>>> turtle.position()
(150.00,-0.00)
\>>> turtle.color("blue")
\>>> astamp \= turtle.stamp()
\>>> turtle.fd(50)
\>>> turtle.position()
(200.00,-0.00)
\>>> turtle.clearstamp(astamp)
\>>> turtle.position()
(200.00,-0.00)

turtle.clearstamps(_n\=None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.clearstamps "Link to this definition")

Parameters:

**n** – an integer or `None`

Delete all or the first or last _n_ of the turtle’s stamps. If _n_ is not given, delete all stamps. If _n_ is positive, delete the first _n_ stamps. If _n_ is negative, delete the last _n_ stamps, so -2 deletes the last two.

Copy

\>>> for i in range(8):
...     unused\_stamp\_id \= turtle.stamp()
...     turtle.fd(30)
\>>> turtle.clearstamps(2)
\>>> turtle.clearstamps(\-2)
\>>> turtle.clearstamps()

turtle.undo()[¶](https://docs.python.org/3/library/turtle.html#turtle.undo "Link to this definition")

Undo (repeatedly) the last turtle action(s). Number of available undo actions is determined by the size of the undobuffer.

Copy

\>>> for i in range(4):
...     turtle.fd(50); turtle.lt(80)
...
\>>> for i in range(8):
...     turtle.undo()

turtle.speed(_speed\=None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.speed "Link to this definition")

Parameters:

**speed** – an integer, a string or `None`

Return or set the turtle’s speed. If _speed_ is not given, return the current speed. Otherwise set the turtle’s speed to an integer from 0 to 10. If _speed_ is a number greater than 10 or smaller than 0.5, the speed is set to 0. You can also use these names instead of numbers:

*   “fastest”: 0
    
*   “fast”: 10
    
*   “normal”: 6
    
*   “slow”: 3
    
*   “slowest”: 1
    

Speeds from 1 to 10 give increasingly faster animation of line drawing and turtle turning. A speed of 0 means that no animation takes place: [`forward()`](https://docs.python.org/3/library/turtle.html#turtle.forward "turtle.forward")
 and [`back()`](https://docs.python.org/3/library/turtle.html#turtle.back "turtle.back")
 make the turtle jump, and likewise [`left()`](https://docs.python.org/3/library/turtle.html#turtle.left "turtle.left")
 and [`right()`](https://docs.python.org/3/library/turtle.html#turtle.right "turtle.right")
 make the turtle turn instantly.

Copy

\>>> turtle.speed()
3
\>>> turtle.speed('normal')
\>>> turtle.speed()
6
\>>> turtle.speed(9)
\>>> turtle.speed()
9

#### Tell Turtle’s state[¶](https://docs.python.org/3/library/turtle.html#tell-turtle-s-state "Link to this heading")

turtle.position()[¶](https://docs.python.org/3/library/turtle.html#turtle.position "Link to this definition")

turtle.pos()[¶](https://docs.python.org/3/library/turtle.html#turtle.pos "Link to this definition")

Return the turtle’s current location (x,y) as a [`Vec2D`](https://docs.python.org/3/library/turtle.html#turtle.Vec2D "turtle.Vec2D")
 vector.

Copy

\>>> turtle.pos()
(440.00,-0.00)

turtle.towards(_x_, _y\=None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.towards "Link to this definition")

Parameters:

*   **x** – a number or a pair/vector of numbers or a turtle instance
    
*   **y** – a number if _x_ is a number, else `None`
    

Return the angle of the line from the turtle’s position to (x,y). If _y_ is `None`, _x_ must be a pair of coordinates, a [`Vec2D`](https://docs.python.org/3/library/turtle.html#turtle.Vec2D "turtle.Vec2D")
, for example as returned by [`pos()`](https://docs.python.org/3/library/turtle.html#turtle.pos "turtle.pos")
, or another turtle. The angle is measured from the turtle’s start orientation, which depends on the turtle mode, see [`mode()`](https://docs.python.org/3/library/turtle.html#turtle.mode "turtle.mode")
.

Copy

\>>> turtle.goto(10, 10)
\>>> turtle.towards(0,0)
225.0

turtle.xcor()[¶](https://docs.python.org/3/library/turtle.html#turtle.xcor "Link to this definition")

Return the turtle’s x coordinate.

Copy

\>>> turtle.home()
\>>> turtle.left(50)
\>>> turtle.forward(100)
\>>> turtle.pos()
(64.28,76.60)
\>>> print(round(turtle.xcor(), 5))
64.27876

turtle.ycor()[¶](https://docs.python.org/3/library/turtle.html#turtle.ycor "Link to this definition")

Return the turtle’s y coordinate.

Copy

\>>> turtle.home()
\>>> turtle.left(60)
\>>> turtle.forward(100)
\>>> print(turtle.pos())
(50.00,86.60)
\>>> print(round(turtle.ycor(), 5))
86.60254

turtle.heading()[¶](https://docs.python.org/3/library/turtle.html#turtle.heading "Link to this definition")

Return the turtle’s current heading. The value depends on the turtle mode, see [`mode()`](https://docs.python.org/3/library/turtle.html#turtle.mode "turtle.mode")
.

Copy

\>>> turtle.home()
\>>> turtle.left(67)
\>>> turtle.heading()
67.0

turtle.distance(_x_, _y\=None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.distance "Link to this definition")

Parameters:

*   **x** – a number or a pair/vector of numbers or a turtle instance
    
*   **y** – a number if _x_ is a number, else `None`
    

Return the distance from the turtle to (x,y) in turtle step units. If _y_ is `None`, _x_ must be a pair of coordinates, a [`Vec2D`](https://docs.python.org/3/library/turtle.html#turtle.Vec2D "turtle.Vec2D")
, for example as returned by [`pos()`](https://docs.python.org/3/library/turtle.html#turtle.pos "turtle.pos")
, or another turtle.

Copy

\>>> turtle.home()
\>>> turtle.distance(30,40)
50.0
\>>> turtle.distance((30,40))
50.0
\>>> joe \= Turtle()
\>>> joe.forward(77)
\>>> turtle.distance(joe)
77.0

#### Settings for measurement[¶](https://docs.python.org/3/library/turtle.html#settings-for-measurement "Link to this heading")

turtle.degrees(_fullcircle\=360.0_)[¶](https://docs.python.org/3/library/turtle.html#turtle.degrees "Link to this definition")

Parameters:

**fullcircle** – a number

Set the angle measurement units to degrees. The number of degrees in a full circle is set to _fullcircle_, which defaults to 360.

Copy

\>>> turtle.home()
\>>> turtle.left(90)
\>>> turtle.heading()
90.0

\>>> \# Change angle measurement unit to grad (also known as gon,
\>>> \# grade, or gradian and equals 1/100-th of the right angle.)
\>>> turtle.degrees(400.0)
\>>> turtle.heading()
100.0
\>>> turtle.degrees(360)
\>>> turtle.heading()
90.0

turtle.radians()[¶](https://docs.python.org/3/library/turtle.html#turtle.radians "Link to this definition")

Set the angle measurement units to radians. Equivalent to `degrees(2 * math.pi)`.

Copy

\>>> turtle.home()
\>>> turtle.left(90)
\>>> turtle.heading()
90.0
\>>> turtle.radians()
\>>> turtle.heading()
1.5707963267948966

#### Pen control[¶](https://docs.python.org/3/library/turtle.html#id1 "Link to this heading")

##### Drawing state[¶](https://docs.python.org/3/library/turtle.html#drawing-state "Link to this heading")

turtle.pendown()[¶](https://docs.python.org/3/library/turtle.html#turtle.pendown "Link to this definition")

turtle.pd()[¶](https://docs.python.org/3/library/turtle.html#turtle.pd "Link to this definition")

turtle.down()[¶](https://docs.python.org/3/library/turtle.html#turtle.down "Link to this definition")

Lower the pen. The turtle draws a line when it moves.

turtle.penup()[¶](https://docs.python.org/3/library/turtle.html#turtle.penup "Link to this definition")

turtle.pu()[¶](https://docs.python.org/3/library/turtle.html#turtle.pu "Link to this definition")

turtle.up()[¶](https://docs.python.org/3/library/turtle.html#turtle.up "Link to this definition")

Lift the pen. The turtle does not draw when it moves.

turtle.pensize(_width\=None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.pensize "Link to this definition")

turtle.width(_width\=None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.width "Link to this definition")

Parameters:

**width** – a positive number or `None`

Return or set the line thickness. If _width_ is not given, return the current pensize. If resizemode is set to “auto” and the turtle shape is a polygon, that polygon is drawn with the same line thickness.

Copy

\>>> turtle.pensize()
1
\>>> turtle.pensize(10)   \# from here on lines of width 10 are drawn

turtle.pen(_pen\=None_, _\*\*pendict_)[¶](https://docs.python.org/3/library/turtle.html#turtle.pen "Link to this definition")

Parameters:

*   **pen** – a dictionary or `None`
    
*   **pendict** – keyword arguments with the keys below
    

Return or set the pen’s attributes. The attributes are returned as a dictionary with the following keys and values:

*   “shown”: `True` or `False`
    
*   “pendown”: `True` or `False`
    
*   “pencolor”: a color string or a color tuple
    
*   “fillcolor”: a color string or a color tuple
    
*   “pensize”: a positive number
    
*   “speed”: a number from 0 to 10
    
*   “resizemode”: “auto”, “user” or “noresize”
    
*   “stretchfactor”: a pair of positive numbers
    
*   “shearfactor”: a number
    
*   “outline”: a positive number
    
*   “tilt”: a number
    

Such a dictionary can be passed as _pen_ to restore a former pen state. The attributes can also be given as keyword arguments, which can be used to set several of them in one statement.

Copy

\>>> turtle.pen(fillcolor\="black", pencolor\="red", pensize\=10)
\>>> turtle.pen()
{'shown': True, 'pendown': True, 'pencolor': 'red', 'fillcolor': 'black',
 'pensize': 10, 'speed': 9, 'resizemode': 'noresize',
 'stretchfactor': (1.0, 1.0), 'shearfactor': 0.0, 'outline': 1,
 'tilt': 0.0}
\>>> penstate \= turtle.pen()
\>>> turtle.color("yellow", "")
\>>> turtle.penup()
\>>> turtle.pen()\["pencolor"\]
'yellow'
\>>> \# restore the saved pen state, but with a green fill
\>>> turtle.pen(penstate, fillcolor\="green")
\>>> turtle.pen()\["pencolor"\]
'red'
\>>> turtle.pen()\["fillcolor"\]
'green'

turtle.isdown()[¶](https://docs.python.org/3/library/turtle.html#turtle.isdown "Link to this definition")

Return `True` if the pen is down, `False` if it’s up.

Copy

\>>> turtle.penup()
\>>> turtle.isdown()
False
\>>> turtle.pendown()
\>>> turtle.isdown()
True

##### Color control[¶](https://docs.python.org/3/library/turtle.html#color-control "Link to this heading")

turtle.pencolor()[¶](https://docs.python.org/3/library/turtle.html#turtle.pencolor "Link to this definition")

turtle.pencolor(_color_, _/_)

turtle.pencolor(_r_, _g_, _b_, _/_)

Return or set the pencolor.

Four input formats are allowed:

`pencolor()`

Return the current pencolor as color specification string or as a tuple (see example). May be used as input to another [`color()`](https://docs.python.org/3/library/turtle.html#turtle.color "turtle.color")
, `pencolor()`, [`fillcolor()`](https://docs.python.org/3/library/turtle.html#turtle.fillcolor "turtle.fillcolor")
 or [`bgcolor()`](https://docs.python.org/3/library/turtle.html#turtle.bgcolor "turtle.bgcolor")
 call.

`pencolor(colorstring)`

Set the pencolor to _colorstring_, which is a Tk color specification string, such as `"red"`, `"yellow"`, or `"#33cc8c"`.

`pencolor((r, g, b))`

Set the pencolor to the RGB color represented by the tuple of _r_, _g_, and _b_. Each of _r_, _g_, and _b_ must be between 0 and colormode, where colormode is either 1.0 or 255 (see [`colormode()`](https://docs.python.org/3/library/turtle.html#turtle.colormode "turtle.colormode")
).

`pencolor(r, g, b)`

Set the pencolor to the RGB color represented by _r_, _g_, and _b_. Each of _r_, _g_, and _b_ must be between 0 and colormode.

If the turtle shape is a polygon, the outline of that polygon is drawn with the newly set pencolor.

Copy

\>>> colormode()
1.0
\>>> turtle.pencolor()
'red'
\>>> turtle.pencolor("brown")
\>>> turtle.pencolor()
'brown'
\>>> tup \= (0.2, 0.8, 0.55)
\>>> turtle.pencolor(tup)
\>>> turtle.pencolor()
(0.2, 0.8, 0.5490196078431373)
\>>> colormode(255)
\>>> turtle.pencolor()
(51.0, 204.0, 140.0)
\>>> turtle.pencolor('#32c18f')
\>>> turtle.pencolor()
(50.0, 193.0, 143.0)

turtle.fillcolor()[¶](https://docs.python.org/3/library/turtle.html#turtle.fillcolor "Link to this definition")

turtle.fillcolor(_color_, _/_)

turtle.fillcolor(_r_, _g_, _b_, _/_)

Return or set the fillcolor.

Four input formats are allowed:

`fillcolor()`

Return the current fillcolor as color specification string, possibly in tuple format (see example). May be used as input to another [`color()`](https://docs.python.org/3/library/turtle.html#turtle.color "turtle.color")
, [`pencolor()`](https://docs.python.org/3/library/turtle.html#turtle.pencolor "turtle.pencolor")
, `fillcolor()` or [`bgcolor()`](https://docs.python.org/3/library/turtle.html#turtle.bgcolor "turtle.bgcolor")
 call.

`fillcolor(colorstring)`

Set the fillcolor to _colorstring_, which is a Tk color specification string, such as `"red"`, `"yellow"`, or `"#33cc8c"`.

`fillcolor((r, g, b))`

Set the fillcolor to the RGB color represented by the tuple of _r_, _g_, and _b_. Each of _r_, _g_, and _b_ must be between 0 and colormode, where colormode is either 1.0 or 255 (see [`colormode()`](https://docs.python.org/3/library/turtle.html#turtle.colormode "turtle.colormode")
).

`fillcolor(r, g, b)`

Set the fillcolor to the RGB color represented by _r_, _g_, and _b_. Each of _r_, _g_, and _b_ must be between 0 and colormode.

If the turtle shape is a polygon, the interior of that polygon is drawn with the newly set fillcolor.

Copy

\>>> turtle.fillcolor("violet")
\>>> turtle.fillcolor()
'violet'
\>>> turtle.pencolor()
(50.0, 193.0, 143.0)
\>>> turtle.fillcolor((50, 193, 143))  \# Integers, not floats
\>>> turtle.fillcolor()
(50.0, 193.0, 143.0)
\>>> turtle.fillcolor('#ffffff')
\>>> turtle.fillcolor()
(255.0, 255.0, 255.0)

turtle.color()[¶](https://docs.python.org/3/library/turtle.html#turtle.color "Link to this definition")

turtle.color(_color_, _/_)

turtle.color(_r_, _g_, _b_, _/_)

turtle.color(_pencolor_, _fillcolor_, _/_)

Return or set the pencolor and fillcolor.

Several input formats are allowed. They use 0 to 3 arguments as follows:

`color()`

Return the current pencolor and the current fillcolor as a pair of color specification strings or tuples as returned by [`pencolor()`](https://docs.python.org/3/library/turtle.html#turtle.pencolor "turtle.pencolor")
 and [`fillcolor()`](https://docs.python.org/3/library/turtle.html#turtle.fillcolor "turtle.fillcolor")
.

`color(colorstring)`, `color((r,g,b))`, `color(r,g,b)`

Inputs as in [`pencolor()`](https://docs.python.org/3/library/turtle.html#turtle.pencolor "turtle.pencolor")
. Set both the pencolor and the fillcolor to the given value.

`color(colorstring1, colorstring2)`, `color((r1,g1,b1), (r2,g2,b2))`

Equivalent to `pencolor(colorstring1)` and `fillcolor(colorstring2)` and analogously if the other input format is used.

If the turtle shape is a polygon, the outline and interior of that polygon are drawn with the newly set colors.

Copy

\>>> turtle.color("red", "green")
\>>> turtle.color()
('red', 'green')
\>>> color("#285078", "#a0c8f0")
\>>> color()
((40.0, 80.0, 120.0), (160.0, 200.0, 240.0))

See also: Screen method [`colormode()`](https://docs.python.org/3/library/turtle.html#turtle.colormode "turtle.colormode")
.

##### Filling[¶](https://docs.python.org/3/library/turtle.html#filling "Link to this heading")

turtle.filling()[¶](https://docs.python.org/3/library/turtle.html#turtle.filling "Link to this definition")

Return `True` if the turtle is filling, `False` otherwise.

Copy

\>>> turtle.begin\_fill()
\>>> if turtle.filling():
...    turtle.pensize(5)
... else:
...    turtle.pensize(3)

turtle.fill()[¶](https://docs.python.org/3/library/turtle.html#turtle.fill "Link to this definition")

Fill the shape drawn in the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 block.

Copy

\>>> turtle.color("black", "red")
\>>> with turtle.fill():
...     turtle.circle(80)

`fill()` is a [context manager](https://docs.python.org/3/glossary.html#term-context-manager)
, so using it is the same as calling [`begin_fill()`](https://docs.python.org/3/library/turtle.html#turtle.begin_fill "turtle.begin_fill")
 before the block and [`end_fill()`](https://docs.python.org/3/library/turtle.html#turtle.end_fill "turtle.end_fill")
 after it:

Copy

\>>> turtle.color("black", "red")
\>>> turtle.begin\_fill()
\>>> turtle.circle(80)
\>>> turtle.end\_fill()

Added in version 3.14.

turtle.begin\_fill()[¶](https://docs.python.org/3/library/turtle.html#turtle.begin_fill "Link to this definition")

Call just before drawing a shape to be filled. The shape is filled by the next call to [`end_fill()`](https://docs.python.org/3/library/turtle.html#turtle.end_fill "turtle.end_fill")
.

turtle.end\_fill()[¶](https://docs.python.org/3/library/turtle.html#turtle.end_fill "Link to this definition")

Fill the shape drawn after the last call to [`begin_fill()`](https://docs.python.org/3/library/turtle.html#turtle.begin_fill "turtle.begin_fill")
.

If the shape crosses itself or several shapes overlap, whether the overlapping parts are filled depends on the operating system, the type of overlap and how many there are. For example, the turtle star above may be either all yellow or have some white regions.

Copy

\>>> turtle.color("black", "red")
\>>> turtle.begin\_fill()
\>>> turtle.circle(80)
\>>> turtle.end\_fill()

##### More drawing control[¶](https://docs.python.org/3/library/turtle.html#more-drawing-control "Link to this heading")

turtle.reset()[¶](https://docs.python.org/3/library/turtle.html#turtle.reset "Link to this definition")

Delete the turtle’s drawings and re-center the turtle. The turtle’s settings are restored to their default values.

Copy

\>>> turtle.goto(0,\-22)
\>>> turtle.left(100)
\>>> turtle.position()
(0.00,-22.00)
\>>> turtle.heading()
100.0
\>>> turtle.reset()
\>>> turtle.position()
(0.00,0.00)
\>>> turtle.heading()
0.0

turtle.clear()[¶](https://docs.python.org/3/library/turtle.html#turtle.clear "Link to this definition")

Delete the turtle’s drawings from the screen. The state and position of the turtle as well as the drawings of other turtles are not affected.

turtle.write(_arg_, _move\=False_, _align\='left'_, _font\=('Arial', 8, 'normal')_)[¶](https://docs.python.org/3/library/turtle.html#turtle.write "Link to this definition")

Parameters:

*   **arg** – an object
    
*   **move** – a boolean
    
*   **align** – a string
    
*   **font** – a tuple of a string, an integer and a string
    

Write text at the current turtle position. The text is the string representation of _arg_. _align_ is one of the strings “left”, “center” or “right” and says how the text is placed relative to the turtle position. _font_ is a triple of font name, font size and font type. If _move_ is `True`, the pen is moved to the bottom-right corner of the text.

Copy

\>>> turtle.write("Home = ", True, align\="center")
\>>> turtle.write((0,0), True)

#### Turtle state[¶](https://docs.python.org/3/library/turtle.html#turtle-state "Link to this heading")

##### Visibility[¶](https://docs.python.org/3/library/turtle.html#visibility "Link to this heading")

turtle.hideturtle()[¶](https://docs.python.org/3/library/turtle.html#turtle.hideturtle "Link to this definition")

turtle.ht()[¶](https://docs.python.org/3/library/turtle.html#turtle.ht "Link to this definition")

Make the turtle invisible. If the pen is down, movement still draws.

turtle.showturtle()[¶](https://docs.python.org/3/library/turtle.html#turtle.showturtle "Link to this definition")

turtle.st()[¶](https://docs.python.org/3/library/turtle.html#turtle.st "Link to this definition")

Make the turtle visible.

turtle.isvisible()[¶](https://docs.python.org/3/library/turtle.html#turtle.isvisible "Link to this definition")

Return `True` if the turtle is visible, `False` if it’s hidden.

Copy

\>>> turtle.hideturtle()
\>>> turtle.isvisible()
False
\>>> turtle.showturtle()
\>>> turtle.isvisible()
True

##### Appearance[¶](https://docs.python.org/3/library/turtle.html#appearance "Link to this heading")

turtle.shape(_name\=None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.shape "Link to this definition")

Parameters:

**name** – a string or `None`

Set the turtle shape to the named shape. If _name_ is not given, return the name of the current shape. The shape must exist in the [`TurtleScreen`](https://docs.python.org/3/library/turtle.html#turtle.TurtleScreen "turtle.TurtleScreen")
’s shape dictionary. Initially there are the following shapes: “arrow”, “turtle”, “circle”, “square”, “triangle” and “classic”. To add shapes, see the [`Screen`](https://docs.python.org/3/library/turtle.html#turtle.Screen "turtle.Screen")
 method [`register_shape()`](https://docs.python.org/3/library/turtle.html#turtle.register_shape "turtle.register_shape")
.

Copy

\>>> turtle.shape()
'classic'
\>>> turtle.shape("turtle")
\>>> turtle.shape()
'turtle'

turtle.resizemode(_rmode\=None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.resizemode "Link to this definition")

Parameters:

**rmode** – a string or `None`

Set the resizemode to “auto”, “user” or “noresize”. If _rmode_ is not given, return the current resizemode. The different resizemodes have the following effects:

*   “auto”: the turtle is resized according to the value of [`pensize()`](https://docs.python.org/3/library/turtle.html#turtle.pensize "turtle.pensize")
    .
    
*   “user”: the turtle is resized according to the stretch factors and outline width, which are set by [`shapesize()`](https://docs.python.org/3/library/turtle.html#turtle.shapesize "turtle.shapesize")
    .
    
*   “noresize”: the turtle is not resized.
    

`resizemode("user")` is called by [`shapesize()`](https://docs.python.org/3/library/turtle.html#turtle.shapesize "turtle.shapesize")
 when used with arguments.

Copy

\>>> turtle.resizemode()
'noresize'
\>>> turtle.resizemode("auto")
\>>> turtle.resizemode()
'auto'

turtle.shapesize(_stretch\_wid\=None_, _stretch\_len\=None_, _outline\=None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.shapesize "Link to this definition")

turtle.turtlesize(_stretch\_wid\=None_, _stretch\_len\=None_, _outline\=None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.turtlesize "Link to this definition")

Parameters:

*   **stretch\_wid** – a positive number or `None`
    
*   **stretch\_len** – a positive number or `None`
    
*   **outline** – a positive number or `None`
    

Return or set the turtle’s stretch factors and outline width. If no arguments are given, return the current values. Otherwise set resizemode to “user”, so that the turtle is displayed stretched according to its stretch factors:

*   _stretch\_wid_: the stretch factor perpendicular to the turtle’s heading
    
*   _stretch\_len_: the stretch factor in the direction of the turtle’s heading
    
*   _outline_: the width of the shape’s outline
    

For example, `shapesize(2, 1)` makes the turtle twice as wide without changing its length. If only _stretch\_wid_ is given, _stretch\_len_ is set to the same value.

Copy

\>>> turtle.shapesize()
(1.0, 1.0, 1)
\>>> turtle.resizemode("user")
\>>> turtle.shapesize(5, 5, 12)
\>>> turtle.shapesize()
(5, 5, 12)
\>>> turtle.shapesize(outline\=8)
\>>> turtle.shapesize()
(5, 5, 8)

turtle.shearfactor(_shear\=None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.shearfactor "Link to this definition")

Parameters:

**shear** – a number or `None`

Return or set the current shear factor. Shearing slants the turtle shape, like the slant of italic letters. The shear factor says how much it is slanted: 0 is not slanted at all, and the larger the number, the stronger the slant. Negative numbers slant the other way. If _shear_ is not given, return the current shear factor. Otherwise slant the turtle shape accordingly and set resizemode to “user”. The turtle’s heading does not change. Precisely, the shear factor is the tangent of the shear angle.

Copy

\>>> turtle.shape("circle")
\>>> turtle.shapesize(5,2)
\>>> turtle.shearfactor(0.5)
\>>> turtle.shearfactor()
0.5

turtle.tilt(_angle_)[¶](https://docs.python.org/3/library/turtle.html#turtle.tilt "Link to this definition")

Parameters:

**angle** – a number

Turn the turtle shape by _angle_ from its current tilt angle. The turtle’s heading does not change, so the turtle keeps moving in the same direction. See [`tiltangle()`](https://docs.python.org/3/library/turtle.html#turtle.tiltangle "turtle.tiltangle")
.

Copy

\>>> turtle.reset()
\>>> turtle.shape("circle")
\>>> turtle.shapesize(5,2)
\>>> turtle.tilt(30)
\>>> turtle.fd(50)
\>>> turtle.tilt(30)
\>>> turtle.fd(50)

turtle.tiltangle(_angle\=None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.tiltangle "Link to this definition")

Parameters:

**angle** – a number or `None`

Return or set the current tilt angle. The tilt angle is the angle between the direction the turtle shape points in and the direction the turtle moves in. Normally the shape points in the direction of movement, so the tilt angle is 0. If _angle_ is given, turn the turtle shape to that tilt angle, no matter what it was before, and set resizemode to “user”. The turtle’s heading does not change. If _angle_ is not given, return the current tilt angle.

Copy

\>>> turtle.reset()
\>>> turtle.shape("circle")
\>>> turtle.shapesize(5,2)
\>>> turtle.tilt(45)
\>>> turtle.tiltangle()
45.0

turtle.shapetransform(_t11\=None_, _t12\=None_, _t21\=None_, _t22\=None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.shapetransform "Link to this definition")

Parameters:

*   **t11** – a number or `None`
    
*   **t12** – a number or `None`
    
*   **t21** – a number or `None`
    
*   **t22** – a number or `None`
    

Return or set the transformation matrix of the turtle shape. The matrix combines the stretch factors, the shear factor and the tilt angle of the turtle shape into four numbers: _t11_ and _t12_ form its first row, _t21_ and _t22_ its second. If none of them are given, return the current matrix as a tuple of four numbers. Otherwise set the given elements and update the stretch factors, shear factor and tilt angle accordingly. `t11 * t22 - t12 * t21` must not be zero, otherwise an error is raised.

Copy

\>>> turtle \= Turtle()
\>>> turtle.shape("square")
\>>> turtle.shapesize(4,2)
\>>> turtle.shearfactor(\-0.5)
\>>> turtle.shapetransform()
(4.0, -1.0, -0.0, 2.0)

turtle.get\_shapepoly()[¶](https://docs.python.org/3/library/turtle.html#turtle.get_shapepoly "Link to this definition")

Return the points that form the outline of the current turtle shape as a tuple of `(x, y)` coordinate pairs. These points can be used to define a new shape or parts of a [compound shape](https://docs.python.org/3/library/turtle.html#compound-shapes)

Copy

\>>> turtle.shape("square")
\>>> turtle.shapetransform(4, \-1, 0, 2)
\>>> turtle.get\_shapepoly()
((50, -20), (30, 20), (-50, 20), (-30, -20))

#### Using events[¶](https://docs.python.org/3/library/turtle.html#using-events "Link to this heading")

turtle.onclick(_fun_, _btn\=1_, _add\=None_)

Parameters:

*   **fun** – a function with two arguments or `None`
    
*   **btn** – an integer
    
*   **add** – a boolean or `None`
    

Bind _fun_ to mouse-click events on this turtle. _fun_ is called with the coordinates of the clicked point on the canvas. If _fun_ is `None`, existing bindings are removed. _btn_ is the number of the mouse button and defaults to 1, the left mouse button. If _add_ is `True`, a new binding is added, otherwise it replaces a former binding. Example for the anonymous turtle, that is, the procedural way:

Copy

\>>> def turn(x, y):
...     left(180)
...
\>>> onclick(turn)  \# Now clicking into the turtle will turn it.
\>>> onclick(None)  \# event-binding will be removed

turtle.onrelease(_fun_, _btn\=1_, _add\=None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.onrelease "Link to this definition")

Parameters:

*   **fun** – a function with two arguments which will be called with the coordinates of the clicked point on the canvas
    
*   **btn** – number of the mouse-button, defaults to 1 (left mouse button)
    
*   **add** – `True` or `False` – if `True`, a new binding will be added, otherwise it will replace a former binding
    

Bind _fun_ to mouse-button-release events on this turtle. If _fun_ is `None`, existing bindings are removed.

Copy

\>>> class MyTurtle(Turtle):
...     def glow(self,x,y):
...         self.fillcolor("red")
...     def unglow(self,x,y):
...         self.fillcolor("")
...
\>>> turtle \= MyTurtle()
\>>> turtle.onclick(turtle.glow)     \# clicking on turtle turns fillcolor red,
\>>> turtle.onrelease(turtle.unglow) \# releasing turns it to transparent.

turtle.ondrag(_fun_, _btn\=1_, _add\=None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.ondrag "Link to this definition")

Parameters:

*   **fun** – a function with two arguments which will be called with the coordinates of the clicked point on the canvas
    
*   **btn** – number of the mouse-button, defaults to 1 (left mouse button)
    
*   **add** – `True` or `False` – if `True`, a new binding will be added, otherwise it will replace a former binding
    

Bind _fun_ to mouse-move events on this turtle. If _fun_ is `None`, existing bindings are removed.

Remark: Every sequence of mouse-move-events on a turtle is preceded by a mouse-click event on that turtle.

Copy

\>>> turtle.ondrag(turtle.goto)

Subsequently, clicking and dragging the Turtle will move it across the screen thereby producing handdrawings (if pen is down).

#### Special Turtle methods[¶](https://docs.python.org/3/library/turtle.html#special-turtle-methods "Link to this heading")

turtle.poly()[¶](https://docs.python.org/3/library/turtle.html#turtle.poly "Link to this definition")

Record the vertices of a polygon drawn in the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 block. The first and last vertices will be connected.

Copy

\>>> with turtle.poly():
...     turtle.forward(100)
...     turtle.right(60)
...     turtle.forward(100)

`poly()` is a [context manager](https://docs.python.org/3/glossary.html#term-context-manager)
, so using it is the same as calling [`begin_poly()`](https://docs.python.org/3/library/turtle.html#turtle.begin_poly "turtle.begin_poly")
 before the block and [`end_poly()`](https://docs.python.org/3/library/turtle.html#turtle.end_poly "turtle.end_poly")
 after it:

Copy

\>>> turtle.begin\_poly()
\>>> turtle.forward(100)
\>>> turtle.right(60)
\>>> turtle.forward(100)
\>>> turtle.end\_poly()

Added in version 3.14.

turtle.begin\_poly()[¶](https://docs.python.org/3/library/turtle.html#turtle.begin_poly "Link to this definition")

Start recording the vertices of a polygon. The current turtle position is the first vertex of the polygon.

turtle.end\_poly()[¶](https://docs.python.org/3/library/turtle.html#turtle.end_poly "Link to this definition")

Stop recording the vertices of a polygon. The current turtle position is the last vertex of the polygon. This will be connected with the first vertex.

turtle.get\_poly()[¶](https://docs.python.org/3/library/turtle.html#turtle.get_poly "Link to this definition")

Return the last recorded polygon.

Copy

\>>> turtle.home()
\>>> turtle.begin\_poly()
\>>> turtle.fd(100)
\>>> turtle.left(20)
\>>> turtle.fd(30)
\>>> turtle.left(60)
\>>> turtle.fd(50)
\>>> turtle.end\_poly()
\>>> p \= turtle.get\_poly()
\>>> register\_shape("myFavouriteShape", p)

turtle.clone()[¶](https://docs.python.org/3/library/turtle.html#turtle.clone "Link to this definition")

Create and return a clone of the turtle. The clone has the same position, heading and turtle properties.

Copy

\>>> leonel \= Turtle()
\>>> marco \= leonel.clone()

turtle.getturtle()[¶](https://docs.python.org/3/library/turtle.html#turtle.getturtle "Link to this definition")

turtle.getpen()[¶](https://docs.python.org/3/library/turtle.html#turtle.getpen "Link to this definition")

Return the Turtle object itself.

Call `getturtle()` to get the turtle used by functions such as [`forward()`](https://docs.python.org/3/library/turtle.html#turtle.forward "turtle.forward")
 and [`left()`](https://docs.python.org/3/library/turtle.html#turtle.left "turtle.left")
:

Copy

\>>> pet \= getturtle()
\>>> pet.fd(50)
\>>> pet
<turtle.Turtle object at 0x...>

turtle.getscreen()[¶](https://docs.python.org/3/library/turtle.html#turtle.getscreen "Link to this definition")

Return the [`TurtleScreen`](https://docs.python.org/3/library/turtle.html#turtle.TurtleScreen "turtle.TurtleScreen")
 object the turtle is drawing on. TurtleScreen methods can then be called for that object.

Copy

\>>> ts \= turtle.getscreen()
\>>> ts
<turtle.\_Screen object at 0x...>
\>>> ts.bgcolor("pink")

turtle.setundobuffer(_size_)[¶](https://docs.python.org/3/library/turtle.html#turtle.setundobuffer "Link to this definition")

Parameters:

**size** – an integer or `None`

Set or disable the undo buffer. If _size_ is an integer, an empty undo buffer of the given size is installed. _size_ is the maximum number of turtle actions that can be undone by [`undo()`](https://docs.python.org/3/library/turtle.html#turtle.undo "turtle.undo")
. If _size_ is `None`, the undo buffer is disabled.

Copy

\>>> turtle.setundobuffer(42)

turtle.undobufferentries()[¶](https://docs.python.org/3/library/turtle.html#turtle.undobufferentries "Link to this definition")

Return the number of entries in the undo buffer.

Copy

\>>> while undobufferentries():
...     undo()

### Screen methods and functions[¶](https://docs.python.org/3/library/turtle.html#screen-methods-and-functions "Link to this heading")

Most of the examples in this section refer to a TurtleScreen instance called `screen`.

#### Window control[¶](https://docs.python.org/3/library/turtle.html#window-control "Link to this heading")

turtle.bgcolor()[¶](https://docs.python.org/3/library/turtle.html#turtle.bgcolor "Link to this definition")

turtle.bgcolor(_color_, _/_)

turtle.bgcolor(_r_, _g_, _b_, _/_)

Return or set the background color of the TurtleScreen.

Four input formats are allowed:

`bgcolor()`

Return the current background color as a color specification string or as a tuple (see example). May be used as input to another [`color()`](https://docs.python.org/3/library/turtle.html#turtle.color "turtle.color")
, [`pencolor()`](https://docs.python.org/3/library/turtle.html#turtle.pencolor "turtle.pencolor")
, [`fillcolor()`](https://docs.python.org/3/library/turtle.html#turtle.fillcolor "turtle.fillcolor")
 or `bgcolor()` call.

`bgcolor(colorstring)`

Set the background color to _colorstring_, which is a Tk color specification string, such as `"red"`, `"yellow"`, or `"#33cc8c"`.

`bgcolor((r, g, b))`

Set the background color to the RGB color represented by the tuple of _r_, _g_, and _b_. Each of _r_, _g_, and _b_ must be between 0 and colormode, where colormode is either 1.0 or 255 (see [`colormode()`](https://docs.python.org/3/library/turtle.html#turtle.colormode "turtle.colormode")
).

`bgcolor(r, g, b)`

Set the background color to the RGB color represented by _r_, _g_, and _b_. Each of _r_, _g_, and _b_ must be between 0 and colormode.

Copy

\>>> screen.bgcolor("orange")
\>>> screen.bgcolor()
'orange'
\>>> screen.bgcolor("#800080")
\>>> screen.bgcolor()
(128.0, 0.0, 128.0)

turtle.bgpic(_picname\=None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.bgpic "Link to this definition")

Parameters:

**picname** – a string or `None`

Set the background image or return the name of the current one. If _picname_ is the name of an image file (PNG, GIF, PGM, and PPM), set that image as the background. If _picname_ is `"nopic"`, delete the background image, if present. If _picname_ is `None`, return the filename of the current background image.

Copy

\>>> screen.bgpic()
'nopic'
\>>> screen.bgpic("landscape.gif")
\>>> screen.bgpic()
'landscape.gif'

turtle.clear()

Note

This TurtleScreen method is available as a global function only under the name `clearscreen`. The global function `clear` is a different one derived from the Turtle method `clear`.

turtle.clearscreen()[¶](https://docs.python.org/3/library/turtle.html#turtle.clearscreen "Link to this definition")

Delete all drawings and all turtles from the TurtleScreen. Reset the now empty TurtleScreen to its initial state: white background, no background image, no event bindings and tracing on.

turtle.reset()

Note

This TurtleScreen method is available as a global function only under the name `resetscreen`. The global function `reset` is another one derived from the Turtle method `reset`.

turtle.resetscreen()[¶](https://docs.python.org/3/library/turtle.html#turtle.resetscreen "Link to this definition")

Reset all turtles on the screen to their initial state.

turtle.screensize(_canvwidth\=None_, _canvheight\=None_, _bg\=None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.screensize "Link to this definition")

Parameters:

*   **canvwidth** – a positive integer or `None`
    
*   **canvheight** – a positive integer or `None`
    
*   **bg** – a colorstring or a color tuple or `None`
    

Resize the canvas the turtles are drawing on. _canvwidth_ and _canvheight_ are the new width and height of the canvas in pixels, and _bg_ is the new background color. If no arguments are given, return the current canvas width and height.

The drawing window is not altered. To see hidden parts of the canvas, use the scrollbars. This can make visible those parts of a drawing which were outside the canvas before, for example to find a turtle that has wandered off the canvas.

Copy

\>>> screen.screensize()
(400, 300)
\>>> screen.screensize(2000,1500)
\>>> screen.screensize()
(2000, 1500)

turtle.setworldcoordinates(_llx_, _lly_, _urx_, _ury_)[¶](https://docs.python.org/3/library/turtle.html#turtle.setworldcoordinates "Link to this definition")

Parameters:

*   **llx** – a number
    
*   **lly** – a number
    
*   **urx** – a number
    
*   **ury** – a number
    

Set up a user-defined coordinate system. _llx_ and _lly_ are the x and y coordinates of the lower left corner of the canvas. _urx_ and _ury_ are the x and y coordinates of the upper right corner. Switch to mode “world” if necessary, which performs a reset. If mode “world” is already active, all drawings are redrawn according to the new coordinates. In user-defined coordinate systems, angles may appear distorted, see [`mode()`](https://docs.python.org/3/library/turtle.html#turtle.mode "turtle.mode")
.

Copy

\>>> screen.reset()
\>>> screen.setworldcoordinates(\-50,\-7.5,50,7.5)
\>>> for \_ in range(72):
...     left(10)
...
\>>> for \_ in range(8):
...     left(45); fd(2)   \# a regular octagon

#### Animation control[¶](https://docs.python.org/3/library/turtle.html#animation-control "Link to this heading")

turtle.no\_animation()[¶](https://docs.python.org/3/library/turtle.html#turtle.no_animation "Link to this definition")

Temporarily turn off turtle animation. The code inside the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 block is not animated. Once the block is exited, the drawing appears. This is useful for drawing complex shapes where even the fastest speed setting is too slow.

Copy

\>>> with screen.no\_animation():
...     for dist in range(2, 400, 2):
...         fd(dist)
...         rt(90)

Added in version 3.14.

turtle.delay(_delay\=None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.delay "Link to this definition")

Parameters:

**delay** – a nonnegative integer or `None`

Return or set the drawing delay in milliseconds. This is approximately the time interval between two consecutive canvas updates. The longer the drawing delay, the slower the animation.

Copy

\>>> screen.delay()
10
\>>> screen.delay(5)
\>>> screen.delay()
5

turtle.tracer(_n\=None_, _delay\=None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.tracer "Link to this definition")

Parameters:

*   **n** – a nonnegative integer or `None`
    
*   **delay** – a nonnegative integer or `None`
    

Turn turtle animation on or off and set the drawing delay. If _n_ is given, only every n-th regular screen update is performed, which can be used to speed up the drawing of complex graphics. If _n_ is 0, animation is turned off and the screen is only updated by calling [`update()`](https://docs.python.org/3/library/turtle.html#turtle.update "turtle.update")
. If _delay_ is given, it sets the drawing delay, see [`delay()`](https://docs.python.org/3/library/turtle.html#turtle.delay "turtle.delay")
. When called without arguments, return the current value of _n_.

Copy

\>>> screen.tracer(8, 25)
\>>> dist \= 2
\>>> for i in range(200):
...     fd(dist)
...     rt(90)
...     dist += 2

turtle.update()[¶](https://docs.python.org/3/library/turtle.html#turtle.update "Link to this definition")

Perform a TurtleScreen update. To be used when tracer is turned off.

See also the RawTurtle/Turtle method [`speed()`](https://docs.python.org/3/library/turtle.html#turtle.speed "turtle.speed")
.

#### Using screen events[¶](https://docs.python.org/3/library/turtle.html#using-screen-events "Link to this heading")

turtle.listen(_xdummy\=None_, _ydummy\=None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.listen "Link to this definition")

Parameters:

*   **xdummy** – ignored
    
*   **ydummy** – ignored
    

Set focus on the [`TurtleScreen`](https://docs.python.org/3/library/turtle.html#turtle.TurtleScreen "turtle.TurtleScreen")
 so that it receives key events. The two dummy arguments are only there so that `listen()` can be passed to [`onclick()`](https://docs.python.org/3/library/turtle.html#turtle.onclick "turtle.onclick")
.

turtle.onkey(_fun_, _key_)[¶](https://docs.python.org/3/library/turtle.html#turtle.onkey "Link to this definition")

turtle.onkeyrelease(_fun_, _key_)[¶](https://docs.python.org/3/library/turtle.html#turtle.onkeyrelease "Link to this definition")

Parameters:

*   **fun** – a function with no arguments or `None`
    
*   **key** – a string
    

Bind _fun_ to the key-release event of _key_. _key_ is a key, such as “a”, or a key symbol, such as “space”. If _fun_ is `None`, the event binding is removed. To be able to receive key events, the [`TurtleScreen`](https://docs.python.org/3/library/turtle.html#turtle.TurtleScreen "turtle.TurtleScreen")
 must have focus, see [`listen()`](https://docs.python.org/3/library/turtle.html#turtle.listen "turtle.listen")
.

Copy

\>>> def f():
...     fd(50)
...     lt(60)
...
\>>> screen.onkey(f, "Up")
\>>> screen.listen()

The turtle can then be moved by repeatedly pressing the up-arrow key, drawing a hexagon.

turtle.onkeypress(_fun_, _key\=None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.onkeypress "Link to this definition")

Parameters:

*   **fun** – a function with no arguments or `None`
    
*   **key** – a string or `None`
    

Bind _fun_ to the key-press event of _key_. _key_ is a key, such as “a”, or a key symbol, such as “space”. If _key_ is not given, _fun_ is bound to the key-press event of any key. If _fun_ is `None`, the event binding is removed. To be able to receive key events, the [`TurtleScreen`](https://docs.python.org/3/library/turtle.html#turtle.TurtleScreen "turtle.TurtleScreen")
 must have focus, see [`listen()`](https://docs.python.org/3/library/turtle.html#turtle.listen "turtle.listen")
.

Copy

\>>> def f():
...     fd(50)
...     lt(60)
...
\>>> screen.onkeypress(f, "Up")
\>>> screen.listen()

The turtle can then be moved by pressing or holding down the up-arrow key, drawing a hexagon.

turtle.onclick(_fun_, _btn\=1_, _add\=None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.onclick "Link to this definition")

turtle.onscreenclick(_fun_, _btn\=1_, _add\=None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.onscreenclick "Link to this definition")

Parameters:

*   **fun** – a function with two arguments or `None`
    
*   **btn** – an integer
    
*   **add** – a boolean or `None`
    

Bind _fun_ to mouse-click events on this screen. _fun_ is called with the coordinates of the clicked point on the canvas. If _fun_ is `None`, existing bindings are removed. _btn_ is the number of the mouse button and defaults to 1, the left mouse button. If _add_ is `True`, a new binding is added, otherwise it replaces a former binding.

Example for a TurtleScreen instance named `screen` and a Turtle instance named `turtle`:

Copy

\>>> screen.onclick(turtle.goto) \# Subsequently clicking into the TurtleScreen will
\>>>                             \# make the turtle move to the clicked point.
\>>> screen.onclick(None)        \# remove event binding again

Note

This TurtleScreen method is available as a global function only under the name `onscreenclick`. The global function `onclick` is another one derived from the Turtle method `onclick`.

turtle.ontimer(_fun_, _t\=0_)[¶](https://docs.python.org/3/library/turtle.html#turtle.ontimer "Link to this definition")

Parameters:

*   **fun** – a function with no arguments
    
*   **t** – a nonnegative number
    

Install a timer that calls _fun_ after _t_ milliseconds.

Copy

\>>> running \= True
\>>> def f():
...     if running:
...         fd(50)
...         lt(60)
...         screen.ontimer(f, 250)
\>>> f()  \# makes the turtle march around
\>>> running \= False

turtle.mainloop()[¶](https://docs.python.org/3/library/turtle.html#turtle.mainloop "Link to this definition")

turtle.done()[¶](https://docs.python.org/3/library/turtle.html#turtle.done "Link to this definition")

Start the event loop by calling Tkinter’s [`mainloop()`](https://docs.python.org/3/library/tkinter.html#tkinter.Misc.mainloop "tkinter.Misc.mainloop")
 method. Must be the last statement in a turtle graphics program. Must _not_ be used if a script is run from within IDLE in -n mode (see [Running without a subprocess](https://docs.python.org/3/library/idle.html#idle-no-subprocess)
).

#### Input methods[¶](https://docs.python.org/3/library/turtle.html#input-methods "Link to this heading")

turtle.textinput(_title_, _prompt_)[¶](https://docs.python.org/3/library/turtle.html#turtle.textinput "Link to this definition")

Parameters:

*   **title** – a string
    
*   **prompt** – a string
    

Pop up a dialog window for input of a string. _title_ is the title of the dialog window and _prompt_ is a text describing what information to input. Return the string entered. If the dialog is canceled, return `None`.

Copy

\>>> screen.textinput("NIM", "Name of first player:")

turtle.numinput(_title_, _prompt_, _default\=None_, _minval\=None_, _maxval\=None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.numinput "Link to this definition")

Parameters:

*   **title** – a string
    
*   **prompt** – a string
    
*   **default** – a number or `None`
    
*   **minval** – a number or `None`
    
*   **maxval** – a number or `None`
    

Pop up a dialog window for input of a number. _title_ is the title of the dialog window and _prompt_ is a text describing what numerical information to input. _default_ is the default value, _minval_ and _maxval_ are the minimum and maximum values for input. If these are given, the number entered must be between _minval_ and _maxval_. If not, a hint is issued and the dialog remains open for correction. Return the number entered. If the dialog is canceled, return `None`.

Copy

\>>> screen.numinput("Poker", "Your stakes:", 1000, minval\=10, maxval\=10000)

#### Settings and special methods[¶](https://docs.python.org/3/library/turtle.html#settings-and-special-methods "Link to this heading")

turtle.mode(_mode\=None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.mode "Link to this definition")

Parameters:

**mode** – a string or `None`

Set the turtle mode and perform a reset. _mode_ is one of the strings “standard”, “logo” or “world”. If _mode_ is not given, return the current mode.

Mode “standard” is compatible with the old `turtle` module. Mode “logo” is compatible with most Logo turtle graphics. Mode “world” uses user-defined world coordinates, see [`setworldcoordinates()`](https://docs.python.org/3/library/turtle.html#turtle.setworldcoordinates "turtle.setworldcoordinates")
. In this mode, angles appear distorted if the x and y units are not of equal length.

| Mode | Initial turtle heading | positive angles |
| --- | --- | --- |
| “standard” | to the right (east) | counterclockwise |
| “logo” | upward (north) | clockwise |

Copy

\>>> mode("logo")  \# resets turtle heading to north
\>>> mode()
'logo'

turtle.colormode(_cmode\=None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.colormode "Link to this definition")

Parameters:

**cmode** – a number or `None`

Return the colormode or set it to 1.0 or 255. After setting it, the _r_, _g_ and _b_ values of color triples have to be between 0 and _cmode_.

Copy

\>>> screen.colormode(1)
\>>> turtle.pencolor(240, 160, 80)
Traceback (most recent call last):
     ...
TurtleGraphicsError: bad color sequence: (240, 160, 80)
\>>> screen.colormode()
1.0
\>>> screen.colormode(255)
\>>> screen.colormode()
255
\>>> turtle.pencolor(240,160,80)

turtle.getcanvas()[¶](https://docs.python.org/3/library/turtle.html#turtle.getcanvas "Link to this definition")

Return the Canvas of this TurtleScreen. Useful for insiders who know what to do with a Tkinter Canvas.

Copy

\>>> cv \= screen.getcanvas()
\>>> cv
<turtle.ScrolledCanvas object ...>

turtle.getshapes()[¶](https://docs.python.org/3/library/turtle.html#turtle.getshapes "Link to this definition")

Return a list of names of all currently available turtle shapes.

Copy

\>>> screen.getshapes()
\['arrow', 'blank', 'circle', ..., 'turtle'\]

turtle.register\_shape(_name_, _shape\=None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.register_shape "Link to this definition")

turtle.addshape(_name_, _shape\=None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.addshape "Link to this definition")

Parameters:

*   **name** – a string
    
*   **shape** – a string, a tuple of pairs of numbers, a [`Shape`](https://docs.python.org/3/library/turtle.html#turtle.Shape "turtle.Shape")
     object or `None`
    

Add a turtle shape to the TurtleScreen’s shape list. It can be called in four different ways:

1.  _name_ is the name of an image file (PNG, GIF, PGM, and PPM) and _shape_ is `None`: Install the corresponding image shape.
    
    Copy
    
    \>>> screen.register\_shape("turtle.gif")
    
2.  _name_ is an arbitrary string and _shape_ is the name of an image file (PNG, GIF, PGM, and PPM): Install the corresponding image shape.
    
    Copy
    
    \>>> screen.register\_shape("turtle", "turtle.gif")
    
3.  _name_ is an arbitrary string and _shape_ is a tuple of pairs of coordinates: Install the corresponding polygon shape.
    
    Copy
    
    \>>> screen.register\_shape("triangle", ((5,\-3), (0,5), (\-5,\-3)))
    
4.  _name_ is an arbitrary string and _shape_ is a (compound) [`Shape`](https://docs.python.org/3/library/turtle.html#turtle.Shape "turtle.Shape")
     object: Install the corresponding compound shape.
    

Image shapes do not rotate when turning the turtle, so they do not display the heading of the turtle. To use a registered shape, call [`shape()`](https://docs.python.org/3/library/turtle.html#turtle.shape "turtle.shape")
 with its name.

Changed in version 3.14: Added support for PNG, PGM, and PPM image formats. Both a shape name and an image file name can be specified.

turtle.turtles()[¶](https://docs.python.org/3/library/turtle.html#turtle.turtles "Link to this definition")

Return the list of turtles on the screen.

Copy

\>>> for turtle in screen.turtles():
...     turtle.color("red")

turtle.window\_height()[¶](https://docs.python.org/3/library/turtle.html#turtle.window_height "Link to this definition")

Return the height of the turtle window.

Copy

\>>> screen.window\_height()
480

turtle.window\_width()[¶](https://docs.python.org/3/library/turtle.html#turtle.window_width "Link to this definition")

Return the width of the turtle window.

Copy

\>>> screen.window\_width()
640

#### Screen-only methods[¶](https://docs.python.org/3/library/turtle.html#screen-only-methods "Link to this heading")

turtle.bye()[¶](https://docs.python.org/3/library/turtle.html#turtle.bye "Link to this definition")

Close the turtle graphics window.

turtle.exitonclick()[¶](https://docs.python.org/3/library/turtle.html#turtle.exitonclick "Link to this definition")

Bind `bye()` method to mouse clicks on the Screen.

If the value “using\_IDLE” in the configuration dictionary is `False` (default value), also enter mainloop. Remark: If IDLE with the `-n` switch (no subprocess) is used, this value should be set to `True` in `turtle.cfg`. In this case IDLE’s own mainloop is active also for the client script.

turtle.save(_filename_, _\*_, _overwrite\=False_)[¶](https://docs.python.org/3/library/turtle.html#turtle.save "Link to this definition")

Parameters:

*   **filename** – a string
    
*   **overwrite** – a boolean
    

Save the current drawing and the turtles as a PostScript file. _filename_ is the path of the file to create. It must end with `".ps"` or `".eps"`. If a file with that name already exists, a [`FileExistsError`](https://docs.python.org/3/builtins/exceptions.html#FileExistsError "FileExistsError")
 is raised, unless _overwrite_ is `True`. _overwrite_ must be given by name, as in `overwrite=True`.

Copy

\>>> screen.save("my\_drawing.ps")
\>>> screen.save("my\_drawing.ps", overwrite\=True)

Added in version 3.14.

turtle.setup(_width\=\_CFG\['width'\]_, _height\=\_CFG\['height'\]_, _startx\=\_CFG\['leftright'\]_, _starty\=\_CFG\['topbottom'\]_)[¶](https://docs.python.org/3/library/turtle.html#turtle.setup "Link to this definition")

Set the size and position of the main window. Default values of arguments are stored in the configuration dictionary and can be changed via a `turtle.cfg` file.

Parameters:

*   **width** – if an integer, a size in pixels, if a float, a fraction of the screen; default is 50% of screen
    
*   **height** – if an integer, the height in pixels, if a float, a fraction of the screen; default is 75% of screen
    
*   **startx** – if positive, starting position in pixels from the left edge of the screen, if negative from the right edge, if `None`, center window horizontally
    
*   **starty** – if positive, starting position in pixels from the top edge of the screen, if negative from the bottom edge, if `None`, center window vertically
    

Copy

\>>> screen.setup (width\=200, height\=200, startx\=0, starty\=0)
\>>>              \# sets window to 200x200 pixels, in upper left of screen
\>>> screen.setup(width\=.75, height\=0.5, startx\=None, starty\=None)
\>>>              \# sets window to 75% of screen by 50% of screen and centers

turtle.title(_titlestring_)[¶](https://docs.python.org/3/library/turtle.html#turtle.title "Link to this definition")

Parameters:

**titlestring** – a string

Set the title of the turtle window to _titlestring_. The title is shown in the title bar of the turtle graphics window.

Copy

\>>> screen.title("Welcome to the turtle zoo!")

### Public classes[¶](https://docs.python.org/3/library/turtle.html#public-classes "Link to this heading")

class turtle.RawTurtle(_canvas_)[¶](https://docs.python.org/3/library/turtle.html#turtle.RawTurtle "Link to this definition")

class turtle.RawPen(_canvas_)[¶](https://docs.python.org/3/library/turtle.html#turtle.RawPen "Link to this definition")

Parameters:

**canvas** – a `tkinter.Canvas`, a [`ScrolledCanvas`](https://docs.python.org/3/library/turtle.html#turtle.ScrolledCanvas "turtle.ScrolledCanvas")
 or a [`TurtleScreen`](https://docs.python.org/3/library/turtle.html#turtle.TurtleScreen "turtle.TurtleScreen")

Create a turtle. The turtle has all methods described above as “methods of Turtle/RawTurtle”.

class turtle.Turtle[¶](https://docs.python.org/3/library/turtle.html#turtle.Turtle "Link to this definition")

Subclass of RawTurtle, has the same interface but draws on a default [`Screen`](https://docs.python.org/3/library/turtle.html#turtle.Screen "turtle.Screen")
 object created automatically when needed for the first time.

class turtle.TurtleScreen(_cv_)[¶](https://docs.python.org/3/library/turtle.html#turtle.TurtleScreen "Link to this definition")

Parameters:

**cv** – a `tkinter.Canvas`

Provides screen oriented methods like [`bgcolor()`](https://docs.python.org/3/library/turtle.html#turtle.bgcolor "turtle.bgcolor")
 etc. that are described above.

class turtle.Screen[¶](https://docs.python.org/3/library/turtle.html#turtle.Screen "Link to this definition")

Subclass of [`TurtleScreen`](https://docs.python.org/3/library/turtle.html#turtle.TurtleScreen "turtle.TurtleScreen")
, with [four methods added](https://docs.python.org/3/library/turtle.html#screenspecific)
. Calling `Screen()` returns the single screen object. If it does not exist yet, it is created. Otherwise the existing one is returned.

class turtle.ScrolledCanvas(_master_)[¶](https://docs.python.org/3/library/turtle.html#turtle.ScrolledCanvas "Link to this definition")

Parameters:

**master** – some Tkinter widget to contain the ScrolledCanvas, i.e. a Tkinter-canvas with scrollbars added

Used by class Screen, which thus automatically provides a ScrolledCanvas as playground for the turtles.

class turtle.Shape(_type\__, _data_)[¶](https://docs.python.org/3/library/turtle.html#turtle.Shape "Link to this definition")

Parameters:

*   **type\_** – a string
    
*   **data** – depends on _type\__
    

Data structure modeling shapes. _type\__ is one of the strings “polygon”, “image” or “compound”. What _data_ must be depends on _type\__: for “polygon” a tuple of pairs of coordinates, for “image” an image (only used internally), and for “compound” `None`, as a compound shape is built up using the [`addcomponent()`](https://docs.python.org/3/library/turtle.html#turtle.Shape.addcomponent "turtle.Shape.addcomponent")
 method.

addcomponent(_poly_, _fill_, _outline\=None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.Shape.addcomponent "Link to this definition")

Parameters:

*   **poly** – a tuple of pairs of numbers
    
*   **fill** – a color
    
*   **outline** – a color or `None`
    

Add a component to a shape of type “compound”. _poly_ is a polygon, a tuple of pairs of numbers. _fill_ is the color the polygon is filled with and _outline_ is the color of its outline. If _outline_ is not given, _fill_ is used for it as well.

Example:

Copy

\>>> poly \= ((0,0), (10,\-5), (0,10), (\-10,\-5))
\>>> s \= Shape("compound")
\>>> s.addcomponent(poly, "red", "blue")
\>>> \# ... add more components and then use register\_shape()

See [How to use compound shapes](https://docs.python.org/3/library/turtle.html#compoundshapes)
.

class turtle.Vec2D(_x_, _y_)[¶](https://docs.python.org/3/library/turtle.html#turtle.Vec2D "Link to this definition")

A two-dimensional vector class, used as a helper class for implementing turtle graphics. May be useful for turtle graphics programs too. Derived from tuple, so a vector is a tuple!

Provides (for _a_, _b_ vectors, _k_ number):

*   `a + b` vector addition
    
*   `a - b` vector subtraction
    
*   `a * b` inner product
    
*   `k * a` and `a * k` multiplication with scalar
    
*   `abs(a)` absolute value of a
    
*   `a.rotate(angle)` rotation
    

### Exceptions[¶](https://docs.python.org/3/library/turtle.html#exceptions "Link to this heading")

The `turtle` module defines the following exception:

exception turtle.TurtleGraphicsError[¶](https://docs.python.org/3/library/turtle.html#turtle.TurtleGraphicsError "Link to this definition")

Raised for invalid arguments or operations. For example, a malformed color string:

Copy

\>>> turtle.color("blau")
Traceback (most recent call last):
    ...
turtle.TurtleGraphicsError: bad color string: blau

How-to guides[¶](https://docs.python.org/3/library/turtle.html#how-to-guides "Link to this heading")

-----------------------------------------------------------------------------------------------------

This section covers some typical turtle use-cases and approaches.

### How to automatically begin and end filling[¶](https://docs.python.org/3/library/turtle.html#how-to-automatically-begin-and-end-filling "Link to this heading")

Starting with Python 3.14, you can use the [`fill()`](https://docs.python.org/3/library/turtle.html#turtle.fill "turtle.fill")
 [context manager](https://docs.python.org/3/glossary.html#term-context-manager)
 instead of [`begin_fill()`](https://docs.python.org/3/library/turtle.html#turtle.begin_fill "turtle.begin_fill")
 and [`end_fill()`](https://docs.python.org/3/library/turtle.html#turtle.end_fill "turtle.end_fill")
 to automatically begin and end fill. Here is an example:

Copy

with fill():
    for i in range(4):
        forward(100)
        right(90)

forward(200)

The code above is equivalent to:

Copy

begin\_fill()
for i in range(4):
    forward(100)
    right(90)
end\_fill()

forward(200)

### How to use compound shapes[¶](https://docs.python.org/3/library/turtle.html#how-to-use-compound-shapes "Link to this heading")

To use compound turtle shapes, which consist of several polygons of different color, you must use the helper class [`Shape`](https://docs.python.org/3/library/turtle.html#turtle.Shape "turtle.Shape")
 explicitly as described below:

1.  Create an empty [`Shape`](https://docs.python.org/3/library/turtle.html#turtle.Shape "turtle.Shape")
     object of type “compound”.
    
2.  Add as many components to this object as desired, using the [`addcomponent()`](https://docs.python.org/3/library/turtle.html#turtle.Shape.addcomponent "turtle.Shape.addcomponent")
     method.
    
    For example:
    
    Copy
    
    \>>> s \= Shape("compound")
    \>>> poly1 \= ((0,0), (10,\-5), (0,10), (\-10,\-5))
    \>>> s.addcomponent(poly1, "red", "blue")
    \>>> poly2 \= ((0,0), (10,\-5), (\-10,\-5))
    \>>> s.addcomponent(poly2, "blue", "red")
    
3.  Now add the Shape to the Screen’s shapelist and use it:
    
    Copy
    
    \>>> register\_shape("myshape", s)
    \>>> shape("myshape")
    

### How to use the `turtle` module namespace[¶](https://docs.python.org/3/library/turtle.html#how-to-use-the-turtle-module-namespace "Link to this heading")

Using `from turtle import *` is convenient - but be warned that it imports a rather large collection of objects, and if you’re doing anything but turtle graphics you run the risk of a name conflict (this becomes even more an issue if you’re using turtle graphics in a script where other modules might be imported).

The solution is to use `import turtle` - `fd()` becomes `turtle.fd()`, `width()` becomes `turtle.width()` and so on. (If typing “turtle” over and over again becomes tedious, use for example `import turtle as t` instead.)

### How to use turtle graphics in a script[¶](https://docs.python.org/3/library/turtle.html#how-to-use-turtle-graphics-in-a-script "Link to this heading")

It’s recommended to use the `turtle` module namespace as described immediately above, for example:

Copy

import turtle as t
from random import random

for i in range(100):
    steps \= int(random() \* 100)
    angle \= int(random() \* 360)
    t.right(angle)
    t.fd(steps)

Another step is also required though - as soon as the script ends, Python will also close the turtle’s window. Add:

Copy

t.mainloop()

to the end of the script. The script will now wait to be dismissed and will not exit until it is terminated, for example by closing the turtle graphics window.

### How to use object-oriented turtle graphics[¶](https://docs.python.org/3/library/turtle.html#how-to-use-object-oriented-turtle-graphics "Link to this heading")

See also

[Explanation of the object-oriented interface](https://docs.python.org/3/library/turtle.html#turtle-explanation)

Other than for very basic introductory purposes, or for trying things out as quickly as possible, it’s more usual and much more powerful to use the object-oriented approach to turtle graphics. For example, this allows multiple turtles on screen at once.

In this approach, the various turtle commands are methods of objects (mostly of `Turtle` objects). You _can_ use the object-oriented approach in the shell, but it would be more typical in a Python script.

The example above then becomes:

Copy

from turtle import Turtle
from random import random

t \= Turtle()
for i in range(100):
    steps \= int(random() \* 100)
    angle \= int(random() \* 360)
    t.right(angle)
    t.fd(steps)

t.screen.mainloop()

Note the last line. `t.screen` is an instance of the [`Screen`](https://docs.python.org/3/library/turtle.html#turtle.Screen "turtle.Screen")
 that a Turtle instance exists on; it’s created automatically along with the turtle.

The turtle’s screen can be customised, for example:

Copy

t.screen.title('Object-oriented turtle demo')
t.screen.bgcolor("orange")

### How to use `help()`[¶](https://docs.python.org/3/library/turtle.html#how-to-use-help "Link to this heading")

The public methods of the Screen and Turtle classes are documented extensively via docstrings. So these can be used as online-help via the Python help facilities:

*   When using IDLE, tooltips show the signatures and first lines of the docstrings of typed in function-/method calls.
    
*   Calling [`help()`](https://docs.python.org/3/builtins/functions.html#help "help")
     on methods or functions displays the docstrings:
    
    Copy
    
    \>>> help(Screen.bgcolor)
    Help on method bgcolor in module turtle:
    
    bgcolor(self, \*args) unbound turtle.Screen method
        Set or return backgroundcolor of the TurtleScreen.
    
        Arguments (if given): a color string or three numbers
        in the range 0..colormode or a 3-tuple of such numbers.
    
        >>> screen.bgcolor("orange")
        >>> screen.bgcolor()
        "orange"
        >>> screen.bgcolor(0.5,0,0.5)
        >>> screen.bgcolor()
        "#800080"
    
    \>>> help(Turtle.penup)
    Help on method penup in module turtle:
    
    penup(self) unbound turtle.Turtle method
        Pull the pen up -- no drawing when moving.
    
        Aliases: penup | pu | up
    
        No argument
    
        >>> turtle.penup()
    
*   The docstrings of the functions which are derived from methods have a modified form:
    
    Copy
    
    \>>> help(bgcolor)
    Help on function bgcolor in module turtle:
    
    bgcolor(\*args)
        Set or return backgroundcolor of the TurtleScreen.
    
        Arguments (if given): a color string or three numbers
        in the range 0..colormode or a 3-tuple of such numbers.
    
        Example::
    
          >>> bgcolor("orange")
          >>> bgcolor()
          "orange"
          >>> bgcolor(0.5,0,0.5)
          >>> bgcolor()
          "#800080"
    
    \>>> help(penup)
    Help on function penup in module turtle:
    
    penup()
        Pull the pen up -- no drawing when moving.
    
        Aliases: penup | pu | up
    
        No argument
    
        Example:
        >>> penup()
    

These modified docstrings are created automatically together with the function definitions that are derived from the methods at import time.

### Translation of docstrings into different languages[¶](https://docs.python.org/3/library/turtle.html#translation-of-docstrings-into-different-languages "Link to this heading")

There is a utility to create a dictionary the keys of which are the method names and the values of which are the docstrings of the public methods of the classes Screen and Turtle.

turtle.write\_docstringdict(_filename\='turtle\_docstringdict'_)[¶](https://docs.python.org/3/library/turtle.html#turtle.write_docstringdict "Link to this definition")

Parameters:

**filename** – a string, used as filename

Create and write docstring-dictionary to a Python script with the given filename. This function has to be called explicitly (it is not used by the turtle graphics classes). The docstring dictionary will be written to the Python script `_filename_.py`. It is intended to serve as a template for translation of the docstrings into different languages.

If you (or your students) want to use `turtle` with online help in your native language, you have to translate the docstrings and save the resulting file as e.g. `turtle_docstringdict_german.py`.

If you have an appropriate entry in your `turtle.cfg` file this dictionary will be read in at import time and will replace the original English docstrings.

At the time of this writing there are docstring dictionaries in German and in Italian. (Requests please to [glingl@aon.at](mailto:glingl%40aon.at)
.)

### How to configure Screen and Turtles[¶](https://docs.python.org/3/library/turtle.html#how-to-configure-screen-and-turtles "Link to this heading")

The built-in default configuration mimics the appearance and behaviour of the old turtle module in order to retain best possible compatibility with it.

If you want to use a different configuration which better reflects the features of this module or which better fits to your needs, e.g. for use in a classroom, you can prepare a configuration file `turtle.cfg` which will be read at import time and modify the configuration according to its settings.

The built in configuration would correspond to the following `turtle.cfg`:

width \= 0.5
height \= 0.75
leftright \= None
topbottom \= None
canvwidth \= 400
canvheight \= 300
mode \= standard
colormode \= 1.0
delay \= 10
undobuffersize \= 1000
shape \= classic
pencolor \= black
fillcolor \= black
resizemode \= noresize
visible \= True
language \= english
exampleturtle \= turtle
examplescreen \= screen
title \= Python Turtle Graphics
using\_IDLE \= False

Short explanation of selected entries:

*   The first four lines correspond to the arguments of the [`Screen.setup`](https://docs.python.org/3/library/turtle.html#turtle.setup "turtle.setup")
     method.
    
*   Line 5 and 6 correspond to the arguments of the method [`Screen.screensize`](https://docs.python.org/3/library/turtle.html#turtle.screensize "turtle.screensize")
    .
    
*   _shape_ can be any of the built-in shapes, e.g: arrow, turtle, etc. For more info try `help(shape)`.
    
*   If you want to use no fill color (i.e. make the turtle transparent), you have to write `fillcolor = ""` (but all nonempty strings must not have quotes in the cfg file).
    
*   If you want to reflect the turtle its state, you have to use `resizemode = auto`.
    
*   If you set e.g. `language = italian` the docstringdict `turtle_docstringdict_italian.py` will be loaded at import time (if present on the import path, e.g. in the same directory as `turtle`).
    
*   The entries _exampleturtle_ and _examplescreen_ define the names of these objects as they occur in the docstrings. The transformation of method-docstrings to function-docstrings will delete these names from the docstrings.
    
*   _using\_IDLE_: Set this to `True` if you regularly work with IDLE and its `-n` switch (“no subprocess”). This will prevent [`exitonclick()`](https://docs.python.org/3/library/turtle.html#turtle.exitonclick "turtle.exitonclick")
     to enter the mainloop.
    

There can be a `turtle.cfg` file in the directory where `turtle` is stored and an additional one in the current working directory. The latter will override the settings of the first one.

The `Lib/turtledemo` directory contains a `turtle.cfg` file. You can study it as an example and see its effects when running the demos (preferably not from within the demo-viewer).

Explanation[¶](https://docs.python.org/3/library/turtle.html#explanation "Link to this heading")

-------------------------------------------------------------------------------------------------

A turtle object draws on a screen object, and there a number of key classes in the turtle object-oriented interface that can be used to create them and relate them to each other.

A [`Turtle`](https://docs.python.org/3/library/turtle.html#turtle.Turtle "turtle.Turtle")
 instance will automatically create a [`Screen`](https://docs.python.org/3/library/turtle.html#turtle.Screen "turtle.Screen")
 instance if one is not already present.

`Turtle` is a subclass of [`RawTurtle`](https://docs.python.org/3/library/turtle.html#turtle.RawTurtle "turtle.RawTurtle")
, which _doesn’t_ automatically create a drawing surface - a _canvas_ will need to be provided or created for it. The _canvas_ can be a `tkinter.Canvas`, [`ScrolledCanvas`](https://docs.python.org/3/library/turtle.html#turtle.ScrolledCanvas "turtle.ScrolledCanvas")
 or [`TurtleScreen`](https://docs.python.org/3/library/turtle.html#turtle.TurtleScreen "turtle.TurtleScreen")
.

[`TurtleScreen`](https://docs.python.org/3/library/turtle.html#turtle.TurtleScreen "turtle.TurtleScreen")
 is the basic drawing surface for a turtle. [`Screen`](https://docs.python.org/3/library/turtle.html#turtle.Screen "turtle.Screen")
 is a subclass of `TurtleScreen`, and includes [some additional methods](https://docs.python.org/3/library/turtle.html#screenspecific)
 for managing its appearance (including size and title) and behaviour. `TurtleScreen`’s constructor needs a `tkinter.Canvas` or a [`ScrolledCanvas`](https://docs.python.org/3/library/turtle.html#turtle.ScrolledCanvas "turtle.ScrolledCanvas")
 as an argument.

The functional interface for turtle graphics uses the various methods of `Turtle` and `TurtleScreen`/`Screen`. Behind the scenes, a screen object is automatically created whenever a function derived from a `Screen` method is called. Similarly, a turtle object is automatically created whenever any of the functions derived from a Turtle method is called.

To use multiple turtles on a screen, the object-oriented interface must be used.

`turtledemo` — Demo scripts[¶](https://docs.python.org/3/library/turtle.html#module-turtledemo "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

The `turtledemo` package includes a set of demo scripts. These scripts can be run and viewed using the supplied demo viewer as follows:

Copy

python \-m turtledemo

Alternatively, you can run the demo scripts individually. For example,

Copy

python \-m turtledemo.bytedesign

The `turtledemo` package directory contains:

*   A demo viewer `__main__.py` which can be used to view the sourcecode of the scripts and run them at the same time.
    
*   Multiple scripts demonstrating different features of the `turtle` module. Examples can be accessed via the Examples menu. They can also be run standalone.
    
*   A `turtle.cfg` file which serves as an example of how to write and use such files.
    

The demo scripts are:

| Name | Description | Features |
| --- | --- | --- |
| `bytedesign` | complex classical turtle graphics pattern | [`tracer()`](https://docs.python.org/3/library/turtle.html#turtle.tracer "turtle.tracer")<br>, [`delay()`](https://docs.python.org/3/library/turtle.html#turtle.delay "turtle.delay")<br>, [`update()`](https://docs.python.org/3/library/turtle.html#turtle.update "turtle.update") |
| `chaos` | graphs Verhulst dynamics, shows that computer’s computations can generate results sometimes against the common sense expectations | world coordinates |
| `clock` | analog clock showing time of your computer | turtles as clock’s hands, [`ontimer()`](https://docs.python.org/3/library/turtle.html#turtle.ontimer "turtle.ontimer") |
| `colormixer` | experiment with r, g, b | [`ondrag()`](https://docs.python.org/3/library/turtle.html#turtle.ondrag "turtle.ondrag") |
| `forest` | 3 breadth-first trees | randomization |
| `fractalcurves` | Hilbert & Koch curves | recursion |
| `lindenmayer` | ethnomathematics (indian kolams) | L-System |
| `minimal_hanoi` | Towers of Hanoi | Rectangular Turtles as Hanoi discs ([`shape()`](https://docs.python.org/3/library/turtle.html#turtle.shape "turtle.shape")<br>, [`shapesize()`](https://docs.python.org/3/library/turtle.html#turtle.shapesize "turtle.shapesize")<br>) |
| `nim` | play the classical nim game with three heaps of sticks against the computer. | turtles as nimsticks, event driven (mouse, keyboard) |
| `paint` | super minimalistic drawing program | [`onclick()`](https://docs.python.org/3/library/turtle.html#turtle.onclick "turtle.onclick") |
| `peace` | elementary | turtle: appearance and animation |
| `penrose` | aperiodic tiling with kites and darts | [`stamp()`](https://docs.python.org/3/library/turtle.html#turtle.stamp "turtle.stamp") |
| `planet_and_moon` | simulation of gravitational system | compound shapes, [`Vec2D`](https://docs.python.org/3/library/turtle.html#turtle.Vec2D "turtle.Vec2D") |
| `rosette` | a pattern from the wikipedia article on turtle graphics | [`clone()`](https://docs.python.org/3/library/turtle.html#turtle.clone "turtle.clone")<br>, [`undo()`](https://docs.python.org/3/library/turtle.html#turtle.undo "turtle.undo") |
| `round_dance` | dancing turtles rotating pairwise in opposite direction | compound shapes, [`clone()`](https://docs.python.org/3/library/turtle.html#turtle.clone "turtle.clone")<br> [`shapesize()`](https://docs.python.org/3/library/turtle.html#turtle.shapesize "turtle.shapesize")<br>, [`tilt()`](https://docs.python.org/3/library/turtle.html#turtle.tilt "turtle.tilt")<br>, [`get_shapepoly()`](https://docs.python.org/3/library/turtle.html#turtle.get_shapepoly "turtle.get_shapepoly")<br>, [`update()`](https://docs.python.org/3/library/turtle.html#turtle.update "turtle.update") |
| `sorting_animate` | visual demonstration of different sorting methods | simple alignment, randomization |
| `tree` | a (graphical) breadth first tree (using generators) | [`clone()`](https://docs.python.org/3/library/turtle.html#turtle.clone "turtle.clone") |
| `two_canvases` | simple design | turtles on two canvases |
| `yinyang` | another elementary example | [`circle()`](https://docs.python.org/3/library/turtle.html#turtle.circle "turtle.circle") |

Have fun!

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`turtle` — Turtle graphics](https://docs.python.org/3/library/turtle.html#)
    *   [Tutorial](https://docs.python.org/3/library/turtle.html#tutorial)
        *   [Starting a turtle environment](https://docs.python.org/3/library/turtle.html#starting-a-turtle-environment)
            
        *   [Basic drawing](https://docs.python.org/3/library/turtle.html#basic-drawing)
            *   [Pen control](https://docs.python.org/3/library/turtle.html#pen-control)
                
            *   [The turtle’s position](https://docs.python.org/3/library/turtle.html#the-turtle-s-position)
                
        *   [Making algorithmic patterns](https://docs.python.org/3/library/turtle.html#making-algorithmic-patterns)
            
    *   [Reference](https://docs.python.org/3/library/turtle.html#reference)
        *   [Turtle methods and functions](https://docs.python.org/3/library/turtle.html#turtle-methods-and-functions)
            *   [Move and draw](https://docs.python.org/3/library/turtle.html#move-and-draw)
                
            *   [Tell Turtle’s state](https://docs.python.org/3/library/turtle.html#tell-turtle-s-state)
                
            *   [Settings for measurement](https://docs.python.org/3/library/turtle.html#settings-for-measurement)
                
            *   [Pen control](https://docs.python.org/3/library/turtle.html#id1)
                *   [Drawing state](https://docs.python.org/3/library/turtle.html#drawing-state)
                    
                *   [Color control](https://docs.python.org/3/library/turtle.html#color-control)
                    
                *   [Filling](https://docs.python.org/3/library/turtle.html#filling)
                    
                *   [More drawing control](https://docs.python.org/3/library/turtle.html#more-drawing-control)
                    
            *   [Turtle state](https://docs.python.org/3/library/turtle.html#turtle-state)
                *   [Visibility](https://docs.python.org/3/library/turtle.html#visibility)
                    
                *   [Appearance](https://docs.python.org/3/library/turtle.html#appearance)
                    
            *   [Using events](https://docs.python.org/3/library/turtle.html#using-events)
                
            *   [Special Turtle methods](https://docs.python.org/3/library/turtle.html#special-turtle-methods)
                
        *   [Screen methods and functions](https://docs.python.org/3/library/turtle.html#screen-methods-and-functions)
            *   [Window control](https://docs.python.org/3/library/turtle.html#window-control)
                
            *   [Animation control](https://docs.python.org/3/library/turtle.html#animation-control)
                
            *   [Using screen events](https://docs.python.org/3/library/turtle.html#using-screen-events)
                
            *   [Input methods](https://docs.python.org/3/library/turtle.html#input-methods)
                
            *   [Settings and special methods](https://docs.python.org/3/library/turtle.html#settings-and-special-methods)
                
            *   [Screen-only methods](https://docs.python.org/3/library/turtle.html#screen-only-methods)
                
        *   [Public classes](https://docs.python.org/3/library/turtle.html#public-classes)
            
        *   [Exceptions](https://docs.python.org/3/library/turtle.html#exceptions)
            
    *   [How-to guides](https://docs.python.org/3/library/turtle.html#how-to-guides)
        *   [How to automatically begin and end filling](https://docs.python.org/3/library/turtle.html#how-to-automatically-begin-and-end-filling)
            
        *   [How to use compound shapes](https://docs.python.org/3/library/turtle.html#how-to-use-compound-shapes)
            
        *   [How to use the `turtle` module namespace](https://docs.python.org/3/library/turtle.html#how-to-use-the-turtle-module-namespace)
            
        *   [How to use turtle graphics in a script](https://docs.python.org/3/library/turtle.html#how-to-use-turtle-graphics-in-a-script)
            
        *   [How to use object-oriented turtle graphics](https://docs.python.org/3/library/turtle.html#how-to-use-object-oriented-turtle-graphics)
            
        *   [How to use `help()`](https://docs.python.org/3/library/turtle.html#how-to-use-help)
            
        *   [Translation of docstrings into different languages](https://docs.python.org/3/library/turtle.html#translation-of-docstrings-into-different-languages)
            
        *   [How to configure Screen and Turtles](https://docs.python.org/3/library/turtle.html#how-to-configure-screen-and-turtles)
            
    *   [Explanation](https://docs.python.org/3/library/turtle.html#explanation)
        
    *   [`turtledemo` — Demo scripts](https://docs.python.org/3/library/turtle.html#module-turtledemo)
        

#### Previous topic

[IDLE — Python editor and shell](https://docs.python.org/3/library/idle.html "previous chapter")

#### Next topic

[Development Tools](https://docs.python.org/3/library/development.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=turtle+%E2%80%94+Turtle+graphics&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fturtle.html&pagesource=library%2Fturtle.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/turtle.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/development.html "Development Tools")
     |
*   [previous](https://docs.python.org/3/library/idle.html "IDLE — Python editor and shell")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [Graphical user interfaces with Tk](https://docs.python.org/3/library/tk.html)
     »
*   [`turtle` — Turtle graphics](https://docs.python.org/3/library/turtle.html)
    
*    
    
    |
*   Theme Auto Light Dark |
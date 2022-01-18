import turtle
integer_check = True

print("Hello and welcome to N-Gon Creator Online!")

while integer_check == True:
    side_input_value = input("How many sides (3 or more) would you like your N-Gon to have?: ")
    #checks if input was an integer then checks if integer is < 3
    try:
        int(side_input_value)
        integer_check = True
            #print(f"{integer_check}")
        if int(side_input_value) < 3:
            print("Invalid input. Please try again")
        else:
            integer_check = False
    except ValueError:
            #print(f"{integer_check}")
        print("Invalid input. Please try again")
        continue

n_value = int(side_input_value)

#interior angle computation
interior_angle = ((n_value - 2) * 180) / n_value
print(f"{interior_angle}")

#interior angle to angle of turn for turtle
turn_angle = 180 - interior_angle

border_color = input("What color would you like the sides of your N-Gon to be?: ")
interior_color = input("And finally, what color would you like the interior of your N-Gon to be?: ")

#setting parameters for the turtle loop
position_check = False
side_tally = 0

#turtle setup
turtle.delay(100)
turtle.home()
turtle.pensize(10)
turtle.pencolor(border_color)
turtle.fillcolor(interior_color)
turtle.begin_fill()
turtle.begin_poly()

#turtle loops until it has drawn n-number of sides
while position_check == False:
    turtle.fd(100)
    turtle.left(turn_angle)
    side_tally += 1
    if side_tally == n_value:
        position_check = True

turtle.end_fill()
turtle.end_poly()
p = turtle.get_poly()

print("Click to exit N-Gon Creator Online")
turtle.Screen().exitonclick()
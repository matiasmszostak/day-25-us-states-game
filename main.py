from turtle import Turtle, Screen
import pandas


screen = Screen()
screen.title("U.S. State Game")
IMAGE = "blank_states_img.gif"

t = Turtle()

screen.addshape(IMAGE)
t.shape(IMAGE)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

#Check if the guess is among the 50 states
# Guardar los estados en una lista
# Recorrer la lista y ver si la respuesta coincide
# Si coincide, devolver True (por ahora)

data = pandas.read_csv("50_states.csv")

data_df = pandas.DataFrame(data)
print(data_df)

states_list = data["state"].tolist()
print(states_list)

x_list = data["x"].tolist()
y_list = data["y"].tolist()

location_list = []

iteration = 0

for x in x_list:
    location_list.append((x, y_list[iteration]))
    iteration += 1
print(location_list)




correct_answers = 0


data_dict = {
    "State": states_list,
    "Location": location_list
}

df = pandas.DataFrame(data_dict)
print(df)


FONT = ("Arial", 8, "bold")

def write_state(position, state):
    turtle = Turtle()
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(position)
    turtle.pencolor("green")
    turtle.write(state, align="center", font=FONT)




title = ""


game_is_on = True

while game_is_on:

    if correct_answers == 0:
        title = "Guess the State"
    else:
        title = f"{correct_answers}/50 States Correct"

    answer_state = screen.textinput(title=title, prompt="What's the State's name?").title()
    print(answer_state)

    if answer_state in states_list:
        print("correcto")
        states_list.remove(answer_state)
        correct_answers += 1
        print(states_list)

        state_location_x = data_df.loc[data_df["state"] == answer_state, "x"].values[0]
        state_location_y = data_df.loc[data_df["state"] == answer_state, "y"].values[0]
        location_position = (state_location_x, state_location_y)
        write_state(location_position, answer_state)






screen.exitonclick()
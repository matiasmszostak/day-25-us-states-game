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

# Check if the guess is among the 50 states
# Guardar los estados en una lista
# Recorrer la lista y ver si la respuesta coincide
# Si coincide, devolver True (por ahora)

data = pandas.read_csv("50_states.csv")

states_list = data["state"].to_list()

correct_answers = 0

FONT = ("Arial", 8, "bold")


def write_state(position, state, color):
    turtle = Turtle()
    turtle.speed("fastest")
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(position)
    turtle.pencolor(color)
    turtle.write(state, align="center", font=FONT)


def get_state_location(state_param):
    state_data = data[data.state == state_param]
    return int(state_data.x.iloc[0]), int(state_data.y.iloc[0])


def missing_states_csv():
    missing_states_dict = {
        "Missing States": states_list,
    }
    df_missing_states = pandas.DataFrame(missing_states_dict)
    df_missing_states.to_csv("states_to_learn.csv")


title = ""

game_is_on = True

while game_is_on:

    if correct_answers == 0:
        title = "Guess the State"
    else:
        title = f"{correct_answers}/50 States Correct"

    answer_state = screen.textinput(title=title, prompt="What's the State's name?").title()
    print(answer_state)

    if answer_state == "Exit":
        for state in states_list:
            location_position = get_state_location(state)
            write_state(location_position, state, color="red")

            # Create a csv file with all the missing States so the player can learn them better.
            missing_states_csv()
        break

    elif answer_state in states_list:
        states_list.remove(answer_state)
        correct_answers += 1

        location_position = get_state_location(answer_state)

        write_state(location_position, answer_state, color="green")

        if len(states_list) == 0:
            missing_states_csv()
            game_is_on = False

screen.exitonclick()

import turtle
import pandas as pd

us_states_data = pd.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

all_states = us_states_data.state.to_list()

list_guess_states = []

while len(list_guess_states) < 50:
    state_name = screen.textinput(f"{len(list_guess_states)}/50 States Correct", "Enter the name of the U.S. "
                                                                                 "States name: ").title()
    guess_state = us_states_data[us_states_data.state == state_name]
    if state_name == "Exit":
        learn_state = [state for state in all_states if state not in list_guess_states]
        new_df = pd.DataFrame(learn_state)
        new_df.to_csv("states_to_learn.csv")
        break
    if state_name in all_states:
        list_guess_states.append(state_name)
        x_cor = guess_state.x.values[0]
        y_cor = guess_state.y.values[0]
        my_stata_guess = turtle.Turtle()
        my_stata_guess.hideturtle()
        my_stata_guess.penup()
        my_stata_guess.goto(x_cor, y_cor)
        my_stata_guess.write(f"{state_name}", align="center", font=("Courier", 6, "normal"))

# How to get co-ordinates from screen
# def get_coor_on_mouse_click(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_coor_on_mouse_click)
# turtle.mainloop()

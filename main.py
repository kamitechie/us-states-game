import turtle
import pandas


screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title('U.S. States Game')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
cursor = turtle.Turtle()
cursor.penup()
cursor.hideturtle()
cursor.color("black")

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()

correct_states = []
while len(correct_states) < 50:
    correct = len(correct_states)
    answer_state = screen.textinput(title=f"{correct}/50 States Correct", prompt="What's another state's name?")
    title_answer = answer_state.title()

    if title_answer == "Exit":
        missing_states = [state for state in states_list if state not in correct_states]
        break

    if title_answer in states_list:
        state_row = data[data.state == title_answer]
        cursor.goto(int(state_row.x), int(state_row.y))
        cursor.write(title_answer)
        correct_states.append(title_answer)

learn_data = pandas.DataFrame(missing_states)
learn_data.to_csv("states_to_learn.csv")
screen.exitonclick()

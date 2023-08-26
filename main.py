import turtle
import pandas

screen = turtle.Screen()
screen.title('US States Game')
img = 'blank_states_img.gif'
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv('50_states.csv')
states: list[str] = data.state.to_list()

score = 0

while score < 50:
    guess = screen.textinput(title=f'{score}/50 States Correct', prompt="What's another state name?").title()
    if guess in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == guess]
        x = float(state_data.x.iloc[0])  # Access the first element of the Series and convert to float
        y = float(state_data.y.iloc[0])  # Access the first element of the Series and convert to float
        t.goto(x, y)
        t.write(guess, False, align='center', font=('Arial', 8, 'normal'))
        score += 1
        states.remove(guess)
    elif guess == 'Exit':
        break

new_data = pandas.DataFrame(states)
new_data.to_csv('states_to_learn.csv')

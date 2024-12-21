"""viz functions

This module does abc

Todo:
    * Clean code
    * Add return values

"""
import turtle

turtle.speed("fast")
newXPosition = 720/-2
newYPosition = 675/-2
print('Window height:' + str(newXPosition))
print('Window width:' + str(newYPosition))

def writeText(theText, x, y) :
    turtle.speed("fast")
    turtle.penup()
    turtle.goto(newXPosition + x, newYPosition + y)
    turtle.pendown()
    turtle.pencolor('blue')
    turtle.write(theText, True, align="left", font=("Arial", 20, "normal"))


def draw_bar(x, y, height, width, color):
    turtle.pencolor(color)
    turtle.pensize(0)
    turtle.penup()
    turtle.setposition(newXPosition + x, newYPosition + y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()

    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.end_fill()

# , plots the counts of the top k words in one document.
def plot_top_k_freq_words_doc(data, document, k):
    print('plot_top_k_freq_words_doc: ', end='')

    count = 0                                   # number of bars
    x_offset = 0                                # offset in pixels x axis
    values = list(data[document].values())  # extract values from dictionary
    values.sort(reverse=True)

    writeText('Top ' + str(k) + ' words in ' + document, 20, 300)

    for v in values[:k]:
        count += 1
        draw_bar(20*count, 100, v+100, 10, 'red')
        writeText(v, 20*count, v+220)

# plots the counts of the bottom k words in one document
def plot_bottom_k_freq_words_doc(data, document, k) :
    print('plot_top_k_freq_words_doc: ', end='')

# plots the counts of the “word” on the list of documents passed in doc_list
# the parameter data is the container to be used for this task
def plot_freq_word_doc(data, doc_list, word):
    print('plot_top__size_doc: ', end='')

def render() :
    turtle.update()  # Render image
    turtle.exitonclick()  # Wait for user's mouse click


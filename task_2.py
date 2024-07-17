import turtle

def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3.0
        koch(t, order-1, size)
        t.left(60)
        koch(t, order-1, size)
        t.right(120)
        koch(t, order-1, size)
        t.left(60)
        koch(t, order-1, size)

def snowflake(t, order, size):
    for _ in range(3):
        koch(t, order, size)
        t.right(120)

if __name__ == "__main__":
    order = int(input("Enter the recursion level: "))
    size = 300

    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    t = turtle.Turtle()
    t.speed(0)

    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    snowflake(t, order, size)

    turtle.done()

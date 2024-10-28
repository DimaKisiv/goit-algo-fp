import turtle

def draw_pythagoras_tree(branch_length, level, angle):
    if level == 0:
        return
    turtle.forward(branch_length)
    turtle.left(angle)
    draw_pythagoras_tree(branch_length * 0.8, level - 1, angle)
    turtle.right(2 * angle)
    draw_pythagoras_tree(branch_length * 0.8, level - 1, angle)
    turtle.left(angle)
    turtle.backward(branch_length)

def main():
    turtle.color("red")
    turtle.speed(1000)
    turtle.left(90)  
    turtle.up()
    turtle.backward(100) 
    turtle.down()
    level = int(input("Введіть рівень рекурсії: "))
    draw_pythagoras_tree(branch_length=100, level=level, angle=45)  
    turtle.done()

if __name__ == "__main__":
    main()

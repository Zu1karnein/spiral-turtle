# eng / ru
import turtle

# Create a screen / Создаем экран
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle / Создаем черепаху
artist = turtle.Turtle()
artist.speed(0)  #Highest speed / Наивысшая скорость

# Set the colors for the picture / Устанавливаем цвета для рисунка
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Draw a spiral / Рисуем спираль
for i in range(360):
    artist.color(colors[i % 6])  # Switch color / Переключаем цвет
    artist.forward(i * 10)  # Increasing stride length / Увеличиваем длину шага 
    artist.right(59)  # Rotate the turtle / Поворачиваем черепаху

# Finish drawing by clicking on the screen / Завершаем рисование при клике на экране
screen.exitonclick()
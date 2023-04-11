import turtle

def main():
  # Create a turtle object
  t = turtle.Turtle()

  # Set the turtle's speed
  t.speed(0)

  # Set the turtle's pen color
  t.pencolor('black')

  # Set the turtle's pen size
  t.pensize(3)

  # Set the turtle's initial position
  t.penup()
  t.goto(-100, 100)
  t.pendown()

  # Initialize variables
  total_cost = 0
  tax_rate = 0.08

  # Loop until the user is finished entering items
  while True:
    # Get the price of the item from the user
    price = input("Enter the price of the item (enter 'done' when finished): ")

    # Check if the user is finished
    if price.lower() == 'done':
      break

    # Convert the price to a float and add it to the total cost
    total_cost += float(price)

    # Draw the price on the screen
    t.write(price, align='center', font=('Arial', 24, 'bold'))
    t.forward(50)

  # Calculate the final total cost
  total_cost += total_cost * tax_rate

  # Draw the final total cost on the screen
  t.write("Total cost: $%.2f" % total_cost, align='center', font=('Arial', 24, 'bold'))

# Call the main function
if __name__ == '__main__':
  main()

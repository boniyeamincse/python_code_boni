# Birthday Calculator

print("Welcome to the Birthday Calculator!")  # Greeting message

# Ask for the user's name
name = input("What is your name? ")

# Greet the user and ask for their age
print(f"Hi {name}, please enter your age below.")
age = int(input("Enter your age: "))

# Calculate days, minutes, and seconds lived
days = age * 365
minutes = days * 24 * 60
seconds = minutes * 60

# Display the results
print(f"\n{name}, you have lived for approximately:")
print(f"- {days} days")
print(f"- {minutes} minutes")
print(f"- {seconds} seconds")

print(f"\nThank you for using the Birthday Calculator, {name}!")




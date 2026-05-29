# Function to calculate total steps
def calculate_total_steps(steps):
    return sum(steps)

# Function to calculate average steps
def calculate_average_steps(total):
    return total / 7

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

steps = []

# Input daily steps
for day in days:
    step = int(input("Enter steps for {day}: "))
    steps.append(step)

# Calculate totals
total_steps = calculate_total_steps(steps)
average_steps = calculate_average_steps(total_steps)

# Determine activity level
if average_steps >= 8000:
    activity = "Highly Active"
elif average_steps >= 5000:
    activity = "Moderately Active"
else:
    activity = "Low Activity"

# Display results
print("\nTotal steps this week:", total_steps)
print("Average steps per day:", round(average_steps, 2))
print("Activity level:", activity)
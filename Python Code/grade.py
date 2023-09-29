# Grade Calculator in Python tkinter
# This is Bing

# Import tkinter module
import tkinter as tk

# Create a root window object
root = tk.Tk()

# Set the title and size of the window
root.title('Grade Calculator')
root.geometry('900x500')

# Create a label to display the instructions
label = tk.Label(root, text='Enter your score (0-100) and click Calculate', font=("SF Pro Display", 20))
label.pack()

# Create an entry to get the user input
entry = tk.Entry(root)
entry.pack()

# Create a function to calculate the grade based on the score
def calculate_grade():
    # Get the score from the entry
    score = int(entry.get())

    # Check the range of the score and assign the corresponding grade
    if 0 <= score <= 59:
        grade = 'F'
    elif 60 <= score <= 62:
        grade = 'D-'
    elif 63 <= score <= 66:
        grade = 'D'
    elif 67 <= score <= 69:
        grade = 'D+'
    elif 70 <= score <= 72:
        grade = 'C-'
    elif 73 <= score <= 76:
        grade = 'C'
    elif 77 <= score <= 79:
        grade = 'C+'
    elif 80 <= score <= 82:
        grade = 'B-'
    elif 83 <= score <= 86:
        grade = 'B'
    elif 87 <= score <= 89:
        grade = 'B+'
    elif 90 <= score <= 92:
        grade = 'A-'
    elif 93 <= score <= 96:
        grade = 'A'
    elif 97 <= score <= 100:
        grade = 'A+'
    else:
        # If the score is invalid, display an error message
        grade = 'Invalid score'

    # Display the grade on the screen
    result.config(text=f'Your grade is {grade}', font=("SF Pro Display", 15))

# Create a button to invoke the calculate_grade function
button = tk.Button(root, text='Calculate', command=calculate_grade)
button.pack()

# Create a label to display the result
result = tk.Label(root, text='')
result.pack()

# Start the main loop of the window
root.mainloop()

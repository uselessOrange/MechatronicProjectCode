import tkinter as tk
#WhereIsRobot
def GUI():


    # Create the main window
    window = tk.Tk()
    window.title("Button GUI")

    # Function to handle button clicks
    def button_click(button_num):
        output_variable.set(f"T{button_num}")
        WhereRobotGoing=(f"T{button_num}")
        print(WhereRobotGoing)
    # Create the buttons
    button1 = tk.Button(window, text="Button 1", command=lambda: button_click(1))
    button1.pack(pady=10)

    button2 = tk.Button(window, text="Button 2", command=lambda: button_click(2))
    button2.pack(pady=10)

    # Create the label to display the output
    output_variable = tk.StringVar()
    output_label = tk.Label(window, textvariable=output_variable)
    output_label.pack()

    # Start the GUI main loop
    window.mainloop()

GUI()
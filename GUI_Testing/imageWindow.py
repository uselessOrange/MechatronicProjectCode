import PySimpleGUI as sg

# Specify the image file path
image_path = "/home/miko/Desktop/proj/GUI_Testing/TableGrid.jpg"

# Create the layout of the window
layout = [[sg.Graph(canvas_size=(400, 400), graph_bottom_left=(0, 400), graph_top_right=(400, 0), key="-GRAPH-")]]

# Create the window
window = sg.Window("Image Window", layout, finalize=True)

# Get the graph element from the layout
graph = window["-GRAPH-"]

# Draw the image on the graph canvas
graph.draw_image(image_path, location=(0, 400))

# Read events from the window
while True:
    event, values = window.read()

    # Break the loop if the window is closed
    if event == sg.WINDOW_CLOSED:
        break

# Close the window
window.close()

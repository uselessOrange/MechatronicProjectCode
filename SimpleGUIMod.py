import PySimpleGUI as psg

def buttonEventMod():
    layout = [
   [psg.Text('Where is the robot: '), psg.Input(key='WhereIsRobot')],
   [psg.Text('Where is the robot going '), psg.Input(key='WhereRobotGoing')],
   [psg.Text('Result : '), psg.Text(key='-OUT-')],
   [psg.Button("GO", key='-GO-'), psg.Exit()],
]

    window = psg.Window('Calculator', layout)
    while True:
        event, values = window.read()

        if event == "-GO-":
            print("path calculated")

        if event == psg.WIN_CLOSED or event == 'Exit':
            break

        window['-OUT-'].update("path calculated")
    window.close()
    return values["WhereIsRobot"], values["WhereRobotGoing"]

import webbrowser
import PySimpleGUI as sg

# link text font
font = ('Courier New', 16, 'underline')

layout = [
    [sg.Text("Go to Google", enable_events=True, font=font, key="URL https://www.google.com/")],
    [sg.Text("Go to Apple", enable_events=True, font=font, key="URL https://www.apple.com/")]
]

window = sg.Window("Hyper Link Sample", layout, size=(250, 100), finalize=True)

while True:
    event, values = window.read()
    print(event, values)

    if event == sg.WINDOW_CLOSED:
        break
    elif event.startswith("URL "):
        url = event.split(' ')[1]
        print("URL: ", url)
        webbrowser.open(url)


window.close()

from flask import Flask, render_template
import socket
import random
import PySimpleGUI as sg
app = Flask(__name__)

# Function for getting the user's IP Address to use as the site address
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
        return (IP)

IP_Address = get_ip()

# The port is randomized so the program can be run on multiple devices
# at the same time on the same IP
port = random.randint(1000, 9999)

link = ("http://" + IP_Address + ":" + str(port))

layout = [
    [sg.Text("Paste your text here:", font=('Sans Serif', 18), text_color='black', justification='center',
             background_color='white', relief=sg.RELIEF_RAISED)],
    [sg.Multiline(size=(50, 10), auto_size_text=True, background_color='white', text_color='black')],
    [sg.Text("Your text will be available at: %s" % link, font=('Sans Serif', 13))],
    [sg.ReadButton('OK', size=(4, 1), font=('Monospaced', 18), tooltip='Submit Text'), sg.ReadButton('Close', size=(5, 1), font=('Monospaced', 18), tooltip='Close Window')]
]

window = sg.Window('PySimpleGUI Learning', background_color='white',
                   auto_size_buttons=True, resizable=True, grab_anywhere=True).Layout(layout)

@app.route('/')
def webpage():
    return render_template("home.html", text=str(text), IP_Address=get_ip())

while True:
    (event, value) = window.Read()
    if event == 'OK':
        text = value
        # Running the web app
        if __name__=='__main__':
            app.run(host=str(IP_Address), port=int(port))
        print('OK clicked')
    elif event == 'Close':
        print('Close clicked')
        break

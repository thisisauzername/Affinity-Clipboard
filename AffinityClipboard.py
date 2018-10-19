from flask import Flask, render_template
import socket
import random
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

link = Label(master, text="Your text will be available at: http://" + IP_Address + ":" + str(port) + "/", width=100, height=3)
link.pack()

input = input("")

# Running the web app
@app.route('/')
def webpage():
    return render_template("home.html", text=str(input), IP_Address=get_ip())

if __name__=='__main__':
    app.run(host=str(IP_Address), port=int(port))

from flask import Flask, render_template
import socket
import random
app = Flask(__name__)

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
        return (IP)

IP_Address = get_ip()

text = input("\nPaste your text here: \n")

port = random.randint(1000, 9999)

@app.route('/')
def webpage():
    return render_template("home.html", text=str(text), IP_Address=get_ip())

if __name__=='__main__':
    app.run(host=str(IP_Address), port=int(port))

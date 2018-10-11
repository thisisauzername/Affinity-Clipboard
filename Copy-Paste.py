from flask import Flask
import socket
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

print(IP_Address)

text = input("Paste your text here: \n")

@app.route('/')
def display():
    return (text)

if __name__=='__main__':
    app.run(host=str(IP_Address), port=3134)

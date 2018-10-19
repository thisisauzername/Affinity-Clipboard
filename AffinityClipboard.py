import tkinter as tk
from tkinter import *
from flask import Flask, render_template
import socket
import random
import time
app = Flask(__name__)

master = Tk()
master.title("Affinity Clipboard")
master.geometry("500x500")
master.resizable(0, 0)

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

scrollbar = Scrollbar(master)
scrollbar.pack(side=RIGHT, fill=Y)

instruct = Label(master, text="Paste your text here: ", width=30, height=2)
instruct.pack()

text = Text(master, yscrollcommand=scrollbar.set, width=50, height=15)
text.pack()

def retrieve_input():
    input = text.get("1.0",END)

b = Button(master, text="OK", command=retrieve_input, width=5, height=2)
b.pack()

port = random.randint(1000, 9999)

link = Label(master, text="Your text is available at: http://" + IP_Address + ":" + str(port) + "/", width=100, height=3)
link.pack()

@app.route('/')
def webpage():
    return render_template("home.html", text=str(input), IP_Address=get_ip())

if __name__=='__main__':
    app.run(host=str(IP_Address), port=int(port))

# Online Copy Paste
This program is meant to be used to be able to copy and paste a piece of text on a machine different from the one it was copied one.

## How it Works

This simple program works using Flask. It asks for the text and puts it on a simple webpage hosted on your IP address. You can then access that webpage on any device **connected to the same network.**

## Instructions

If Flask is not already installed on your computer, go into the Command Prompt / Terminal and install Flask:

    pip install flask

##### NOTE: You only need to run this program on the machine you are sending the text from.

Once Flask has installed, run the program.

Wherever you run the program, you should see this once you paste your text:

    * Running on http://x.x.x.x:3134/

The `x` will be your IP address.

On the machine you want to copy the text to, just go to that webpage and you will find the text there.

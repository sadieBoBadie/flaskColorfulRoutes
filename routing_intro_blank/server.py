from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)

######### Let's add some routes! #########

if __name__ == "__main__":
    app.run(debug=True)
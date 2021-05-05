import socket
from flask import Flask, request, render_template

app = Flask(__name__)
print("Server is created...")
@app.route('/')
def index():
    return render_template('index.html', value=10)

@app.route('/click', methods=['POST', 'GET'])
def click():
    var = request.form['sliderValue']
    print(var)
    clientsocket.send(bytes(var, "utf-8"))
    return render_template('index.html', value=var)

if __name__ == "__main__":
    s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    s.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
    s.bind( (socket.gethostname(), 5000) )
    s.listen( 5 )
    clientsocket, address = s.accept()
    print( f"Connection from {address} has been established." )
    app.run()

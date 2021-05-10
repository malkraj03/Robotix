import socket
from flask import Flask, request, render_template

app = Flask(__name__)
print("Server is created...")
@app.route('/')
def index():
    return render_template('index.html', value=25)


# I've added this method to receive slider updates
@app.route('/slider_update', methods=['POST', 'GET'])
def slider():
    var = request.data
    print(var)
    clientsocket.send(bytes(str(var), "utf-8"))
    return render_template('index.html')

@app.route('/slider_act', methods=['POST', 'GET'])
def slideract():
    act = request.data
    print(act)
    clientsocket.send(bytes(str(act), "utf-8"))
    return render_template('index.html')

if __name__ == "__main__":
    s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
    s.bind((socket.gethostname(), 5000))
    s.listen(5)
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    app.run()

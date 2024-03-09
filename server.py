import socketio

from frappe import process_weight_data

sio = socketio.Server(cors_allowed_origins='*')


@sio.event
def connect(sid, environ):
    print('Client connected:', sid)


@sio.event
def disconnect(sid):
    print('Client disconnected:', sid)


@sio.event
def weight_data(sid, data):
    print('Received weight data:', data)
   
    process_weight_data(data)


if __name__ == '__main__':
    app = socketio.WSGIApp(sio)
    from gevent.pywsgi import WSGIServer
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()

import socketio

sio = socketio.Client()

sio.connect('http://localhost:5000')


while True:
    sio.emit('weight_data', {'weight': 100, 'timestamp': '2023-04-01T12:00:00'})
    sio.emit('weight_data', {'weight': 100, 'timestamp': '2023-04-01T12:00:00'})
    sio.emit('weight_data', {'weight': 100, 'timestamp': '2023-04-01T12:00:00'})
    sio.emit('weight_data', {'weight': 100, 'timestamp': '2023-04-01T12:00:00'})
    sio.emit('weight_data', {'weight': 100, 'timestamp': '2023-04-01T12:00:00'})
    sio.emit('weight_data', {'weight': 100, 'timestamp': '2023-04-01T12:00:00'})
    sio.emit('weight_data', {'weight': 100, 'timestamp': '2023-04-01T12:00:00'})

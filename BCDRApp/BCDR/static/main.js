const socket = new WebSocket('ws://localhost:8000/ws/updates/');

socket.onmessage = function(event) {
    const data = JSON.parse(event.data);
    console.log(data.message);
};

socket.onclose = function(event) {
    if (event.wasClean) {
        console.log(`Connection closed cleanly, code=${event.code}, reason=${event.reason}`);
    } else {
        console.log('Connection died');
    }
};

socket.onerror = function(error) {
    console.error(`[error] ${error.message}`);
};

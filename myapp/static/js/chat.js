const id = JSON.parse(document.getElementById('json-username').textContent);
const message_username = JSON.parse(document.getElementById('json-message-username').textContent);

const webSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/'
    + id
    + '/'
);

webSocket.onopen = function (e) {
    console.log("CONNECTION ESTABLISHED");
}

webSocket.onclose = function (e) {
    console.log("CONNECTION LOST");
}

webSocket.onerror = function (e) {
    console.log("ERROR OCCURED");
}

webSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    console.log("Data:" + data);
    document.querySelector('#chat-body').innerHTML += `<tr><td><p>${data.username}: ${data.message}</p></td></tr>`
}

document.querySelector('#chat-message-submit').onclick = function (e) {
    const message_input = document.querySelector('#message_input');
    const message = message_input.value;
    console.log('Message: ' + message + 'Username: ' + message_username)

    webSocket.send(JSON.stringify({
        'message': message,
        'username': message_username
    }));

    message_input.value = '';
}
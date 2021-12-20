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
    if (data.username == message_username) {
        document.querySelector('#chat-body').innerHTML += `<tr style="text-align: right;"> 
                                                                <td class="sent-message">
                                                                    <div class="blue_box">
                                                                        <span>
                                                                            ${data.message}
                                                                        </span>
                                                                    </div>
                                                                </td>
                                                            </tr>`
    } else {
        document.querySelector('#chat-body').innerHTML += `<tr style="text-align: left;">
                                                                <td class="received-message">
                                                                    <div class="green_box">
                                                                        <span>
                                                                            ${data.message}
                                                                        </span>
                                                                    </div>
                                                                </td>
                                                            </tr>`
    }
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
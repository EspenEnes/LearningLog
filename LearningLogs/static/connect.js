/**
 * Created by Espen on 16.05.2017.
 */

var open = false;

socket = new WebSocket('ws://' + window.location.host);

socket.onopen = function () {
    socket.send('Connected');
    open = true;

}

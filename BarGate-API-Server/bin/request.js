const request = require('request');

const gatePort = 8080;

const COMMANDS = {
    OPEN: 'open',
    MESSAGE: 'message'
};

const gateOpen = (gateIP, barCode) => {
    sendSimpleRequest(gateIP, gatePort, {command : COMMANDS.OPEN, barCode: barCode});
};

const gateMessage = (gateIP, message) => {
    sendSimpleRequest(gateIP, gatePort, {command : COMMANDS.OPEN, message: message});
};



const sendSimpleRequest = (ip, port, data = {}) => {
    request.post({url: 'http://' + ip + ':' + port + '/', form: data},
        (err, resp, body) => {
            if(err)
                console.error(err);
        }
    );
};

module.exports = {
    gateOpen,
    gateMessage
};
const request = require('request');

const gatePort = 8080;

const COMMANDS = {
    CLOSED: 'closed'
};

const gateClosed = (apiIP, gateNumber) => {
    sendSimpleRequest(apiIP, gatePort, {command : COMMANDS.CLOSED, gateNumber: gateNumber});
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
    gateClosed
};
const request = require('request');

const gatePort = 8080;

const gateOpen = (gateIP, barCode) => {
    sendGraphqlRequest(gateIP, gatePort, `{ open(barCode: "${barCode}") }`, console.info);
};

const gateMessage = (gateIP, message) => {
    sendGraphqlRequest(gateIP, gatePort, `{ message(message: ${message}) }`, console.info);
};

const sendGraphqlRequest = (ip, port, query, callback = (body) => {}) => {
    sendSimpleRequest(ip, port, {query: query}, (json) => {callback(JSON.parse(json)); }, '/graphql');
};

const sendSimpleRequest = (ip, port, data = {}, callback = (body) => {}, path = '/') => {
    console.info(data);
    request.post({url: 'http://' + ip + ':' + port + path, form: data},
        (err, resp, body) => {
            if(err)
                return console.error(err);

            callback(body);
        }
    );
};

module.exports = {
    gateOpen,
    gateMessage
};
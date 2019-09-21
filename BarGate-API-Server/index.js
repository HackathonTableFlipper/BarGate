const express = require('express');
const fs = require('fs')
const https = require('https')

const app = express();

app.use(express.static('public'));
app.use('/graphql', require('./routes/graphql'));

// openssl req -nodes -new -x509 -keyout server.key -out server.cert
https.createServer({
    key: fs.readFileSync('server.key'),
    cert: fs.readFileSync('server.cert')
}, app)
.listen(3000, function () {
    console.log('Example app listening on port 3000! Go to https://localhost:3000/')
});
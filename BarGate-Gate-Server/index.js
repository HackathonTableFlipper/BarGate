const express = require('express');

const app = express();

app.use('/graphql', require('./routes/graphql'));

app.listen(8080);
console.log('Running a GraphQL API server at localhost:8080/graphql');
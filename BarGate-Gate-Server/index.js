const express = require('express');

const app = express();

app.use('/graphql', require('./routes/graphql'));

app.listen(4000);
console.log('Running a GraphQL API server at localhost:4000/graphql');
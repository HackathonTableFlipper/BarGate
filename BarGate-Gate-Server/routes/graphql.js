const graphqlHTTP = require('express-graphql');
const { buildSchema } = require('graphql');

const request = require('../bin/request');

// Construct a schema, using GraphQL schema language
const schema = buildSchema(`
  type Query {
    gateOpen(barCode: String!): String,
    message(message: String!): String
  }
`);


let gateTimer = 0
let isGateOpen = false
const timeGateIsOpenInMs = 10000
const gateNumber = 1
const APIServerIP = "10.200.24.232"

// The root provides a resolver function for each API endpoint
const root = {
    gateOpen: ({barCode}) => {
        gateTimer = Date.now()
        isGateOpen = true
        // TODO open gate via python
        // TODO light green light
        console.info("Barcode: "+barCode+" can go")
        return "OK";
    },
    gateMessage : ({message}) => {
        console.info(message);
        // TODO light yellow light
        return "OK";
    }
};

module.exports = graphqlHTTP({
    schema: schema,
    rootValue: root,
    graphiql: true,
});

setInterval(() => {
    if(isGateOpen && Date.now() - gateTimer > timeGateIsOpenInMs)
    {
        // TODO close Gate via python
        // TODO light red light        
        request.gateClosed(APIServerIP, gateNumber)
        isGateOpen = false;
    }
}, 2000)
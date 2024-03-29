const graphqlHTTP = require('express-graphql');
const { buildSchema } = require('graphql');

const request = require('../bin/request');
const gates = require('../data/gates');

// Construct a schema, using GraphQL schema language
const schema = buildSchema(`
  type Query {
    gates: [Int],
    gateOpen(gateNumber: Int!, carCode: String): String,
    gateClosed(gateNumber: Int!): String
  }
`);

// The root provides a resolver function for each API endpoint
const root = {
    gates: () => {
        return Object.keys(gates);
    },
    gateOpen: ({gateNumber, carCode}) => {
        if(carCode) {
            request.gateOpen(gates[gateNumber].ip, carCode);
        } else {
            request.gateMessage(gates[gateNumber].ip, 'no-barcode');
        }
        return "OK";
    },
    gateClosed : ({gateNumber}) => {
        console.info(`Gate Number '${gateNumber}' is closed`);
        return "OK";
    }
};

module.exports = graphqlHTTP({
    schema: schema,
    rootValue: root,
    graphiql: true,
});
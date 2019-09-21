const graphqlHTTP = require('express-graphql');
const { buildSchema } = require('graphql');
const PythonShell = require('python-shell');
const spawn = require('child_process').spawn;

const request = require('../bin/request');

// Construct a schema, using GraphQL schema language
const schema = buildSchema(`
  type Query {
    open(barCode: String!): String,
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
    open: ({barCode}) => {
        gateTimer = Date.now()
	if(isGateOpen) return 'Already Open!';
        isGateOpen = true
	spawn('python', ['./../ServoControl.py', 'open'])
        console.info("opened gate")
        spawn('python', ['./../Trafficlight/LED.py', '010'])
        console.info("switched light to green")
        console.info("Barcode: "+barCode+" can go")
        return "OK";
    },
    message: ({message}) => {
        console.info("received Message:"+ message);
        spawn('python', ['./../Trafficlight/LED.py', '001'])
        console.info("switched light to yellow")
        return "OK";
    }
};

module.exports = graphqlHTTP({
    schema: schema,
    rootValue: root,
    graphiql: true,
});

setInterval(() => {
    if (!isGateOpen)
    {
	return
    }
    // TODO check LAZOR
    pythonProcess = spawn('python', ['./../LightBarrier.py'])
    pythonProcess.stdout.on('data', (data) => {
	console.info("light barrier state = "+ data)
        if(data | 0)
	{	     
             gateTimer = Date.now()
	}
    });
    if(Date.now() - gateTimer > timeGateIsOpenInMs)
    {       
	spawn('python', ['./../ServoControl.py', 'close'])
        console.info("closing gate")
        spawn('python', ['./../Trafficlight/LED.py', '100'])
        console.info("switched light to red")     
        // request.gateClosed(APIServerIP, gateNumber)
        console.info("informing api server")
        isGateOpen = false;
    }    
}, 2000)

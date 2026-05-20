// ========================================================
// Main Entry Point: Basic Node.js Application
// ========================================================

// Importing Express - our production web server framework
const express = require('express');
const app = express();

// Defining a standard configuration port
const PORT = 3000;

// Log a basic verification message immediately when script initiates
console.log("Initializing Node.js Runtime Engine...");

// Configuring a fundamental HTTP GET endpoint at the root path ('/')
app.get('/', (req, res) => {
    console.log(`[Server Log]: Intercepted incoming request at timestamp: ${new Date().toISOString()}`);
    res.send("Hello World! My Node.js application environment is perfectly configured and operational.");
});

// Binding the application server to the specified network port
app.listen(PORT, () => {
    console.log(`====================================================`);
    printEnvironmentDetails();
    console.log(` -> Live Application Endpoint: http://localhost:${PORT}`);
    console.log(`====================================================`);
});

// Helper function to cleanly display environment details in the terminal
function printEnvironmentDetails() {
    console.log(`SUCCESS: Core Node.js Web Server Activated.`);
    console.log(`Active Execution Platform: Node.js ${process.version}`);
    console.log(`Process Memory Allocation: ${(process.memoryUsage().heapUsed / 1024 / 1024).toFixed(2)} MB`);
}
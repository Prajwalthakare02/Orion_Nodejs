// ==========================================
// Custom Native HTTP API: server.js
// ==========================================

import http from 'http';
import { URL } from 'url';

const PORT = 3000;

// Local in-memory dataset acting as our database repository
let usersCollection = [
    { id: 1, name: "Prajwal Thakare", role: "Software Engineer" },
    { id: 2, name: "Alice Smith", role: "Data Scientist" }
];

// Instantiating the raw HTTP server context block
const server = http.createServer((req, res) => {
    // Parse the incoming request URL string natively
    // We provide a fallback base because relative paths cannot be evaluated directly by the URL constructor
    const parsedUrl = new URL(req.url, `http://${req.headers.host}`);
    const pathname = parsedUrl.pathname;
    const method = req.method;

    console.log(`[Server Stream]: Intercepted ${method} request at path ${pathname}`);

    // Set standard default header to return structured JSON payloads safely
    res.setHeader('Content-Type', 'application/json');

    // ----------------------------------------------------
    // ROUTE 1: GET /users -> Retrieve all user documents
    // ----------------------------------------------------
    // ROUTE 1: GET /users
if (pathname === '/users' && method === 'GET') {
    res.statusCode = 200;
    res.end(JSON.stringify(usersCollection));
}
// ROUTE 2: POST /users
else if (pathname === '/users' && method === 'POST') {
    let rawBodyChunks = [];
    
    // Receive data in chunks
    req.on('data', chunk => {
        rawBodyChunks.push(chunk);
    });

    // When the whole request body is received
    req.on('end', () => {
        try {
            // Buffer the chunks and convert to string
            const bodyString = Buffer.concat(rawBodyChunks).toString();
            // Parse the string into a JSON object
            const newUser = JSON.parse(bodyString);
            
            // Assign a new ID (simple logic)
            newUser.id = usersCollection.length ? usersCollection[usersCollection.length - 1].id + 1 : 1;
            
            // Add the new user to the array
            usersCollection.push(newUser);
            
            res.statusCode = 201; // Created
            res.end(JSON.stringify(newUser));
        } catch (error) {
            res.statusCode = 400; // Bad Request
            res.end(JSON.stringify({ error: "Invalid JSON format in request body." }));
        }
    });
}
// ROUTE 3: GET /greet (Change 'elif' to 'else if')
else if (pathname === '/greet' && method === 'GET') {
    const targetName = parsedUrl.searchParams.get('name') || 'Guest';
    res.statusCode = 200;
    res.end(JSON.stringify({ greeting: `Hello, ${targetName}! Welcome to my native Node.js server ecosystem.` }));
}
// FALLBACK
else {
    res.statusCode = 404;
    res.end(JSON.stringify({ error: "Endpoint path pattern unmapped." }));
}
});

// Start the server
server.listen(PORT, () => {
    console.log(`Server is listening on port ${PORT}...`);
});
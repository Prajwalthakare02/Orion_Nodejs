const express = require('express');
const app = express();

const PORT = 3000;

app.get('/', (req, res) => {
    res.send('Hello, Welcome to my first Node.js Application!');
});

app.listen(PORT, () => {
    console.log(`Server is running! Message: Hello, World from Node.js!`);
    console.log(`Access the app at http://localhost:${PORT}`);
});

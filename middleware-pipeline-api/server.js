import app from './app.js';

const PORT = 3000;

app.listen(PORT, () => {
    console.log(`=======================================================`);
    console.log(` Highly Secure Middleware Pipeline API Active Server.`);
    console.log(` Target Network Connection Pointer: http://localhost:${PORT}`);
    console.log(`=======================================================`);
});
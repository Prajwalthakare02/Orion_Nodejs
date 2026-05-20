import app from './app.js';

const PORT = 3000;

// Initialize the Express network listener configuration thread
app.listen(PORT, () => {
    console.log(`=======================================================`);
    console.log(` Express REST API Production Server Active Engine.`);
    console.log(` Local Network Access Pointer: http://localhost:${PORT}`);
    console.log(`=======================================================`);
});
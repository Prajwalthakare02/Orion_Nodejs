# Setting Up and Launching a Basic Node.js Application

## 1. Installing Node.js and npm
To start developing with Node.js, you first need to download the **LTS (Long Term Support)** version from the official Node.js website (nodejs.org). The LTS version is recommended over the "Current" version because it is more stable and reliable for production environments. Installing Node.js also automatically installs **npm (Node Package Manager)**, which is used to manage libraries and dependencies for your projects.

### Verifying the Installation
Once installed, you should verify that both Node.js and npm are installed correctly by running these commands in your terminal:
```bash
node -v   # Returns the installed Node version (e.g., v20.x.x)
npm -v    # Returns the installed npm version
```

## 2. The Importance of Node.js Version Management (NVM)
**NVM (Node Version Manager)** is a crucial tool for developers. Different projects often require different versions of Node.js. NVM allows you to install multiple versions of Node.js on a single machine and seamlessly switch between them using commands like `nvm install <version>` and `nvm use <version>`. This prevents compatibility issues and ensures your project runs on the exact environment it was built for.

## 3. Initializing a New Node.js Project
To start a new project, navigate to your desired directory in the terminal and run:
```bash
npm init -y
```
This command initializes a new project and creates a `package.json` file. The `-y` flag stands for "yes" and automatically accepts the default configuration, skipping the interactive setup questions.

### Purpose of package.json
The `package.json` file is the heart of any Node.js project. Its key fields include:
- **name & version**: Identifies your project and its current build version.
- **main**: The entry point of your application (usually `index.js` or `app.js`).
- **scripts**: Defines custom terminal commands (like the `"dev": "nodemon app.js"` script).
- **dependencies**: Lists the packages required for the app to run in production.
- **devDependencies**: Lists packages only needed during local development.

## 4. Setting up Essential Development Tools
For a modern Node.js web application, two essential tools are Express and Nodemon:
```bash
npm install express
npm install nodemon --save-dev
```
- **Express**: A minimal, fast web framework for Node.js. It drastically simplifies the process of creating web servers, handling HTTP routes (GET, POST, etc.), and managing server logic compared to using Node's raw built-in modules.
- **Nodemon**: A utility tool specifically for development. Normally, if you change your code, you have to manually stop and restart your Node server to see the changes. Nodemon solves this by watching your project files for changes and automatically restarting the server for you.

## 5. Creating and Executing a Basic Application
A basic Node application is typically built inside the main entry file (e.g., `app.js`):

```javascript
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
```

Because `package.json` is set up with `"dev": "nodemon app.js"`, you can execute the app by running:
```bash
npm run dev
```
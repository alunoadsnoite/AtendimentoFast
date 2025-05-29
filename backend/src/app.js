const express = require('express');
const setRoutes = require('./routes/index');
const app = express();

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Set up routes
setRoutes(app);

// Export the app for testing or further configuration
module.exports = app;
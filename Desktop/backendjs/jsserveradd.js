// Centralized error handler middleware
const errorHandler = (err, req, res, next) => {
  console.error(err.message);
  res.status(500).json({
    error: err.message || 'Internal Server Error',
  });
};

module.exports = errorHandler;

//Main Express App

const express = require('express');
const userRoutes = require('./routes/user.routes');
const errorHandler = require('./middleware/error.middleware');
const { sequelize, testConnection } = require('./config/db.config');

const app = express();

// Middleware for parsing request bodies
app.use(express.json());

// Connect and test the database connection
testConnection();

// Define routes
app.use('/api', userRoutes);

// Error handling middleware
app.use(errorHandler);

module.exports = app; 

//Starting the Server 

const app = require('./app');
const port = process.env.PORT || 3000;

// Start the server
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});


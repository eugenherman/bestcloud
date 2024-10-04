const express = require('express');
const UserController = require('../controllers/user.controller');
const router = express.Router();

// Define user routes
router.get('/users', UserController.getAllUsers);      // GET all users
router.post('/users', UserController.createUser);      // POST create a user
router.get('/users/:id', UserController.getUserById);  // GET user by ID

module.exports = router;

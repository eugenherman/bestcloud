const User = require('../models/user.model');

// Get all users
exports.getAllUsers = async () => {
  return await User.findAll();
};

// Create a new user
exports.createUser = async (username, email, password) => {
  const newUser = await User.create({ username, email, password });
  return newUser;
};

// Get user by ID
exports.getUserById = async (id) => {
  return await User.findByPk(id);
};

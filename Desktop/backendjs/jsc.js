const UserService = require('../services/user.service');

// Controller function to get all users
exports.getAllUsers = async (req, res, next) => {
  try {
    const users = await UserService.getAllUsers();
    res.status(200).json(users);
  } catch (error) {
    next(error);
  }
};

// Controller function to create a user
exports.createUser = async (req, res, next) => {
  try {
    const { username, email, password } = req.body;
    const newUser = await UserService.createUser(username, email, password);
    res.status(201).json(newUser);
  } catch (error) {
    next(error);
  }
};

// Controller function to get a user by ID
exports.getUserById = async (req, res, next) => {
  try {
    const user = await UserService.getUserById(req.params.id);
    if (!user) {
      return res.status(404).json({ message: 'User not found' });
    }
    res.status(200).json(user);
  } catch (error) {
    next(error);
  }
};

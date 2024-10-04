// server.js
const express = require('express');
const fs = require('fs');
const cors = require('cors');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();
const PORT = 5000;

app.use(cors());
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, '../public')));

// Simulating Database
const tasksFilePath = './tasks.json';

const readTasks = () => {
  const tasks = fs.readFileSync(tasksFilePath);
  return JSON.parse(tasks);
};

const writeTasks = (tasks) => {
  fs.writeFileSync(tasksFilePath, JSON.stringify(tasks, null, 2));
};

// API Endpoints

// GET all tasks
app.get('/api/tasks', (req, res) => {
  const tasks = readTasks();
  res.json(tasks);
});

// POST a new task
app.post('/api/tasks', (req, res) => {
  const tasks = readTasks();
  const newTask = {
    id: tasks.length ? tasks[tasks.length - 1].id + 1 : 1,
    title: req.body.title,
    description: req.body.description,
    completed: false,
  };
  tasks.push(newTask);
  writeTasks(tasks);
  res.json(newTask);
});

// PUT to update a task
app.put('/api/tasks/:id', (req, res) => {
  const tasks = readTasks();
  const taskIndex = tasks.findIndex((task) => task.id == req.params.id);

  if (taskIndex >= 0) {
    tasks[taskIndex] = { ...tasks[taskIndex], ...req.body };
    writeTasks(tasks);
    res.json(tasks[taskIndex]);
  } else {
    res.status(404).json({ message: 'Task not found' });
  }
});

// DELETE a task
app.delete('/api/tasks/:id', (req, res) => {
  let tasks = readTasks();
  tasks = tasks.filter((task) => task.id != req.params.id);
  writeTasks(tasks);
  res.json({ message: 'Task deleted' });
});

// Starting the server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});

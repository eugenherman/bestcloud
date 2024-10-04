// Select DOM elements
const taskForm = document.getElementById('task-form');
const taskInput = document.getElementById('task-input');
const taskList = document.getElementById('task-list');

// Array to store tasks
let tasks = [];

// Load tasks from local storage
document.addEventListener('DOMContentLoaded', loadTasks);

// Add task event listener
taskForm.addEventListener('submit', addTask);

// Function to load tasks from local storage
function loadTasks() {
    const storedTasks = JSON.parse(localStorage.getItem('tasks'));
    if (storedTasks) {
        tasks = storedTasks;
        tasks.forEach(task => displayTask(task));
    }
}

// Function to add a new task
function addTask(event) {
    event.preventDefault();
    const taskText = taskInput.value;

    const task = {
        id: Date.now(),
        text: taskText,
        completed: false,
    };

    tasks.push(task);
    displayTask(task);
    saveTasks();
    taskInput.value = '';
}

// Function to display a task
function displayTask(task) {
    const li = document.createElement('li');
    li.className = 'task-item';
    li.innerHTML = `
        <span>${task.text}</span>
        <button class="edit-button" onclick="editTask(${task.id})">Edit</button>
        <button class="delete-button" onclick="deleteTask(${task.id})">Delete</button>
    `;
    taskList.appendChild(li);
}

// Function to edit a task
function editTask(taskId) {
    const task = tasks.find(t => t.id === taskId);
    if (task) {
        const newText = prompt('Edit Task:', task.text);
        if (newText) {
            task.text = newText;
            saveTasks();
            refreshTaskList();
        }
    }
}

// Function to delete a task
function deleteTask(taskId) {
    tasks = tasks.filter(task => task.id !== taskId);
    saveTasks();
    refreshTaskList();
}

// Function to save tasks to local storage
function saveTasks() {
    localStorage.setItem('tasks', JSON.stringify(tasks));
}

// Function to refresh the task list
function refreshTaskList() {
    taskList.innerHTML = '';
    tasks.forEach(task => displayTask(task));
}

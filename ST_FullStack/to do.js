// Load tasks from local storage on page load
document.addEventListener("DOMContentLoaded", loadTasks);

function addTask() {
    const taskInput = document.getElementById("taskInput");
    const task = taskInput.value.trim();
    if (task === "") {
        alert("Please enter a task!");
        return;
    }

    createTaskElement(task);
    saveTask(task);
    taskInput.value = "";
}

// Create and append task list item with delete and checkbox
function createTaskElement(taskText, isCompleted = false) {
    const taskList = document.getElementById("taskList");

    const li = document.createElement("li");

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.checked = isCompleted;
    checkbox.addEventListener("change", function () {
        li.classList.toggle("completed");
        updateLocalStorage();
    });

    const span = document.createElement("span");
    span.textContent = taskText;

    const deleteBtn = document.createElement("button");
    deleteBtn.textContent = "Delete";
    deleteBtn.style.marginLeft = "10px";
    deleteBtn.style.backgroundColor = "#ff4d4d";
    deleteBtn.style.color = "white";
    deleteBtn.addEventListener("click", function () {
        li.remove();
        updateLocalStorage();
    });

    li.appendChild(checkbox);
    li.appendChild(span);
    li.appendChild(deleteBtn);

    if (isCompleted) li.classList.add("completed");

    taskList.appendChild(li);
}

// Save task to local storage
function saveTask(taskText) {
    const tasks = JSON.parse(localStorage.getItem("tasks")) || [];
    tasks.push({ text: taskText, completed: false });
    localStorage.setItem("tasks", JSON.stringify(tasks));
}

// Load tasks from local storage
function loadTasks() {
    const tasks = JSON.parse(localStorage.getItem("tasks")) || [];
    tasks.forEach(task => {
        createTaskElement(task.text, task.completed);
    });
}

// Update local storage after checkbox/delete
function updateLocalStorage() {
    const taskListItems = document.querySelectorAll("#taskList li");
    const updatedTasks = [];

    taskListItems.forEach(li => {
        const text = li.querySelector("span").textContent;
        const completed = li.querySelector("input").checked;
        updatedTasks.push({ text, completed });
    });

    localStorage.setItem("tasks", JSON.stringify(updatedTasks));
}

// Clear all tasks
function clearTasks() {
    document.getElementById("taskList").innerHTML = "";
    localStorage.removeItem("tasks");
}

const taskInput = document.getElementById('taskInput');
const addButton = document.getElementById('addButton');
const taskList = document.getElementById('taskList');

addButton.addEventListener('click', (e) => {
    e.preventDefault();
    const taskText = taskInput.value;
    if (taskText !== '') {
        const newTask = document.createElement('li');
        newTask.innerText = taskText;
        taskList.appendChild(newTask);
        taskInput.value = '';
        newTask.addEventListener('click', () => {
            newTask.classList.toggle('completed');
        });
    }
});

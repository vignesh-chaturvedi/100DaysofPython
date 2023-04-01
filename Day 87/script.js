const cafeList = document.getElementById('cafe-list');
const addCafeForm = document.getElementById('add-cafe-form');

function fetchCafes() {
  fetch('/cafes')
    .then(response => response.json())
    .then(cafes => {
      cafes.forEach(cafe => {
        const li = document.createElement('li');
        li.textContent = `${cafe.name} - ${cafe.location}`;
        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Delete';
        deleteButton.onclick = () => deleteCafe(cafe.id);
        li.appendChild(deleteButton);
        cafeList.appendChild(li);
      });
    });
}

function addCafe(name, location) {
  fetch('/cafes', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ name, location })
  })
    .then(response => response.json())
    .then(cafe => {
      const li = document.createElement('li');
      li.textContent = `${cafe.name} - ${cafe.location}`;
      const deleteButton = document.createElement('button');
      deleteButton.textContent = 'Delete';
      deleteButton.onclick = () => deleteCafe(cafe.id);
      li.appendChild(deleteButton);
      cafeList.appendChild(li);
    });
}

function deleteCafe(cafeId) {
  fetch(`/cafes/${cafeId}`, {
    method: 'DELETE'
  })
    .then(response => response.json())
    .then(() => {
      const li = document.querySelector(`[data-id="${cafeId}"]`);
      cafeList.removeChild(li);
    });
}

addCafeForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const name = document.getElementById('name').value;
  const location = document.getElementById('location').value;
  addCafe(name, location);
  addCafeForm.reset();
});

fetchCafes();

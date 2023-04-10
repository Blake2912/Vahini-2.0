const startSelect = document.querySelector('#start');
const endSelect = document.querySelector('#end');

// Fetch all nodes and add them as options to the start dropdown menu
fetch('/fetch-all-nodes')
  .then((response) => response.json())
  .then((nodes) => {
    nodes.forEach((node) => {
      const option = document.createElement('option');
      option.innerText = node;
      option.value = node;
      startSelect.appendChild(option);
    });
  });

// When a start node is selected, fetch the neighboring nodes and add them as options to the end dropdown menu
startSelect.addEventListener('change', (event) => {
    const current_node = event.target.value;
    console.log(current_node);
  fetch('/fetch-neighbours', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ current_node: current_node }),
  })
    .then((response) => response.json())
      .then((neighbors) => {
        console.log(neighbors);
      endSelect.innerHTML = '<option value="">Select a node</option>'; // Clear the current options in the end dropdown menu
      neighbors.forEach((neighbor) => {
        const option = document.createElement('option');
        option.innerText = neighbor;
        option.value = neighbor;
        endSelect.appendChild(option);
      });
    });
});

const startSelect = document.querySelector("#start");
const endSelect = document.querySelector("#end");

// Fetch all nodes and add them as options to the start dropdown menu
fetch("/fetch-all-nodes")
  .then((response) => response.json())
  .then((nodes) => {
    nodes.forEach((node) => {
      const option = document.createElement("option");
      option.innerText = node;
      option.value = node;
      startSelect.appendChild(option);
    });
  });

// When a start node is selected, fetch the neighboring nodes and add them as options to the end dropdown menu
startSelect.addEventListener("change", (event) => {
  const current_node = event.target.value;
  console.log(current_node);
  fetch("/fetch-neighbours", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ current_node: current_node }),
  })
    .then((response) => response.json())
    .then((neighbors) => {
      console.log(neighbors);
      endSelect.innerHTML = '<option value="">Select a node</option>'; // Clear the current options in the end dropdown menu
      neighbors.forEach((neighbor) => {
        const option = document.createElement("option");
        option.innerText = neighbor;
        option.value = neighbor;
        endSelect.appendChild(option);
      });
    });
});

const addTreeButton = document.getElementById("add-tree-button");
const saveButton = document.getElementById("save-button");

addTreeButton.addEventListener("click", () => {
  const selectedStart = startSelect.value;
  const selectedEnd = endSelect.value;

  fetch("/add_tree", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      start_node: selectedStart,
      end_node: selectedEnd,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      // Do something with the response data if needed
    })
    .catch((error) => console.error(error));
});

saveButton.addEventListener("click", () => {
  fetch("/save")
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      // Do something with the response data if needed
    })
    .catch((error) => console.error(error));
});

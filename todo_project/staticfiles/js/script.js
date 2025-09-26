// Select all draggable elements
const dragItems = document.querySelectorAll('.dragElement');
const dropZones = document.querySelectorAll('.dropZone');

let currentDraggedItem = null;

dragItems.forEach(item => {
  item.setAttribute('draggable', true);

  item.addEventListener('dragstart', () => {
    currentDraggedItem = item;
    item.classList.add('beingDragged');
  });

  item.addEventListener('dragend', () => {
    item.classList.remove('beingDragged');
    // currentDraggedItem = null;
  });
});

dropZones.forEach(dropZone => {
  dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropZone.classList.add('hoverOver');
  });

  dropZone.addEventListener('dragleave', () => {
    dropZone.classList.remove('hoverOver');
  });

  dropZone.addEventListener('drop', () => {
    let proceed = true
    let dropZoneChildren = dropZone.children;

    dropZone.classList.remove('hoverOver');
    if (Array.from(dropZoneChildren).forEach(child => {
      if (child == currentDraggedItem) proceed = false
    }));

    if (currentDraggedItem && proceed == true) {
      dropZone.appendChild(currentDraggedItem);
      if (dropZone.getAttribute("isdone") == "true"){
        completeTodo("completetodo",currentDraggedItem.getAttribute("todoid"));
      } else {
        completeTodo("uncompletetodo",currentDraggedItem.getAttribute("todoid"));
      }
    }
  });
});

function completeTodo(functionCall, itemId) {
  fetch(`/${functionCall}/${itemId}`, {
    method: 'POST',
    headers: {
      'X-CSRFToken': getCSRFToken()
    }
  })
  .then(response => response.json())
  .then(data => {
    console.log(data);
    if (data.status === 'success') {
      // Update UI, e.g., mark item visually as completed
    }
  })
  .catch(error => {
    console.error('Error:', error);
  });
}

function getCSRFToken() {
  const match = document.cookie.match(/csrftoken=([^;]+)/);
  return match ? match[1] : '';
}
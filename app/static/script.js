// Allow drag-and-drop
function allowDrop(event) {
    event.preventDefault();
}

// Set up the drag event (when the user starts dragging a tag)
function drag(event) {
    event.dataTransfer.setData("text", event.target.id);
}

// Drop event (when the user drops the tag into a new column)
function drop(event) {
    event.preventDefault();
    const data = event.dataTransfer.getData("text");
    const draggedElement = document.getElementById(data);
    // Append the dragged element to the target list
    if (event.target.tagName === "LI" || event.target.tagName === "UL") {
        event.target.appendChild(draggedElement);
    }
}

// Add tag on Enter key press in Include/Exclude columns
function addTag(event, column) {
    if (event.key === "Enter") {
        event.preventDefault();
        const input = column === 'include' ? document.getElementById("includeTagInput") : document.getElementById("excludeTagInput");
        const tagValue = input.value.trim();

        if (tagValue) {
            const newTag = document.createElement("li");
            newTag.textContent = tagValue;
            newTag.setAttribute("draggable", "true");
            newTag.setAttribute("id", `tag-${new Date().getTime()}`);
            newTag.setAttribute("ondragstart", "drag(event)");

            // Append the new tag to the respective column
            const list = column === 'include' ? document.getElementById("includeList") : document.getElementById("excludeList");
            list.appendChild(newTag);

            input.value = "";  // Clear the input field after adding the tag
        }
    }
}

// Prepare the tags before submitting the form
function prepareTags() {
    const includeList = document.querySelectorAll("#includeList li");
    const excludeList = document.querySelectorAll("#excludeList li");

    const includeTags = Array.from(includeList).map(tag => tag.textContent.trim());
    const excludeTags = Array.from(excludeList).map(tag => tag.textContent.trim());

    document.getElementById("includeTagsInput").value = JSON.stringify(includeTags);
    document.getElementById("excludeTagsInput").value = JSON.stringify(excludeTags);
}

// Function to add a new username field
function addUsernameField() {
    const container = document.getElementById("usernameContainer");

    // Create a new username group
    const newGroup = document.createElement("div");
    newGroup.classList.add("username-group");

    // Create the input field
    const newInput = document.createElement("input");
    newInput.type = "text";
    newInput.name = "usernames[]";
    newInput.placeholder = "Enter username";
    newInput.required = true;

    // Create the remove button
    const removeButton = document.createElement("button");
    removeButton.type = "button";
    removeButton.textContent = "-";
    removeButton.classList.add("remove-username");
    removeButton.onclick = function () {
        container.removeChild(newGroup);
    };

    // Add input and button to the new group
    newGroup.appendChild(newInput);
    newGroup.appendChild(removeButton);

    // Append the group to the container
    container.appendChild(newGroup);
}

const addButton = document.querySelector(".add");

addButton.addEventListener("click", () => {
    let deleteButton = document.createElement("button");
    let image = document.createElement("img");
    let container = document.createElement("div");
    let inputLink = document.createElement("input");

    inputLink.classList.add("input-link")
    inputLink.placeholder = "Введите ссылку на необходимый материал...";
    container.classList.add("input-link-container");
    container.appendChild(inputLink);
    image.src = document.querySelector("meta[name='trash-link']").getAttribute("content");
    deleteButton.appendChild(image);
    deleteButton.type = "button";
    image.classList.add("plus");
    deleteButton.classList.add("add");

    deleteButton.addEventListener("click", () => {
        deleteButton.parentNode.parentNode.removeChild(deleteButton.parentNode);
    })

    addButton.parentNode.appendChild(deleteButton);
    addButton.parentNode.parentNode.appendChild(container);
    container.appendChild(addButton);
})
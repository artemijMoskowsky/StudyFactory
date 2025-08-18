const fileInput = document.querySelector("#input-files");
const fileBuffer = document.querySelector("#file-buffer");
const filePlacer = document.querySelector("#file-placer");
const fileLink = document.querySelector("meta[name='file-link']").content;

function loadElements(){
    while (filePlacer.children.length) {
        filePlacer.removeChild(filePlacer.firstChild);
    }
    let dataTransfer = new DataTransfer;
    for (let file of fileBuffer.files){
        dataTransfer.items.add(file);
    }
    for (let file of fileInput.files){
        dataTransfer.items.add(file);
    }
    // console.log(fileBuffer.files, fileInput.files, dataTransfer.files)
    fileBuffer.files = dataTransfer.files;
    let clearList = new DataTransfer;;
    fileInput.files = clearList.files;
    console.log(fileBuffer.files)

    // let fileReader = new FileReader;
    // fileReader.onload = function () {
    //     let newFile = document.createElement("embed");
    //     newFile.width = "50px";
    //     newFile.height = "50px";
    //     newFile.src = fileReader.result;
    //     filePlacer.appendChild(newFile);
    // }
    // for (let file of fileBuffer.files){
    //     fileReader.readAsDataURL(file);
    // }
    for (let file of fileBuffer.files){
        let fileBase = document.createElement("div");
        fileBase.classList.add("file-base");
        let fileImg = document.createElement("img");
        if (file.type.startsWith("image")){
           let fr = new FileReader;
           fr.onload = function () {
            fileImg.src = fr.result;
           }
           fr.readAsDataURL(file);
        } else if (file.type.startsWith("video")){
           
        } else {
            fileImg.src = fileLink;
        }
        fileImg.classList.add("file-img")
        let fileName = document.createElement("p");
        fileName.textContent = `${file.name}`;
        fileName.classList.add("file-name");
        let fileSize = document.createElement("p");
        fileSize.classList.add("file-size");
        fileSize.textContent = `${Math.round(file.size/1024)} KB`;
        fileBase.appendChild(fileImg);
        fileBase.appendChild(fileName);
        fileBase.appendChild(fileSize);
        filePlacer.appendChild(fileBase);
    }
}


window.addEventListener("pageshow", (event)=>{
    loadElements();
    fileInput.addEventListener("input", loadElements);
})

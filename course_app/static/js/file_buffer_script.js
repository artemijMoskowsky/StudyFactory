const fileInput = document.querySelector("#input-files");
const fileBuffer = document.querySelector("#file-buffer");
const filePlacer = document.querySelector("#file-placer");

fileInput.addEventListener("input", ()=>{
    for (let child of filePlacer.children){
        filePlacer.removeChild(child);
    }
    let dataTransfer = new DataTransfer;
    for (let file of fileBuffer.files){
        dataTransfer.items.add(file);
    }
    for (let file of fileInput.files){
        dataTransfer.items.add(file);
    }
    
    fileBuffer.files = dataTransfer.files;

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
        let fileBase = document.createElement("div")
        let fileImg = document.createElement("img");
        let fileName = document.createElement("p");
        fileName.textContent = `${file.name} ${Math.round(file.size/1024)} KB`
        fileBase.appendChild(fileImg);
        fileBase.appendChild(fileName);
        filePlacer.appendChild(fileBase);
    }
})
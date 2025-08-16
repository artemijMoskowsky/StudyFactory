const courseContainer = document.querySelector("#course-container");

function getCourses() {
    let xhr = new XMLHttpRequest();
    xhr.open("GET", "/get_all_user_courses");
    xhr.onload = function () {
        if (this.status == 200 && this.readyState == 4) {
            console.log(this.response);
            let data = JSON.parse(this.response);
            console.log(data, typeof data);
            for (let course of data) {
                appendCourse(course.color, course.description, course.name, course.owner);
            }
        }
    };
    xhr.send();
}

getCourses();

function appendCourse(color, description, name, owner) {
    let course = document.createElement("div");
    course.classList.add("course");
    courseContainer.appendChild(course);

    let courseName = document.createElement("div");
    courseName.classList.add("course-name");
    // Вставка
    courseName.style.backgroundColor = color;
    courseName.textContent = name;
    // Вставка
    course.appendChild(courseName);

    let courseAccount = document.createElement("div");
    courseAccount.classList.add("course-account");
    let accountImg = document.createElement("img");
    accountImg.src = "/static_base/img/Account.svg";
    let accountName = document.createElement("span");
    accountName.classList.add("course-creator");
    // Вставка
    accountName.textContent = owner;
    // Вставка
    courseAccount.appendChild(accountImg);
    courseAccount.appendChild(accountName);
    course.appendChild(courseAccount);

    let courseDescription = document.createElement("div");
    courseDescription.classList.add("course-description");
    // Вставка
    courseDescription.textContent = description;
    // Вставка
    course.appendChild(courseDescription);

    let courseButtons = document.createElement("div");
    courseButtons.classList.add("course-buttons");

    let quitButton = document.createElement("button");
    quitButton.classList.add("quit-course-button");
    let quitImg = document.createElement("img");
    quitImg.src = "/core_static/img/Quit.svg";
    quitButton.append(quitImg, "Выйти");

    let reportButton = document.createElement("button");
    reportButton.classList.add("report-course-button");
    let reportImg = document.createElement("img");
    reportImg.src = "/core_static/img/Report.svg";
    reportButton.append(reportImg, "Пожаловаться");

    courseButtons.appendChild(quitButton);
    courseButtons.appendChild(reportButton);
    course.appendChild(courseButtons);
}
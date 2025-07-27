let xhr = new XMLHttpRequest();

xhr.open("GET", "/get_all_user_courses");

xhr.onload = function () {
    if(this.status == 200 && this.readyState == 4){
        console.log(this.response)
    }
}

xhr.send();
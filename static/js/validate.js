function validate() {
    if (document.getElementById("usernameField").value == "" && document.getElementById("usernameField").value == "") {
         alert("all fields are empty");
         return false;
    } else {
        return true;
    }
}
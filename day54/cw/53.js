function formSubmit(e){
    e.preventDefault();

    let nameInput = document.getElementById("name-input");
    let surnameInput = document. getElementById("surname-input");
    let passwordInput = document.getElementById("password-input");

    let name = nameInput.value;
    let surname = surnameInput.value;
    let password = passwordInput.value;

    console.log(name);
    console.log(surname);
    console.log(password);


    nameInput.value = "";
    surnameInput.value = "";
    passwordInput.value = "";

}
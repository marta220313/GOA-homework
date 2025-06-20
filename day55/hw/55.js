function formSubmit(e){
    e.preventDefault();

    let nameInput = document.getElementById("name-input");
    let surnameInput = document. getElementById("surname-input");
    let passwordInput = document.getElementById("password-input");

    let name = nameInput.value;
    let surname = surnameInput.value;
    let password = passwordInput.value;

    console.log(number);
    console.log(say);


    nameInput.value = "";
    surnameInput.value = "";
    passwordInput.value = "";

}
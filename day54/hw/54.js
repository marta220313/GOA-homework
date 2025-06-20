const hobby = prompt("What is your favorite hobby?");
    alert("Your favorite hobby is: " + hobby);

    
    const firstName = prompt("Enter your first name:");
    const lastName = prompt("Enter your last name:");
    const fullName = firstName + " " + lastName;
    alert("Your full name is: " + fullName);

    
    const userMessage = prompt("Enter a message to display on the page:");
    document.getElementById("message").textContent = userMessage;

    
    const emoji = prompt("What is your favorite emoji?");
    alert("Thanks! Your favorite emoji is: " + emoji);

   
    const newTitle = prompt("Enter a word to set as the page title:");
    document.title = newTitle;
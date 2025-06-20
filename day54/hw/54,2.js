function showAlert() {
      const value = document.getElementById("textInput").value;
      alert(value);
    }

    
    document.getElementById("colorForm").addEventListener("submit", function(e) {
      e.preventDefault(); 
      const color = document.getElementById("colorInput").value;
      document.body.style.backgroundColor = color;
    });

    
    function showFullName() {
      const first = document.getElementById("firstName").value;
      const last = document.getElementById("lastName").value;
      document.getElementById("fullNameDisplay").textContent = `${first} ${last}`;
    }
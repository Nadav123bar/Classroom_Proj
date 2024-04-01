function checkValues() {
    var userName = document.getElementById("userName").value;
    var password = document.getElementById("password").value;

    var url = "/login";
    var data = {
        user_name: userName,
        pass: password
    };

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams(data),
    })
    .then(response => response.json())
    .then(result => {
        // Handle the result as needed
        console.log(result);

        if (result.success) {
            // Redirect to the specified URL on successful login
            window.location.href = result.redirect;
        } 
        else {
            // Handle invalid credentials
            alert("Invalid credentials. Go away hacker!");
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

34.58408
31.6987911
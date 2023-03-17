let rootDiv = document.getElementById('root');
let btn = document.getElementById('btn');
let btn2 = document.getElementById('btn2');
let fName = document.getElementById('inputFirstName');
let lName = document.getElementById('inputLastName');
let IEmail = document.getElementById('inputEmail');
let pswd = document.getElementById('inputPassword');
let form = document.getElementById('form');

btn.addEventListener('click', () => {
    console.log("btn clicked");

    let firstName = fName.value;
    let lastName = lName.value;
    let email = IEmail.value;
    let password = pswd.value;

    firstName = firstName.trim();
    lastName = lastName.trim();
    email = email.trim();
    password = password.trim();

    let data = {
        'first_name' : firstName,
        'last_name' : lastName,
        'email' : email,
        'password' : password
    }
    
    if (firstName == "" || lastName =="" || email=="" || password == "" ) {
        alert("koi bhi field empty nhi honi chaiye..")
    }
    else {
        let rqst = new XMLHttpRequest();
        // rqst.open('POST', 'http://127.0.0.1:8000/testing/');
        rqst.open('POST', 'http://127.0.0.1:8000/register-user/');
        rqst.setRequestHeader('Content-Type', 'application/json');
        rqst.send(JSON.stringify( data ));

        rqst.addEventListener('load', () => {
            console.log(rqst.responseText);

            let data = JSON.parse(rqst.responseText)
            // let p1 = document.createElement('p');
            // p1.innerText = `Old data: ${data.oldData}`;

            // let p2 = document.createElement('p');
            // p2.innerText = `New Data: ${data.newData}`;
            
            // rootDiv.appendChild(p1);
            // rootDiv.appendChild(p2);
            
            let p3 = document.createElement('p');
            p3.innerText = `Response Msg: ${data.msg}`; // data[msg]
            rootDiv.appendChild(p3);

            form.reset();
        })
    }
})


btn2.addEventListener('click', () => {
    console.log('btn 2 clicked');

    // fetch('http://127.0.0.1:8000/testing/', {
    //     headers: {
    //         'Access-Control-Allow-Origin': '*',
    //         'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
    //         'Access-Control-Allow-Headers': 'Content-Type, Authorization, X-Requested-With'
    //     }
    // })
    // .then(response => {
    //     // Handle the response
    //     console.log("here, handle the response")
    //     console.log(response.json(),"<<<")

    // })
    // .catch(err => {
    //     // Handle any errors
    //     console.log("error")
    // });
    /*
        let data = {
            data: "sending data"
        }
    
        fetch("http://127.0.0.1:8000/testing/", {
            method: "POST", // or 'PUT'
            headers: {
                // "Content-Type": "application/json",
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type, Authorization, X-Requested-With'
            },
            body: JSON.stringify(data),
        })
            .then((response) => response.json())
            .then((data) => {
                console.log("Success:", data);
            })
            .catch((error) => {
                console.error("Error:", error);
            })
            */
});


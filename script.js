rootDiv = document.getElementById('root');
btn = document.getElementById('btn');

btn.addEventListener('click',()=>{
    console.log("btn clicked");

    let rqst = new XMLHttpRequest();
    rqst.open('POST','/login');
    rqst.setRequestHeader('Content-Type','application/json');
    rqst.send(JSON.stringify({data:"send test data"}));
    rqst.addEventListener('load',()=>{
        console.log(rqst.responseText);

        // let p1 = document.createElement('p'); 
        // p1.innerHTML = 
        // let p2 = document.createElement('p'); 
    })
})



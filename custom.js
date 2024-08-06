function user_contacts(){
   var name = document.getElementById('name').value;
   var email = document.getElementById('email').value;
   var message = document.getElementById('message').value;
   fetch('../contacts', {
   method: 'POST',
   headers:{'Content-Type': 'application/json'},
   body:JSON.stringify({name: name, email: email, message:message })
   })
   .then(response => response.json())
   .then(data => {
       if (data == 1){
           alert("You message has been successfully received.");
       }else{
           alert("An error occurred. Try again later.");
       }
   })
   .catch(error => console.error("An error occurred: ", error));
}

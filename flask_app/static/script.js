// this is for the flash messages
var users = document.getElementById('users')
var myForm = document.getElementById('myform');
  myForm.onsubmit = function(e){
    e.preventDefault();
    console.log(e)
    console.log(users)
    var form = new FormData(myForm);
    fetch("http://localhost:5000/register", { method : 'POST', body : form })
      .then( response => response.json() )
      .then( data => { users.innerHTML += 
        // this should display the flash meesage for user registration.
        `{% with messages = get_flashed_messages(category_filter=['register']) %}
          {% if messages %}
          <div class="alert alert-danger" role="alert">
            <strong>Incorrect Account Registration</strong>
              {% for message in messages %}
              <p>{{ message }}</p>
              {% endfor %}
          </div>
          {% endif %}
        {% endwith %}`
      } )
      .catch((err) => console.log(err) )
    console.log(users)
  }
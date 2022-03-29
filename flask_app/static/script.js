// this is for the flash messages

// var users = document.getElementById("users");
// var myForm = document.getElementById("myform");
// myForm.onsubmit = function (e) {
//     e.preventDefault();
//     console.log(e);
//     console.log(users);
//     var form = new FormData(myForm);
//     fetch("http://localhost:5000/coach/register", {
//         method: "POST",
//         body: form,
//     })
//         .then((response) => response.json())
//         .then((data) => {
//             users.innerHTML +=
//                 // this should display the flash meesage for user registration.
//                 `{% with messages = get_flashed_messages(category_filter=['register']) %}
//           {% if messages %}
//           <div class="alert alert-danger" role="alert">
//             <strong>Incorrect Account Registration</strong>
//               {% for message in messages %}
//               <p>{{ message }}</p>
//               {% endfor %}
//           </div>
//           {% endif %}
//         {% endwith %}`;
//         })
//         .catch((err) => console.log(err));
//     console.log(users);
// };

// var users = document.getElementById("users");
// var myForm = document.getElementById("myform");
// myForm.onsubmit = function (e) {
//     e.preventDefault();
//     var form = new FormData(myForm);
//     fetch("http://localhost:5000/register", { method: "POST", body: form })
//         .then((response) => response.json())
//         .then((data) => {
//             users.innerHTML +=
//                 // this should display the flash meesage for user registration.
//                 `{% with messages = get_flashed_messages(category_filter=['login']) %}
//           {% if messages %}
//           <div class="alert alert-danger" role="alert">
//             <strong>Incorrect Account Registration</strong>
//               {% for message in messages %}
//               <p>{{ message }}</p>
//               {% endfor %}
//           </div>
//           {% endif %}
//         {% endwith %}`;
//         })
//         .catch((err) => console.log(err));
//     console.log(users);
// };

// var users = document.getElementById("users");
// var myForm = document.getElementById("myform");
// myForm.onsubmit = function (e) {
//     e.preventDefault();
//     var form = new FormData(myForm);
//     fetch("http://localhost:5000/athlete/login", { method: "POST", body: form })
//         .then((response) => response.json())
//         .then((data) => {
//             users.innerHTML +=
//                 // this should display the flash meesage for user registration.
//                 `{% with messages = get_flashed_messages(category_filter=['login']) %}
//           {% if messages %}
//           <div class="alert alert-danger" role="alert">
//             <strong>Incorrect Account Registration</strong>
//               {% for message in messages %}
//               <p>{{ message }}</p>
//               {% endfor %}
//           </div>
//           {% endif %}
//         {% endwith %}`;
//         })
//         .catch((err) => console.log(err));
//     console.log(users);
// };

let checkbox = document.getElementById("relay_check");
let athleteSelect = document.getElementById("athlete_select");
let isRelay = document.getElementById("isRelay");
checkbox.addEventListener("change", function () {
    if (this.checked) {
        fetch("http://127.0.0.1:5000/athletes/get_all")
            .then((response) => response.json())
            .then((data) => {
                console.log(
                    data.athletes.length,
                    ">>>",
                    data,
                    ">>>>",
                    data.athletes[0].last_name
                );
                isRelay.value = "1";
                let athletes = "";
                for (i = 0; i < data.athletes.length; i++) {
                    athletes += `
                    <option value="${data.athletes[i].id}">
                    ${data.athletes[i].last_name}, ${data.athletes[i].first_name}
                    </option>`;
                }
                for (j = 2; j < 5; j++) {
                    console.log(athletes);
                    athleteSelect.innerHTML += `<select name='athlete_id${j}'>${athletes}</select>`;
                }

                // athletes;
            });
        console.log("Checkbox is checked..");
        //ajax call for athletes_by_coach_id
        //use loops to populate drop down
        //factor variables into html code
    } else {
        athleteSelect.innerHTML = "";
        console.log("Checkbox is not checked..");
        isRelay.value = "0";
    }
});

search_form.onsubmit = function (e) {
    e.preventDefault();
    // console.log("made it here");
    let form = new FormData(search_form);

    fetch("http://127.0.0.1:5000/search/results", {
        method: "POST",
        body: form,
    })
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            console.log(typeof data);
            console.log(data.length);
            searchResults = document.getElementById("search_results");
            if (typeof data == "string") {
                searchResults.innerHTML = "<p>No results found</p>";
            } else {
                searchResults.innerHTML = `<table class="table table-bordered table_marg">
      <thead>
      <tr>
        <th scope="col">Event</th>
        <th scope="col">Athlete</th>
        <th scope="col">time</th> 
        <th scope="col">Date</th>
      </tr>
      </thead>
      <tbody id="results">
      </tbody>
      </table>`;
                results = document.getElementById("results");
                for (i = 0; i < data.length; i++) {
                    results.innerHTML += `<tr>
      <td>${data[i].name}</td>
      <td>${data[i].first_name} ${data[i].last_name}</td>
      <td>${data[i].time}</td>
      <td>${data[i].date}</td>
    </tr>`;
                }
            }
        });
};

searchForTimes = document.getElementById("searchForTimes");
searchForTimes.addEventListener("click", function () {
    console.log("hi");
    searchTools.innerHTML += `<form action="/search/results" method="post" id="search_form">
  <input type="hidden" name="coach_id" id="" value="{{session.coach_id}}" />
  <hr class="mb-4" />
  <label for="relay">relay:</label>
  <input type="checkbox" name="relay" value="Relay" id="relay_check" />

  <select name="athlete_id" id="">
      {% if athletes %}
      <option value="" selected></option>
      {% for athlete in athletes %}
      <option value="{{athlete.id}}">
          {{athlete.last_name}}, {{athlete.first_name}}
      </option>
      {% endfor %} {% else %}
      <p>
          There are no Athletes to add times to. Go to add athletes to update
          roster.
      </p>
      {% endif %}
  </select>
  <label
      >Event:
      <select name="event_id" id="">
          <option value="" selected></option>
          {% for event in events %}
          <option value="{{event.id}}">{{event.name}}</option>
          {% endfor %}
      </select>
  </label>
  <!-- change date to dropdown? -->
  <label
      >date:
      <input type="date" name="date" />
  </label>
  <input type="submit" name="" id="" value="Find Times" />
</form>`;
});

let postBox = document.getElementById("Textarea-post");
addTime.addEventListener("click", function () {
    searchResults = document.getElementById("search_results");
    postBox.innerText += searchResults.innerText;
});

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

// e.preventDefault();
// console.log("made it here");
// let form = new FormData(search_events_form);

// fetch("http://127.0.0.1:5000/search_results", {
//     method: "POST",
//     body: form,
// })
//     .then((response) => response.json())
//     .then((data) => {
//         console.log(data);
//         console.log(typeof data);
//         console.log(data.length);
//         resultsTable = document.getElementById("result-table");
//         resultsTable.innerHTML = `<table class="table table-bordered table_marg">
// <thead>
// <tr>
//   <th scope="col">Event</th>
//   <th scope="col">When</th>
//   <th scope="col">Location</th>
// </tr>
// </thead>
// <tbody id=results>
// </tbody>
// </table>`;
//         results = document.getElementById("results");
//         for (i = 0; i < data.length; i++) {
//             results.innerHTML += `<tr>
//       <td><a href= "/event_details/${data[i].id}">${data[i].event_name}</a></td>
//       <td>${data[i].date}</td>
//       <td>${data[i].location}, ${data[i].city}, ${data[i].state}</td>

//     </tr>`;
//         }
//     });
// };

// table class="table table-bordered table_marg">
//   <thead>
//     <tr>
//       <th scope="col">Event</th>
//       <th scope="col">When</th>
//       <th scope="col">Location</th>
//     </tr>
//   </thead>
//   <tbody id="results"></tbody>
// </table> -->

//below is for reference

// search_by_user_loc.onsubmit = function (e) {
// e.preventDefault();
// console.log("user LOCation made it here");
// let form = new FormData(search_by_user_loc);

// fetch("http://127.0.0.1:5000/search_by_user_loc", {
//     method: "POST",
//     body: form,
// })
//     .then((response) => response.json())
//     .then((data) => {
//         console.log(data);
//         console.log(typeof data);
//         console.log(data.length);
//         resultsTable = document.getElementById("result-table");
//         resultsTable.innerHTML = `<table class="table table-bordered table_marg">
// <thead>
// <tr>
//   <th scope="col">Event</th>
//   <th scope="col">When</th>
//   <th scope="col">Location</th>
// </tr>
// </thead>
// <tbody id=results>
// </tbody>
// </table>`;
//         results = document.getElementById("results");
//         for (i = 0; i < data.length; i++) {
//             results.innerHTML += `<tr>
//       <td><a href= "/event_details/${data[i].id}">${data[i].event_name}</a></td>
//       <td>${data[i].date}</td>
//       <td>${data[i].location}, ${data[i].city}, ${data[i].state}</td>

//     </tr>`;
//         }
//     });
// };

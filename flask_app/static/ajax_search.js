search_events_form.onsubmit = function (e) {
    e.preventDefault();
    console.log("made it here");
    let form = new FormData(search_events_form);

    fetch("http://127.0.0.1:5000/search_results", {
        method: "POST",
        body: form,
    })
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            console.log(typeof data);
            console.log(data.length);
            resultsTable = document.getElementById("result-table");
            resultsTable.innerHTML = `<table class="table table-bordered table_marg">
  <thead>
    <tr>
      <th scope="col">Event</th>
      <th scope="col">When</th>
      <th scope="col">Location</th>
    </tr>
  </thead>
  <tbody id=results>
  </tbody>
  </table>`;
            results = document.getElementById("results");
            for (i = 0; i < data.length; i++) {
                results.innerHTML += `<tr>
          <td><a href= "/event_details/${data[i].id}">${data[i].event_name}</a></td>
          <td>${data[i].date}</td>
          <td>${data[i].location}, ${data[i].city}, ${data[i].state}</td>

        </tr>`;
            }
        });
};

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

search_by_user_loc.onsubmit = function (e) {
    e.preventDefault();
    console.log("user LOCation made it here");
    let form = new FormData(search_by_user_loc);

    fetch("http://127.0.0.1:5000/search_by_user_loc", {
        method: "POST",
        body: form,
    })
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            console.log(typeof data);
            console.log(data.length);
            resultsTable = document.getElementById("result-table");
            resultsTable.innerHTML = `<table class="table table-bordered table_marg">
  <thead>
    <tr>
      <th scope="col">Event</th>
      <th scope="col">When</th>
      <th scope="col">Location</th>
    </tr>
  </thead>
  <tbody id=results>
  </tbody>
  </table>`;
            results = document.getElementById("results");
            for (i = 0; i < data.length; i++) {
                results.innerHTML += `<tr>
          <td><a href= "/event_details/${data[i].id}">${data[i].event_name}</a></td>
          <td>${data[i].date}</td>
          <td>${data[i].location}, ${data[i].city}, ${data[i].state}</td>

        </tr>`;
            }
        });
};

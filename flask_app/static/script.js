let autocomplete;
function initAutocomplete() {
    autocomplete = new google.maps.places.Autocomplete(
        document.getElementById("autocomplete"),
        {
            //types: ["establishments"],
            componentRestrictions: { country: "us" },
            fields: ["place_id", "geometry", "name"],
        }
    );
}

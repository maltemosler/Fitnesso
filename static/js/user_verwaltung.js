
function delete_user(user_id) {
    // send ajax request to webserver to delete user
    sendAJAX("delete_user", {
            "user_id": user_id,
        },
        function () {
            // reload website on success to refresh the lists
            location.reload();
        }, function (status_code, message) {
            // this should not occur but in case we catch it
            console.log(status_code);
            console.log(message);
        });

}

function user_filter() {
    // STRG + F search but just as button ;=)
    const result = find(($('#search-user').val()));
    if (result) {
        // hide error when search was  successfully
        $('#user-verwaltung-search-error').hide();
    } else {
        // show error when search was not successfully
        $('#user-verwaltung-search-error').show();
    }
}
function delete_user(user_id) {

    sendAJAX("delete_user", {
            "user_id": user_id,
        },
        function () {
            location.reload();
        }, function (status_code, message) {
            console.log(status_code);
            console.log(message);

        });

}

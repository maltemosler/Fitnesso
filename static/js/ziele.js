function hauptziel_erstellen() {
    const ziel = $("#home-hauptziel").val();

    sendAJAX("hauptziel_erstellen", {
            "ziel": ziel,
        },
        function () {
            location.reload();
        }, function (status_code, message) {
            console.log(status_code);
            console.log(message);
        });
}
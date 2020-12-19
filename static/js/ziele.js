function hauptziel_erstellen() {
    const ziel = $("#home-hauptziel").val();

    sendAJAX("hauptziel_erstellen", {
            "user_id": getGETParams(),
            "ziel": ziel,
        },
        function () {
            location.reload();
        }, function (status_code, message) {
            console.log(status_code);
            console.log(message);
        });
}

function hauptziel_delete(ziel_id) {
    sendAJAX("hauptziel_delete", {
            "user_id": getGETParams(),
            "ziel_id": ziel_id,
        },
        function () {
            location.reload();
        }, function (status_code, message) {
            console.log(status_code);
            console.log(message);
        });
}

function unterziel_erstellen(hauptziel_id) {
    const tmp = "#home-unterziel-" + hauptziel_id
    console.log(tmp);
    const ziel = $(tmp).val();

    sendAJAX("unterziel_erstellen", {
            "user_id": getGETParams(),
            "hauptziel_id": hauptziel_id,
            "ziel": ziel,
        },
        function () {
            location.reload();
        }, function (status_code, message) {
            console.log(status_code);
            console.log(message);
        });
}

function unterziel_abschliessen(unterziel_id) {
    sendAJAX("unterziel_abschliessen", {
            "user_id": getGETParams(),
            "unterziel_id": unterziel_id,
        },
        function () {
            location.reload();
        }, function (status_code, message) {
            console.log(status_code);
            console.log(message);
        });
}

function unterziel_delete(unterziel_id) {
    sendAJAX("unterziel_delete", {
            "user_id": getGETParams(),
            "unterziel_id": unterziel_id,
        },
        function () {
            location.reload();
        }, function (status_code, message) {
            console.log(status_code);
            console.log(message);
        });
}


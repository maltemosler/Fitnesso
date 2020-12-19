function hauptziel_erstellen() {
    const ziel = $("#home-hauptziel").val();
    const ziel_error = $("#hauptziel-create-error");

    if (validateZiel(ziel, ziel_error)) {
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
    const unterziel_error_tmp = "#unterziel-create-error-" + hauptziel_id
    const ziel = $(tmp).val();

    const unterziel_error = $(unterziel_error_tmp);
    if (validateZiel(ziel, unterziel_error)) {
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


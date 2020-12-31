function hauptziel_erstellen() {
    const ziel = $("#home-hauptziel").val();
    const ziel_error = $("#hauptziel-create-error");
    const user_id = getGETParams();
    if (user_id && validateZiel(ziel, ziel_error)) {
        sendAJAX("hauptziel_erstellen", {
                "user_id": user_id,
                "ziel": ziel,
            },
            function () {
                location.reload();
            }, function (status_code, message) {
                console.log(status_code);
                console.log(message);
            });
    } else {
        return 500
    }
}

function hauptziel_delete(ziel_id) {
    const user_id = getGETParams();
    if (user_id && ziel_id) {
        sendAJAX("hauptziel_delete", {
                "user_id": user_id,
                "ziel_id": ziel_id,
            },
            function () {
                location.reload();
            }, function (status_code, message) {
                console.log(status_code);
                console.log(message);
            });
    } else {
        return 500
    }

}

function unterziel_erstellen(hauptziel_id) {
    const tmp = "#home-unterziel-" + hauptziel_id
    const unterziel_error_tmp = "#unterziel-create-error-" + hauptziel_id
    const ziel = $(tmp).val();
    const user_id = getGETParams();
    const unterziel_error = $(unterziel_error_tmp);
    if (user_id && validateZiel(ziel, unterziel_error)) {
        sendAJAX("unterziel_erstellen", {
                "user_id": user_id,
                "hauptziel_id": hauptziel_id,
                "ziel": ziel,
            },
            function () {
                location.reload();
            }, function (status_code, message) {
                console.log(status_code);
                console.log(message);
            });
    } else {
        return 500
    }
}

function unterziel_abschliessen(unterziel_id) {
    const user_id = getGETParams();
    if (user_id && unterziel_id) {
        sendAJAX("unterziel_abschliessen", {
                "user_id": user_id,
                "unterziel_id": unterziel_id,
            },
            function () {
                location.reload();
            }, function (status_code, message) {
                console.log(status_code);
                console.log(message);
            });
    } else {
        return 500
    }
}

function unterziel_delete(unterziel_id) {
    const user_id = getGETParams();
    if (user_id && unterziel_id) {
        sendAJAX("unterziel_delete", {
                "user_id": user_id,
                "unterziel_id": unterziel_id,
            },
            function () {
                location.reload();
            }, function (status_code, message) {
                console.log(status_code);
                console.log(message);
            });
    } else {
        return 500
    }
}


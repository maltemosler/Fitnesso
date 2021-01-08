function hauptziel_erstellen() {
    // get user id from url (ziele/-1) -> -1
    const user_id = getGETParams();
    // get hauptziel text
    const ziel = $("#home-hauptziel").val();
    const ziel_error = $("#hauptziel-create-error");
    // validate userid und ziel content
    if (user_id && validateZiel(ziel, ziel_error)) {
        sendAJAX("hauptziel_erstellen", {
                "user_id": user_id,
                "ziel": ziel,
            },
            function () {
                // reload website to show the new goal
                location.reload();
            }, function (status_code, message) {
                // log when goal creation failed
                console.log(status_code);
                console.log(message);
            });
    } else {
        return 500
    }
}

function hauptziel_delete(ziel_id) {
    // get user id from url (ziele/-1) -> -1
    const user_id = getGETParams();
        // check if user_id and ziel_id is not none
    if (user_id && ziel_id) {
        sendAJAX("hauptziel_delete", {
                "user_id": user_id,
                "ziel_id": ziel_id,
            },
            function () {
                // reload website to display that the goal was removed
                location.reload();
            }, function (status_code, message) {
                // log when goal deletion failed
                console.log(status_code);
                console.log(message);
            });
    } else {
        return 500
    }

}

function unterziel_erstellen(hauptziel_id) {
    // get user id from url (ziele/-1) -> -1
    const user_id = getGETParams();

    // get unterziel text
    const tmp = "#home-unterziel-" + hauptziel_id
    const ziel = $(tmp).val();

    // get unterziel error feld
    const unterziel_error_tmp = "#unterziel-create-error-" + hauptziel_id

    const unterziel_error = $(unterziel_error_tmp);
    // check if user_id is not none and if ziel text is accepted
    if (user_id && validateZiel(ziel, unterziel_error)) {
        sendAJAX("unterziel_erstellen", {
                "user_id": user_id,
                "hauptziel_id": hauptziel_id,
                "ziel": ziel,
            },
            function () {
                // reload website to display that the minor goal was created
                location.reload();
            }, function (status_code, message) {
                // log when unterziel erstellen failed
                console.log(status_code);
                console.log(message);
            });
    } else {
        return 500
    }
}

function unterziel_abschliessen(unterziel_id) {
    // get user id from url (ziele/-1) -> -1
    const user_id = getGETParams();
    // check if user_id und unterziel id are not none
    if (user_id && unterziel_id) {
        sendAJAX("unterziel_abschliessen", {
                "user_id": user_id,
                "unterziel_id": unterziel_id,
            },
            function () {
                // reload website to display that the minor goal was successfully
                location.reload();
            }, function (status_code, message) {
                // log when unterziel abschließen failed
                console.log(status_code);
                console.log(message);
            });
    } else {
        return 500
    }
}

function unterziel_delete(unterziel_id) {
    // get user id from url (ziele/-1) -> -1
    const user_id = getGETParams();

    // check if user_id und unterziel id are not none
    if (user_id && unterziel_id) {
        sendAJAX("unterziel_delete", {
                "user_id": user_id,
                "unterziel_id": unterziel_id,
            },
            function () {
                // reload website to display that the minor goal was deleted
                location.reload();
            }, function (status_code, message) {
                // log when unterziel deletion failed
                console.log(status_code);
                console.log(message);
            });
    } else {
        return 500
    }
}


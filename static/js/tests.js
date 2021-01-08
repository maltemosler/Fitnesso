// JUnit tests wie im Unterricht besprochen
// Jede function hat mindestens 2 tests, einmal mit richtigen Parametern und ein mal mit falschen Parametern
// Dabei können interne Server Errors erstellen, da mit IDs getestet wird, die Akzeptiert werden, jedoch nicht in der Datenbank existieren
// Dies ist jedoch nicht schlimm da nur getestet wird ob der Request gesendet wird oder nicht.

QUnit.module('hauptziel_erstellen-success', function () {
    QUnit.test('hauptziel_erstellen-success', function (assert) {
        const hauptziel = $("#home-hauptziel");
        hauptziel.val("546243534")
        assert.equal(hauptziel_erstellen(), null, "Is passing the test when parameters are right");
    });
});
QUnit.module('hauptziel_erstellen-wrong-parameter-1', function () {
    QUnit.test('hauptziel_erstellen-wrong-parameter-1', function (assert) {
        const hauptziel = $("#home-hauptziel");
        hauptziel.val("")
        assert.equal(hauptziel_erstellen(), 500, "Is passing the test when parameters are missing or wrong");
    });
});
QUnit.module('hauptziel_erstellen-wrong-parameter-2', function () {
    QUnit.test('hauptziel_erstellen-wrong-parameter-2', function (assert) {
        const hauptziel = $("#home-hauptziel");
        hauptziel.val("546243535462435345462435345462435345462435345462435345462435345462435345462435345462435345462435345462435345462435345462435345462435345462435345462435345462435345462435345462435345462435345462435345462435345462435345462435345462435345462435344")
        assert.equal(hauptziel_erstellen(), 500, "Is passing the test when parameters are missing or wrong");
    });
});


QUnit.module('unterziel_erstellen-success', function () {
    QUnit.test('unterziel_erstellen-success', function (assert) {
        const hauptziel = $("#home-unterziel--1");
        hauptziel.val("546243534")
        assert.equal(unterziel_erstellen(-1), null, "Is passing the test when parameters are right");
    });
});
QUnit.module('unterziel_erstellen-wrong-parameter-1', function () {
    QUnit.test('unterziel_erstellen-wrong-parameter-1', function (assert) {
        const hauptziel = $("#home-unterziel--1");
        hauptziel.val("")
        assert.equal(unterziel_erstellen(-1), 500, "Is passing the test when parameters are missing or wrong");
    });
});
QUnit.module('unterziel_erstellen-wrong-parameter-2', function () {
    QUnit.test('unterziel_erstellen-wrong-parameter-2', function (assert) {
        const hauptziel = $("#home-unterziel--1");
        hauptziel.val("546243535462435345462435345462435345462435345462435345462435345462435345462435345462435345462435345462435345462435345462435345462435345462435345462435345462435345462435345462435345462435345462435345462435345462435345462435345462435345462435344")
        assert.equal(unterziel_erstellen(-1), 500, "Is passing the test when parameters are missing or wrong");
    });
});

QUnit.module('hauptziel_delete-success', function () {
    QUnit.test('hauptziel_delete-success', function (assert) {
        assert.equal(hauptziel_delete(-1), null, "Is passing the test when parameters are right");
    });
});
QUnit.module('hauptziel_delete-wrong-parameter-1', function () {
    QUnit.test('hauptziel_delete-wrong-parameter-1', function (assert) {
        assert.equal(hauptziel_delete(), 500, "Is passing the test when parameters are missing or wrong");
    });
});


QUnit.module('unterziel_abschliessen-success', function () {
    QUnit.test('unterziel_abschliessen-success', function (assert) {
        assert.equal(unterziel_abschliessen(-1), null, "Is passing the test when parameters are right");
    });
});
QUnit.module('unterziel_abschliessen-wrong-parameter-1', function () {
    QUnit.test('unterziel_abschliessen-wrong-parameter-1', function (assert) {
        assert.equal(unterziel_abschliessen(), 500, "Is passing the test when parameters are missing or wrong");
    });
});


QUnit.module('unterziel_delete-success', function () {
    QUnit.test('unterziel_delete-success', function (assert) {
        assert.equal(unterziel_delete(0), 500, "Is passing the test when parameters are missing or wrong");
    });
});
QUnit.module('unterziel_delete-wrong-parameter-1', function () {
    QUnit.test('unterziel_delete-wrong-parameter-1', function (assert) {
        assert.equal(unterziel_delete(), 500, "Is passing the test when parameters are missing or wrong");
    });
});
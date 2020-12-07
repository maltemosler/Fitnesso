QUnit.module('extractingList', function () {
    QUnit.test('should extracting a list after :', function (assert) {
        assert.equal(extractingList(sentence), ['cherries', 'limes', 'oranges', 'apples'], "Is passing the test when result is like ['cherries','limes','oranges','apples']");
    });
});
// the sendAJAX functions
function sendAJAX(base_url, base_data, onsuccess, onfail, error) {
    let data = {};
    // set data when base_data content exists
    if (typeof base_data != "undefined") {
        data = base_data;
    }
    // add the csrfmiddlewaretoken to the data
    data["csrfmiddlewaretoken"] = document.getElementsByName('csrfmiddlewaretoken')[0].value;

    // build the ajax url
    let url = "/ajax/" + base_url + "/";

    // send ajax request with JQuery
    $.ajax({
        type: "POST",
        url: url,
        data: data
    }).done(onsuccess)
        .fail(function (data) {
            console.log(data)
            // execute onfail function (selbst erstellbar beim Aufruf der sendAJAX function)
            onfail(data['status'], data['responseText']);
        });
}
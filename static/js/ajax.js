function sendAJAX(base_url, base_data, onsuccess, onfail, error) {
    let data = {};
    if (typeof base_data != "undefined") {
        data = base_data;
    }

    data["csrfmiddlewaretoken"] = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    let url = "/ajax/" + base_url + "/";
    $.ajax({
        type: "POST",
        url: url,
        data: data
    }).done(onsuccess)
        .fail(function (data) {
            console.log(data)
            onfail(error);
        });
}
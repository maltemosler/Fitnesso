// this function returns the url param (.../ziele/-1) -> -1
function getGETParams() {
    return location.href.substring(location.href.lastIndexOf('/') + 1)
}
function getGETParams() {
    return location.href.substring(location.href.lastIndexOf('/') + 1)
}
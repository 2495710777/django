function changeImage() {
    var i = document.getElementById('changeImg');
    i.src = '/axfuser/get_code/?'+Math.random()
}

function parse() {
    var password = document.getElementById('exampleInputPassword1').value;
    password = md5(password);
    document.getElementById('exampleInputPassword1').value = password;
    return true
}
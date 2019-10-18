$(function () {
    CheckName();
    checkPwd();
});

function CheckName() {
    $('#exampleInputName').blur(function () {
        var name = $(this).val();
        var reg = /^[a-z]{3,6}$/;

        if (reg.test(name)) {
            // $('#nameinfo').html('√用户名可以使用').css({'font-size':10,'color':'green'})
            $.getJSON('/axfuser/checkName/',
                {'name': name},
                function (data) {
                    if (data['status'] === 200) {
                        $('#nameinfo').html(data['msg']).css({'font-size': 10, 'color': 'green'});
                    } else {
                        $('#nameinfo').html(data['msg']).css({'font-size': 10, 'color': 'red'});
                        $('#exampleInputName').val('')
                    }
                });
        } else {
            $('#nameinfo').html('×用户名不符合要求').css({'font-size': 10, 'color': 'red'})
            $('#exampleInputName').val('');
        }
        button_disabled()
    })
}

function checkPwd() {
    $('#exampleInputPassword1').blur(function () {
        var password = $(this).val();
        var rep = /^[a-zA-Z0-9!#*_]{3,6}$/;

        if (rep.test(password)) {
            // $('#nameinfo').html('√用户名可以使用').css({'font-size':10,'color':'green'})
            $('#passwordinfo').html('√密码可以使用').css({'font-size': 10, 'color': 'green'})
        } else {
            $('#passwordinfo').html('×密码不符合要求').css({'font-size': 10, 'color': 'red'});
            $(this).val('');
        }
        button_disabled()
    });

    $('#exampleInputPassword2').blur(function () {
        var password1 = $(this).val();
        var password = $('#exampleInputPassword1').val();
        if (password === password1 && password1 !== '') {
            $('#passwordinfo1').html('确认密码成功').css({'font-size': 10, 'color': 'green'})
        } else {
            $('#passwordinfo1').html('确认密码失败').css({'font-size': 10, 'color': 'red'})
            $(this).val('');
        }
        button_disabled()
    });
}

function button_disabled() {
    var name_val = $('#exampleInputName').val().length;
    var email_val = $('#exampleInputEmail1').val().length;
    var pwd_val = $('#exampleInputPassword1').val().length;
    var rpwd_val = $('#exampleInputPassword2').val().length;
    if(name_val === 0 || pwd_val=== 0 || rpwd_val === 0 || email_val === 0){
        $('#exampleButton').attr("disabled",true)
    }else{
        $('#exampleButton').attr("disabled",false)
    }
}

function parse1() {
    var password = $('#exampleInputPassword1').val();
    var password1 = $('#exampleInputPassword2').val();
    password = md5(password);
    password1 = md5(password1);
    $('#exampleInputPassword1').val(password);
    $('#exampleInputPassword2').val(password1);
    button_disabled();
    return true
}
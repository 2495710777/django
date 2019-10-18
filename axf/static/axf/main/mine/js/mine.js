$(function () {
    checkLogin = $('#checkLogin').text();
    if(checkLogin === '未登录'){
        $('#is_hid').attr("hidden", true)
    }else{
        $('#is_hid').attr("hidden", false)
    }
});

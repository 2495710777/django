$(function () {
    $('#all_type').click(function () {
        $(this).find('span').find('span').toggleClass('glyphicon glyphicon-chevron-up glyphicon glyphicon-chevron-down')
        $('#all_type_container').toggle();

    });
    $('#sort_rule').click(function () {
        $(this).find('span').find('span').toggleClass('glyphicon glyphicon-chevron-up glyphicon glyphicon-chevron-down')
        $('#goods_sort').toggle();
    });

    $('.addShopping').click(function () {
        var $button = $(this);
        var goodsid = $button.attr('goodsid');
        $.get('/axfcart/addToCart/',
            {'goodsid':goodsid},
            function(data) {
                if(data['status'] === 200){
                    $button.prev().html(data['c_goods_num'])
                }else{
                    window.location.href='/axfuser/login/'
                }
            })
    });
        $('.subShopping').click(function () {
        var $button = $(this);
        var goodsid = $button.attr('goodsid');
        $.get('/axfcart/subToCart/',
            {'goodsid':goodsid},
            function(data) {
                if(data['status'] === 200){
                    $button.next().html(data['c_goods_num'])
                }else{
                    window.location.href='/axfuser/login/'
                }
            })
    });
});
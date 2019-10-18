$(function () {
    $('.addShopping').click(function () {
        var $button = $(this);
        var cart_id = $button.parent().parent().attr('cart_id');
        $.post('/axfcart/addCart/',
            {'cart_id': cart_id},
            function (data) {
                if (data['status'] === 200) {
                    $button.prev().html(data['c_goods_num']);
                    $('#total_price').html(data['total_price'])
                }
            })
    });
    $('.subShopping').click(function () {
        var $button = $(this);
        var cart_id = $button.parent().parent().attr('cart_id');
        $.post('/axfcart/subCart/',
            {'cart_id': cart_id},
            function (data) {
                if (data['status'] === 200) {
                    $button.next().html(data['c_goods_num']);
                    $('#total_price').html(data['total_price'])
                } else {
                    $button.parent().parent().remove();
                    $('#total_price').html(data['total_price'])
                }
            })
    });

    $('.menuList').find(".confirm").click(function () {
        var $confirm = $(this);
        var cart_id = $confirm.parent().attr('cart_id');
        $.ajax(
            {
                url: '/axfcart/changeStatus/',
                data: {'cart_id': cart_id},
                type: 'GET',
                dataType: 'json',
                success: function (data) {
                    if (data['status'] === 200) {
                        if (data['c_is_select']) {
                            $confirm.find('span').find('span').html('√');
                            $('#total_price').html(data['total_price'])
                        } else {
                            $confirm.find('span').find('span').html('');
                            $('#total_price').html(data['total_price'])
                        }
                        if (data['is_all_select']) {
                            $('#all_select').find('span').find('span').html('√')
                        } else {
                            $('#all_select').find('span').find('span').html('')
                        }
                    }
                }
            }
        )
    });

    //    点击全选
//          把购物车页面中的选中的放在一个列表中
//          把购物车页面中的未选中的放在一个列表中
    $('#all_select').click(function () {

        var $all_select = $('#all_select');

        var select_list = [];
        var unselect_list = [];

        var $confirm = $('.menuList').find(".confirm");

        $confirm.each(function () {
            var cart_id = $(this).parent().attr('cart_id');
            if ($(this).find('span').find('span').html()) {
                select_list.push(cart_id);
            } else {
                unselect_list.push(cart_id)
            }
        });
        if (unselect_list.length > 0) {
            $.getJSON('/axfcart/allSelect/',
                {'cartid_list': unselect_list.join('#')},
                function (data) {
                    if (data['status'] === 200) {
                        $confirm.find('span').find('span').html('√');
                        $('#all_select').find('span').find('span').html('√');
                        $('#total_price').html(data['total_price'])
                    }
                })
        } else {
            $.getJSON('/axfcart/allSelect/',
                {'cartid_list': select_list.join('#')},
                function (data) {
                    if (data['status'] === 200) {
                        $confirm.find('span').find('span').html('');
                        $('#all_select').find('span').find('span').html('');
                        $('#total_price').html(data['total_price'])
                    }
                })
        }

    });


    $('#make_order').click(function () {

        var select_list = [];

        var unselect_list = [];

        var $confirm = $('.menuList').find(".confirm");

        $confirm.each(function () {
            var cart_id = $(this).parent().attr('cart_id');
            if ($(this).find('span').find('span').html()) {
                select_list.push(cart_id);
            } else {
                unselect_list.push(cart_id)
            }
        });
        if(select_list.length === 0){
            return;
        }else{
            $.ajax(
                {
                    url:'/axforder/make_order/',
                    type:'GET',
                    dataType: 'json',
                    success:function (data) {
                        if(data['status'] === 200){
                            window.location.href = '/axforder/order_detail/?order_id='+data['order_id']
                        }
                    }
                }
            )
        }
    });
});

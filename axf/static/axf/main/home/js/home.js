$(function () {
   initWheel();
   initMustBuy();

});

function initWheel() {
    var mySwiper = new Swiper('#topSwiper',
                            {
                                loop:true,
                                autoplay:3000,
                                autoplayDisableOnInteraction: false,
                                pagination: '.swiper-pagination',
                                prevButton:'.swiper-button-prev',
                                nextButton:'.swiper-button-next',

                            })
}
function initMustBuy() {
    var mySwiper1 = new Swiper('#swiperMenu',
        {
            slidesPerView:3,
        })
}
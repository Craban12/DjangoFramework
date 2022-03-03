window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function () {
        let target = event.target;
        let basketID = target.name
        let basketQuantity = target.value
        $.ajax({
            url: '/baskets/basket-edit/' + basketID + '/' + basketQuantity + '/',
            success: function (data) {
                $('.basket_list').html(data.result);
            }
        })
    })
}
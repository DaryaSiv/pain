$(document).ready(()=>{
    var selectbookID = 0;
    $(".addToCart").click((event)=>{
        event.preventDefault();

        var price = $(`#price${selectbookID}`).text().replace(',', '.');
        var url = `/myapp/cart/add/${selectbookID}`;
        $.ajax({

            url: url,
            method: `POST`,
            headers: {
                "x-csrf-token": $("input[name='csrfmiddlewaretoken']").val(),
                contentType: 'application/json',

            },
            data: {
                "quantity_buying": 1,
                "price": price
            },
            success: () => {
                $('#addToCartModal').modal('hide');
                $('#cartSuccessModal').modal('show');
            },
            error: () => {
                alert("Ошибочка")
            }
        });
    });

    $(".cart").click((event) => {
        selectbookID = event.currentTarget.attributes['data-book'].value;

        $('#addToCartModal').modal('show');

    });
})
$(document).ready(()=>{
    $(".addToCart").click((event)=>{
        event.preventDefault();
        
        // var bookID = event.target.attributes['data-book'].id;
        var bookID = event.currentTarget.attributes['data-book'].value;
        var price = $(`#price${bookID}`).text().replace(',', '.');
        var url = `/myapp/cart/add/${bookID}`;
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
                
                alert("Работает")
            },
            error: () => {
                
                alert("Ошибочка")
            }
        })


        // alert("");
    });
})
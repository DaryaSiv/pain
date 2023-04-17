$(document).ready(()=>{
    var selectbookID = 0;
    $(".addToFav").click((event)=>{
        event.preventDefault();

        var url = `/myapp/books/favorite/add/${selectbookID}`;
        $.ajax({

            url: url,
            method: `POST`,
            headers: {
                "x-csrf-token": $("input[name='csrfmiddlewaretoken']").val(),
                contentType: 'application/json',

            },
            success: (response) => {
                if (response.success == true) {
                    $('#addToFavModal').modal('hide');
                    $('#favSuccessModal').modal('show');
                }
                else {
                    alert('Не добавлена')
                }

            },
            error: () => {

                alert("Ошибочка")
            }
        });

    });
    
    $(".favorite").click((event) => {
        selectbookID = event.currentTarget.attributes['data-book'].value

        $('#addToFavModal').modal('show');

    });
})
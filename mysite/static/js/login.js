$(document).ready(()=>{
    $(".login").click((event)=>{
        event.preventDefault();

        var url = `/myapp/login`;
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

})
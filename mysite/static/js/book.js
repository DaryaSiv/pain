$(document).ready(() => {
    $("[id^='books']").click((event) => {
        var bookID = event.target.attributes['data-genre-id'].value;
        // var wqe = `http://localhost:8000/get_furniture_by_room_id/${roomID}`;
        // debugger
        $.ajax({
            url: `http://127.0.0.1:8000/index/${bookID}`,
            method: 'GET',
            headers: {
                contentType: 'application/json',
            },
            success: (response) => {
                console.log(response)
            },
            error: () => {
                alert("Ошибочка")
            }
        })

    });
})
$(document).ready(function () {
    // example: https://getbootstrap.com/docs/4.2/components/modal/
    // Remove dish
    $('.remove').click(function () {
        const remove = $(this)
        console.log(remove);
        $.ajax({
            type: 'POST',
            url: '/restaurant/' + remove.data('restid') + '/delete/' + remove.data('source'),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });
    
});
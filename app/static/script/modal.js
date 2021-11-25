$(document).ready(function () {
    // example: https://getbootstrap.com/docs/4.2/components/modal/
    // show modal
    $('#restaurant-modal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const restaurantID = button.data('source') // Extract info from data-* attributes
        const contentName = button.data('contentName') // Extract info from data-* attributes

        const modal = $(this)
        if (restaurantID === 'New Restaurant') {
            modal.find('.modal-title').text(restaurantID)
            $('#restaurant-form-display').removeAttr('restaurantID')
        } else {
            modal.find('.modal-title').text('Edit Restaurant')
            $('#restaurant-form-display').attr('restaurantID', restaurantID)
        }

        if (contentName) {
            modal.find('.form-control').val(contentName);
        } else {
            modal.find('.form-control').val('');
        }
    })

    $('[id^=restaurant-edit-modal]').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const restaurantID = button.data('source') // Extract info from data-* attributes
        const contentName = button.data('contentName') // Extract info from data-* attributes

        const modal = $(this)
        if (restaurantID === 'New Restaurant') {
            modal.find('.modal-title').text(restaurantID)
            $('#restaurant-form-display').removeAttr('restaurantID')
        } else {
            modal.find('.modal-title').text('Edit Restaurant')
            $('#restaurant-form-display').attr('restaurantID', restaurantID)
        }

        if (contentName) {
            modal.find('.form-control').val(contentName);
        } else {
            modal.find('.form-control').val('');
        }
    })

    // Remove restaurant
    $('.remove').click(function () {
        const remove = $(this)
        $.ajax({
            type: 'POST',
            url: '/delete/' + remove.data('source'),
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
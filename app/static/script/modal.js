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

    // Add restaurant
    // $("#restaurant-form").submit(function(){
    //$('#submit-restaurant').click(function () {
        // console.log("hello")
        //const rID = $('#restaurant-form-display').attr('restaurantID'); // need to fix this
        //console.log($('#restaurant-modal').find('.form-control').val())
        //console.log(rID)
        // var formData = JSON.stringify($("#restaurant-form").serializeArray());
        // console.log(formData)
        // $.ajax({
        //     type: 'POST',
        //     url: '/create/',
            // // contentType: 'application/json;charset=UTF-8',
            // // data: JSON.stringify({
            // //     'RestaurantName': $(document).getElementById("rest-name").value,
            // // //     'ZipCode': $(document).getElementById("rest-zip").value,
            // // //     'Address': $(document).getElementById("rest-addr").value
            // // // }),
            // // data: formData,
            // success: function (res) {
    //             console.log("here")
    //             console.log(res.response)
    //             location.reload();
    //         },
    //         error: function () {
    //             console.log('Error');
    //         }
    //     });
    // });

    // Update restaurant

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

    // Menu button
    // $('.state').click(function () {
    //     const state = $(this)
    //     const tID = state.data('source')
    //     const new_state
    //     if (state.text() === "In Progress") {
    //         new_state = "Complete"
    //     } else if (state.text() === "Complete") {
    //         new_state = "Todo"
    //     } else if (state.text() === "Todo") {
    //         new_state = "In Progress"
    //     }

    //     $.ajax({
    //         type: 'POST',
    //         url: '/edit/' + tID,
    //         contentType: 'application/json;charset=UTF-8',
    //         data: JSON.stringify({
    //             'status': new_state
    //         }),
    //         success: function (res) {
    //             console.log(res)
    //             location.reload();
    //         },
    //         error: function () {
    //             console.log('Error');
    //         }
    //     });
    // });

});
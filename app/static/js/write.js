// write.js
$(document).ready(function () {

    console.log('ere')

    // process the form
    $('#upload').click(function (event) {

        console.log('submite oress')


        var formdata = new FormData()
        var fileInput = document.getElementById('post')
        var file = fileInput.files[0]

        console.log($('#title').val())
        formdata.append('title', $('#title').val())
        formdata.append('post', file)
        

        // process the form
        $.ajax({
            type: 'POST', // define the type of HTTP verb we want to use (POST for our form)
            url: '/writeThought', // the url where we want to POST
            data: formdata, // our data object
            processData: false,
            contentType: false,
            //dataType: 'json', // what type of data do we expect back from the server
            //encode: true
        }).done(function (data) {
                // log data to the console so we can see
                console.log(data);
                M.toast({ html: data.message })

                // here we will handle errors and validation messages
            });

        // stop the form from submitting the normal way and refreshing the page
        event.preventDefault();
        
    });


    /*
    // Inject our CSRF token into our AJAX request.
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", "{{ form.csrf_token._value() }}")
            }
        }
    })
    */

});
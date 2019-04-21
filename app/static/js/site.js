
$(document).ready(function () {
    console.log(' requested')

    $('#loginButton').click(function () {
        console.log('login requested')
        var emailLogin = $("#emailLogin").val();
        var passwordLogin = $("#passwordLogin").val();
        data = { email: emailLogin, password: passwordLogin };

        console.log(data);

		
        //TODO: Use fetch instead
        $.ajax({
            url: "/login",
            type: "POST",
            data: data,
            erorr: function (error) {
                console.log(`Error ${error}`)
            }
		})
		

    })

})

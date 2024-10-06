const recaptcha_key = JSON.parse(document.getElementById('recaptcha-key').textContent);

$( document ).ready(function() {
    $("form").on("submit", async function( event ) {
        event.preventDefault();
        try {
            console.log(typeof recaptcha_key);
            const token = await grecaptcha.execute(recaptcha_key, { action: event.currentTarget.dataset.recaptchaAction});
            console.log($(event.currentTarget).find( "#id_recaptcha" )[0]);
            $(event.currentTarget).find( "#id_recaptcha" ).val(token)
            event.currentTarget.submit();
        } catch (error) {
            // Handle any errors
            console.error('Error obtaining reCAPTCHA token:', error);
            document.getElementById('non_field_errors').textContent = 'reCAPTCHA validation failed. Please try again.';
        }
    });
});
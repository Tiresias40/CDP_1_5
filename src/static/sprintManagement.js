
$(function() {
    $('#sprint_add_button').click(function() {
        $.ajax({
            url: '/addSprint',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response){
            
            },
            error: function(error) {
                console.log(error);
            }
        });
    });

    $('#sprint_delete_button').click(function() {
        $.ajax({
            url: '/deleteSprint',
            data: $('form').serialize(),
            type: 'DELETE',
            success: function(response){
            
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});

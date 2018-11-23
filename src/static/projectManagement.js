
$(function() {
    $('button').click(function() {
        $.ajax({
            url: '/addProject',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response){
              var json = JSON.parse(response);
              $('tbody').append('<tr><td>'+json.id+'</td><td>'+json.name+'</td><td></td></tr>');
            },
            error: function(error) {
                console.log(error);
            }
        });
      });
});

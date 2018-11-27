
$(function() {
    $('button').click(function() {
        $.ajax({
            url: '/addProject',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response){
              var json = JSON.parse(response);
              $('.card-deck').append('<div class="card bg-primary text-center"><div class="card-header">'+json.name+'</div><div class="card-body text-center"><p class="card-text">'+json.id+'</p></div></div>');
            },
            error: function(error) {
                console.log(error);
            }
        });
      });
});

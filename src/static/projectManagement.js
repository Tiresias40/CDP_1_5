
$(function() {
    $('button').click(function() {
        $.ajax({
            url: '/addProject',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response){
              var json = JSON.parse(response);
              $('.card-deck-wrapper').append(
                '<div class="card-deck">' +
                  '<div class="card bg-primary">' +
                    '<div class="card-header">'+json.name+'</div>' +
                    '<div class="card-body">' + 
                      '<p class="card-text">'+json.id+'</p>' +
                    '</div>' +
                  '</div>' + 
                '</div>'
              );
            },
            error: function(error) {
                console.log(error);
            }
        });
      });
});

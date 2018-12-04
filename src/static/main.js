$(function() {
    $('button').click(function() {
      var currentProjectId = $();
        $.ajax({
            url: '/dashBoardPage',
            data:
            type: 'GET',
            success: function(response){
              var json = JSON.parse(response);
              $('.card-deck').append('<div class="card bg-primary text-center"><div class="card-header">'+json.name+'</div><div class="card-body text-center"><p class="card-text">'+json.id+'</p></div></div>');
            },
            error: function(error) {
                console.log(error);
            }
        });
      });

      $(document).ready(function(){
        $()

      });
});

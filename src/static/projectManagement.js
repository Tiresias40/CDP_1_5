
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

    $(document).ready(function() {
      $.ajax({
        url: '/projectsPage',
        success: function(response){
          var json;
          for (proj in response){
            json = JSON.parse(response[proj]);
            console.log(json.name);
          };

        //  var json = JSON.parse(response[1]);

        /*  $.each(response, function(index,value){
            //var json = JSON.parse(d)
            console.log(response[value]);
         });*/
        },
        error: function(error) {
            console.log(error);
        }
      });
    });
});

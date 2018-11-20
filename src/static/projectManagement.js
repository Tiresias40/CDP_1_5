
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
          var json =JSON.parse($('#listToDisplay').text());
          for (i in json.projects){
            $('tbody').append('<tr><td>'+json.projects[i].id+'</td><td>'+json.projects[i].name+'</td><td></td></tr>');
          }
          $('#listToDisplay').hide();
          //console.log($('#listToDisplay').text());
        //  console.log(json.projects.);
    /*      var json;
          for (proj in response){
            //json = JSON.parse(response[proj]);
            console.log(response[proj]);
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

$(function() {
    $('.plus').click(function() {
      var selectedProjectsId = [];
      $('select option:selected').each(function(){
        selectedProjectsId.push($(this).attr('value'));
      });
      var userId = $('.plus').attr('value');
      selectedProjectsId.push(userId);
      encoded =JSON.stringify(selectedProjectsId);
      console.log(encoded);
        $.ajax({
            url: '/updateDevs',
            data: encoded,
            type: 'POST',
            success: function(response){
              var json = JSON.parse(response);
              for(i in json.projects){
                $('.modal-body').append('<p>'+json.projects[i].name+'</p>');
              }
            },
            error: function(error) {
                console.log(error);
            }
        });
    });

    $('.remove').click(function() {
      var selectedProjectsId = [];
      $('select option:selected').each(function(){
        selectedProjectsId.push($(this).attr('value'));
      });
    /*    $.ajax({
            url: '/updateDevs',
            data: selectedProjectsId,
            type: 'DELETE',
            //success: function(){},
            error: function(error) {
                console.log(error);
            }
        });*/
    });
});


$(function() {
    $('.addProject').click(function() {
        $.ajax({
            url: '/addProject',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response){
              var json = JSON.parse(response);
              $('.card-deck').append(
                '<div class="card shadow-sm bg-white rounded w-25">'+
                  '<div class="view overlay">'+
                    '<img class="card-img-top" src="https://mdbootstrap.com/img/Photos/Others/photo9.jpg" alt="Card image cap">'+
                    '<a>'+
                      '<div class="mask rgba-white-slight"></div>'+
                    '</a>'+
                  '</div>'+
                  '<div class="card-body" >'+
                        '<h4 class="card-title">'+json.name+'</h4><hr>'+
                	      '<p class="card-text" >Id : <span class="projectId">'+json.id+'</span></p>'+
                        '<button class="btn btn-indigo btn-rounded btn-md projectSelector">Choisir</button>'+
                  '</div>'+
                '</div>');
              if ((json.id % 4)==0){
                $('.card-deck').append('<div class="w-100 hidden-md-down hidden-xl-up"><br/> <br/></div>');
              }
            },
            error: function(error) {
                console.log(error);
            }
        });
      });


      $('.projectSelector').click(function() {
        var currentProjectId = $(this).prev().children('.projectId').text();
        const pathUrl ='/projects/id/'+currentProjectId;
        $(location).attr('href',pathUrl);
    });
});

$(function() {
    $('button').click(function() {
        $.ajax({
            url: '/addIssue',
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

      $(document).ready(function(){
        const project_id = $('#currentProjectId').text();
        $('#navGroup').append('<li class="nav-item"><a class="nav-link"'+
          ' id="issueNav" href="/projects/id/'+project_id+'/issuesPage">Issues</a></li>'+
          '<li class="nav-item"><a class="nav-link" id="sprintNav" '+
          'href="/projects/id/'+project_id+'/sprintsPage">'+
          'Sprints</a></li><li class="nav-item"><a class="nav-link"'+
          ' id="devNav" href="/projects/id/'+project_id+'/managementPage">Management</a></li>');
      });
});

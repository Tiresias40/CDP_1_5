
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

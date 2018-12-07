$(function() {
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

$(function() {

    $('#selProject').change(function(){
          const selectedProjectId = $('select option:selected').attr('value');
          $.ajax({
              url: '/listRelatedDevs',
              data: selectedProjectId,
              type: 'POST',
              success: function(response){
                if (response != 'Empty'){
                  var json = JSON.parse(response);
                  for(i in json.users){
                    $('#displayDevsTable table').append('<tr><td>'+json.users[i].username+'</td><td>'+json.users[i].first_name+'</td><td>'+json.users[i].last_name+'</td><td class="pt-3-half"> <span class="table-up"><a href="#!" class="indigo-text"><i class="fa fa-long-arrow-up" aria-hidden="true"></i></a></span>  <span class="table-down"><a href="#!" class="indigo-text"><i class="fa fa-long-arrow-down"    aria-hidden="true"></i></a></span></td>   <td><span class="table-remove"><button type="button" class="btn btn-danger btn-rounded btn-sm my-0">Remove</button></span>                    </td>                  </tr>');
                  }
                }
                else {

                }

              },
              error: function(error) {
                  console.log(error);
              }
          });

    });

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


var $TABLE = $('#displayDevsTable');
var $BTN = $('#export-btn');
var $EXPORT = $('#export');

$('.table-add').click(function () {
var $clone = $TABLE.find('tr.hide').clone(true).removeClass('hide table-line');
$TABLE.find('table').append($clone);
});

$('.table-remove').click(function () {
$(this).parents('tr').detach();
});

$('.table-up').click(function () {
var $row = $(this).parents('tr');
if ($row.index() === 1) return; // Don't go above the header
$row.prev().before($row.get(0));
});

$('.table-down').click(function () {
var $row = $(this).parents('tr');
$row.next().after($row.get(0));
});

// A few jQuery helpers for exporting only
jQuery.fn.pop = [].pop;
jQuery.fn.shift = [].shift;

$BTN.click(function () {
var $rows = $TABLE.find('tr:not(:hidden)');
var headers = [];
var data = [];

// Get the headers (add special header logic here)
$($rows.shift()).find('th:not(:empty)').each(function () {
headers.push($(this).text().toLowerCase());
});

// Turn all existing rows into a loopable array
$rows.each(function () {
var $td = $(this).find('td');
var h = {};

// Use the headers from earlier to name our hash keys
headers.forEach(function (header, i) {
h[header] = $td.eq(i).text();
});

data.push(h);
});

// Output the result
$EXPORT.text(JSON.stringify(data));
});

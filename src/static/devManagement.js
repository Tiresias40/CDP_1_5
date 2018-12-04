
    $('#addDevsModalButton').click(function() {
      var projectId = $('#projectId').text();
        $.ajax({
            url: '/usersAvailable',
            data: projectId,
            type: 'POST',
            success: function(response){
                $('#modalTable tbody').empty();
                if(response != "Empty"){
                  console.log("ModalClick")
                  $('#modalDevsToAdd').prop("disabled",false);
                  var json = JSON.parse(response);
                  for(i in json.devs){
                    $('.modal-body table tbody').append('<tr><td>  <input type="checkbox" class="checkboxUsers" name="fancy-checkbox-default" autocomplete="off" value="'+json.devs[i].id+'" /></td><td>'+json.devs[i].id+'</td><td>'+json.devs[i].username+'</td><td>'+json.devs[i].first_name+'</td><td>'+json.devs[i].last_name+'</td></tr>');
                  }
                }
                else {
                  $('#modalDevsToAdd').prop("disabled",true);
                }


            },
            error: function(error) {
                console.log(error);
            }
        });
    });

    $('#modalDevsToAdd').click(function() {
      var projectId = $('#projectId').text();
      var usersChecked =[];
      $(".checkboxUsers:checked").each(function() {
		      usersChecked.push($(this).val());
          console.log($(this).val());
	    });
      $('.checkboxUsers:checked').each(function() {
         $(this).removeAttr('checked');
      });

      var json = '{"users":'+JSON.stringify(usersChecked)+',';
      var jsonbis= '"id": '+JSON.stringify(projectId)+'}';
      var res = json+jsonbis;
        $.ajax({
            url: '/addDevs',
            dataType: 'json',
            data: res,
            type: 'POST',
            success: function(response){
                var json =response;
                for(i in json.devs){
                  $('#displayDevsTable table').append('<tr><td class="inputUsername pt-3-half">'+json.devs[i].username+'</td><td>'+json.devs[i].first_name+'</td><td>'+json.devs[i].last_name+'</td><td class="pt-3-half"><span class="table-up"><a href="#!" class="indigo-text"><i class="fas fa-arrow-up" aria-hidden="true"></i></a></span> <span class="table-down"><a href="#!" class="indigo-text"><i class="fas fa-arrow-down" aria-hidden="true"></i></a></span> </td> <td> <span class="table-remove"><button type="button" class="btn btn-danger btn-rounded btn-sm my-0">Remove</button></span> </td></tr>');
                }
            },
            error: function(error) {
                console.log(error);
            }
        });
    });

    var $TABLE = $('#displayDevsTable');
    var $BTN = $('#export-btn');



    $('.table-remove').click(function () {
      var username= '{"username": '+JSON.stringify($(this).parents('tr').find('.inputUsername').text())+',';
      var projectId = '"project_id": '+JSON.stringify($('#projectId').text())+'}';
      var res = username+projectId;
      $(this).parents('tr').detach();
      $.ajax({
        url: '/deleteDev',
        dataType: 'json',
        data: res,
        type: 'DELETE',
        success: function(response){
        },
        error: function(error) {
            console.log(error);
        }
      });
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
    });

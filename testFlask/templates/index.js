path = "../database/projectManagement.py"

document.querySelector("#addProject").addEventListener("click", addProject);

function addProject() {
    $.ajax({
        type: "POST",
        url: path,
        data: { name : projectname },
        success:function() {
            alert("Projet ajouté avec succès");
        },
        error:function() {
            alert("Error");
        }
    })
}

function getUserProjects() {
    $.ajax({
        type: "GET",
        url: path,
        dataType: "json",
        success:function(response) {
            if(!$("#listProjects").length != 0)
                $("#listProjects").empty();

            for (let p in response){
                let row = "<tr><th>" + response[p]["id"] + "</th><th>" + response[p]["name"] + "</th></tr>";
                $("#listProjects").append(row);
            }
        },
        error:function() {
            alert("Error");
        }
    });
}
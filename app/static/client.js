var el = x => document.getElementById(x);

function showPicker() {
  el("file-input").click();
}

function showPicked(input) {
  el("upload-label").innerHTML = input.files[0].name;
  var reader = new FileReader();
  reader.onload = function(e) {
    el("image-picked").src = e.target.result;
    el("image-picked").className = "";
  };
  reader.readAsDataURL(input.files[0]);
}



function analyze() {
  var uploadFiles = el("file-input").files;
  if (uploadFiles.length !== 1) alert("Please select a file to analyze!");


  el("analyze-button").innerHTML = "Generate...";
  var xhr = new XMLHttpRequest();
  xhr.open("POST", `/analyze`,
    true);
  xhr.onerror = function() {
    alert(xhr.responseText);
  };
  xhr.onload = function(e) {
    if (this.readyState === 4) {
      var response = JSON.parse(e.target.responseText);
      var task_id = response["task_id"];
      var g = setInterval(function () {
        var oReq = new XMLHttpRequest();
        oReq.open("GET", `task/${task_id}`);
        oReq.onload = function(m) {
          var res = JSON.parse(m.target.responseText);
          var r = res['ready'];
          if (r) {
            el("image-picked").src = res['result'];
            clearInterval(g);
          }
        }
        oReq.send()
      }, 2000)
    }
    el("analyze-button").innerHTML = "Analyze";
  };

  var fileData = new FormData();
  fileData.append("file", uploadFiles[0]);
  xhr.send(fileData);
}


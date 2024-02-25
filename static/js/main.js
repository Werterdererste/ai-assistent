function sendData() {
  /*
  sendet frage zum server
  */
  var formData = new FormData(document.getElementById("prompt-form"));

  var xhr = new XMLHttpRequest();

  xhr.open("POST", "/api/model", true);

  xhr.onreadystatechange = function () {
    if (xhr.readyState == XMLHttpRequest.DONE) {
      if (xhr.status == 200) {
        console.log("Data sent successfully!");
        console.log(xhr.responseText);
        printdata(xhr.responseText);
      } else {
        console.log("Error:", xhr.status);
      }
    }
  };

  // Send the form data
  xhr.send(formData);
}

function printdata(data) {
  //erstlellt ein objekt aus dem json file
  obj = JSON.parse(data);
  console.log(obj.prompt);
  CardQuestion(obj.prompt);
  CardAnswere(obj.answer);
}

function CardQuestion(question) {
  //gib eine massagebox zurück
  var massage_container = document.getElementById("massage-container");
  massage_container.innerHTML += `
<div class="card text-bg-primary mb-3">
  <div class="card-body">
    <p class="card-text">${question}</p>
  </div>
</div>
`;
}
function CardAnswere(answere) {
  //gib eine massagebox zurück
  var massage_container = document.getElementById("massage-container");
  massage_container.innerHTML += `
  <div class="card text-bg-success mb-3">
    <div class="card-body">
      <p class="card-text">${answere}</p>
    </div>
  </div>
  `;
}

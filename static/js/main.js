function sendData() {
  /*
  sendet frage zum server
  */
  var formData = new FormData(document.getElementById("prompt-form"));

  CardQuestion(document.getElementById("question-feld").value);
  var xhr = new XMLHttpRequest();

  xhr.open("POST", "/api/model", true);

  xhr.onreadystatechange = function () {
    if (xhr.readyState == XMLHttpRequest.DONE) {
      if (xhr.status == 200) {
        console.log("Data sent successfully!");
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
  CardAnswere(obj.answer);
}

function CardQuestion(question) {
  //gib eine massagebox zurück
  var massage_container = document.getElementById("massage-container");

  var card = document.createElement("div");
  card.classList.add("card", "text-bg-primary", "mb-3");

  var cardBody = document.createElement("div");
  cardBody.classList.add("card-body");

  var cardText = document.createElement("p");
  cardText.classList.add("card-text");
  cardText.textContent = question;

  cardBody.appendChild(cardText);

  card.appendChild(cardBody);

  massage_container.appendChild(card);
}

function CardAnswere(answer) {
  //gib eine massagebox zurück

  var massage_container = document.getElementById("massage-container");

  var card = document.createElement("div");
  card.classList.add("card", "text-bg-success", "mb-3");

  var cardBody = document.createElement("div");
  cardBody.classList.add("card-body");

  var cardText = document.createElement("p");
  cardText.classList.add("card-text");
  cardText.textContent = answer;

  cardBody.appendChild(cardText);

  card.appendChild(cardBody);

  massage_container.appendChild(card);
}

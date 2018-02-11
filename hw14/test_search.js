var dataSet = [
  {
    datetime: "1/1/2010",
    city: "benton",
    state: "ar",
    country: "us",
    shape: "circle",
    durationMinutes: "5 mins.",
    comments: "4 bright green circles high in the sky going in circles then one bright green light at my front door."
  },
  {
    datetime: "1/2/2010",
    city: "bonita",
    state: "ca",
    country: "us",
    shape: "light",
    durationMinutes: "13 minutes",
    comments: "Three bright red lights witnessed floating stationary over San Diego New Years Day 2010"
  }
];



var $app = document.querySelector("#app");
var $date = document.querySelector("#date");
var $city = document.querySelector("#city");
var $state = document.querySelector("#state");
var $country = document.querySelector("#country");
var $shape = document.querySelector("#shape");
var $s_click = document.querySelector("#submit");

$s_click.addEventListener("click", click);

function click (event) {
  event.preventDefault();

  var tr_head = document.createElement("tr");
  var th = document.createElement("th");
  var thead=document.createElement("thead");
  var label=['Date','City','State','Country','Shape','Duration(min)','Comments'];
  var col=['datetime','city', 'state','country','shape','durationMinutes','comments'];
  for (let i=0;i<label.length;i++) {
    th.innerHTML=label[i];
    tr_head.appendChild(th);
    th = document.createElement("th");
  };
  thead.appendChild(tr_head);
  $app.appendChild(thead);

  var td = document.createElement("td");
  var tr = document.createElement("tr");
  var tbody=document.createElement("tbody");

  for (let i=0;i<dataSet.length;i++) {
    if (($date.value == '' || $date.value ==dataSet[i].datetime) &&
        ($city.value == '' || $city.value ==dataSet[i].city) &&
        ($state.value == '' || $state.value ==dataSet[i].state) &&
        ($country.value == '' || $country.value ==dataSet[i].country) &&
        ($shape.value == '' || $shape.value ==dataSet[i].shape)
) {
      for (let j=0;j<Object.keys(dataSet[i]).length;j++) {
        td.innerHTML = dataSet[i][col[j]];
        tr.appendChild(td);
        td=document.createElement("td");
      };
      tbody.appendChild(tr);
      tr = document.createElement("tr");
    };
  };
  $app.appendChild(tbody);
};

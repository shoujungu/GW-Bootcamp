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
    datetime: "1/1/2010",
    city: "bonita",
    state: "ca",
    country: "us",
    shape: "light",
    durationMinutes: "13 minutes",
    comments: "Three bright red lights witnessed floating stationary over San Diego New Years Day 2010"
  }
];


var search_click= document.querySelector("#app");
var s_date = document.querySelector("#date");





var app = document.querySelector("#app");

var tr_head = document.createElement("tr");
var th = document.createElement("th");
var thead=document.createElement("thead");
var col=['datetime','city', 'state','country','shape','durationMinutes','comments'];
for (let i=0;i<col.length;i++) {
  th.innerHTML=col[i];
  tr_head.appendChild(th);
  th = document.createElement("th");
};
thead.appendChild(tr_head);
app.appendChild(thead);

var td = document.createElement("td");
var tr = document.createElement("tr");
var tbody=document.createElement("tbody");
for (let i=0;i<dataSet.length;i++) {
  for (let j=0;j<Object.keys(dataSet[i]).length;j++) {
    td.innerHTML = dataSet[i][col[j]];
    tr.appendChild(td);
    td=document.createElement("td");
  };
  tbody.appendChild(tr);
  tr = document.createElement("tr");
};
app.appendChild(tbody);

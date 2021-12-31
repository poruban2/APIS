const api_location = 'https://zadanie-apis.herokuapp.com/read_locations';

const headers_loc = ['LocationID', 'Name', 'Address', 'Manager', 'Contact'];
//get
async function loadLocIntoTable(url, table, headers) {
    const tableHead = table.querySelector("thead");
    const tableBody = table.querySelector("tbody");
    const response = await fetch(url);
    const {Locations} = await response.json(); 

    tableHead.innerHTML = "<tr><tr/>";
    tableBody.innerHTML = "";

    
    for (const headerText of headers) {
        const headerElement = document.createElement("th");

        headerElement.textContent = headerText;
        tableHead.querySelector("tr").appendChild(headerElement)
    }

    for (const row of Locations) {
        const rowElement = document.createElement("tr");

        for (const cellText of row) {
            const cellElement = document.createElement("td");
            
            cellElement.textContent = cellText;
            rowElement.appendChild(cellElement);
        }

        tableBody.appendChild(rowElement);
    }
}

loadLocIntoTable(api_location, document.querySelector("table"), headers_loc);

//post
const myForm = document.getElementById('myForm');

myForm.addEventListener('submit', function (e) {
    e.preventDefault();

    const formData = new FormData(this);
    var container = document.getElementById("myFormUpdateDiv");
    container.style.visibility = 'visible';

    var object = formData;
    formData.forEach(function(value, key){
        object[key] = value;
    });
    var json = JSON.stringify(object);


    fetch('https://zadanie-apis.herokuapp.com/CreateLocations', {
        method: 'post',
        body: json
    }).then(function (response) {
        return response.text();
    }).then(function (text) {
        console.log(text);
    }).catch(function (error){
        console.error(error);
    })
});

//put
const myFormUpdate = document.getElementById('myFormUpdate');

myFormUpdate.addEventListener('submit', function (e) {
    e.preventDefault();

    const formData = new FormData(this);

    var object = formData;
    formData.forEach(function(value, key){
        object[key] = value;
    });
    var json = JSON.stringify(object);

    fetch('https://zadanie-apis.herokuapp.com/UpdateLocations/' + formData.get('ID'), {
        method: 'put',
        body: json
    }).then(function (response) {
        return response.text();
    }).then(function (text) {
        console.log(text);
    }).catch(function (error){
        console.error(error);
    })
});

//delete
const mySub = document.getElementById('delete');

mySub.addEventListener('submit', function (e) {
    e.preventDefault();

    const formData = new FormData(this);
    
    fetch('https://zadanie-apis.herokuapp.com/DeleteLocations/' + formData.get('deledLocID'), {
        method: 'DELETE'
    }).then(function (response) {
        return response.text();
    }).then(function (text) {
        console.log(text);
    }).catch(function (error){
        console.error(error);
    })
});




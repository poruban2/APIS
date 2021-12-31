
const api_extents = 'https://zadanie-apis.herokuapp.com/read_extents';
const api_amounts = 'https://zadanie-apis.herokuapp.com/read_amounts';

const headers_ext = ['ExtentID', 'Lenght', 'Width', 'Seedings'];
const headers_amo = ['ID', 'Quantity', 'Price', 'LocationID', 'ExtentID'];

//get
async function loadLocIntoTable(url, table, headers) {
    const tableHead = table.querySelector("thead");
    const tableBody = table.querySelector("tbody");
    const response = await fetch(url);
    const {Extents} = await response.json(); 

  
    tableHead.innerHTML = "<tr><tr/>";
    tableBody.innerHTML = "";

    
    for (const headerText of headers) {
        const headerElement = document.createElement("th");

        headerElement.textContent = headerText;
        tableHead.querySelector("tr").appendChild(headerElement)
    }

    for (const row of Extents) {
        const rowElement = document.createElement("tr");

        for (const cellText of row) {
            const cellElement = document.createElement("td");
            
            cellElement.textContent = cellText;
            rowElement.appendChild(cellElement);
        }

        tableBody.appendChild(rowElement);
    }
}

async function loadLocIntoTable2(url, table, headers) {
    const tableHead = table.querySelector("thead");
    const tableBody = table.querySelector("tbody");
    const response = await fetch(url);
    const {Amounts} = await response.json(); 


    tableHead.innerHTML = "<tr><tr/>";
    tableBody.innerHTML = "";

    
    for (const headerText of headers) {
        const headerElement = document.createElement("th");

        headerElement.textContent = headerText;
        tableHead.querySelector("tr").appendChild(headerElement)
    }

    for (const row of Amounts) {
        const rowElement = document.createElement("tr");

        for (const cellText of row) {
            const cellElement = document.createElement("td");
            
            cellElement.textContent = cellText;
            rowElement.appendChild(cellElement);
        }

        tableBody.appendChild(rowElement);
    }
}


loadLocIntoTable(api_extents, document.querySelector(".table"), headers_ext);
loadLocIntoTable2(api_amounts, document.querySelector(".table2"), headers_amo);

//post

const myFormPost = document.getElementById('form-post');

myFormPost.addEventListener('submit', function (e) {
    e.preventDefault();

    const formData = new FormData(this);
    var container = document.getElementById("form-div-post");
    container.style.visibility = 'visible';

    var object = formData;
    formData.forEach(function(value, key){
        if (key != "Seedlings"){
            object[key] = parseInt(value);
        }
        else{
            object[key] = value;
        }
    });
    var json = JSON.stringify(object);
    console.log(object)

    fetch('https://zadanie-apis.herokuapp.com/CreateExtents', {
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

const postForm2 = document.getElementById('formPost2');

postForm2.addEventListener('submit', function (e) {
    e.preventDefault();

    const formData = new FormData(this);
    var container = document.getElementById("formDivPost2");
    container.style.visibility = 'visible';

    var object = formData;
    formData.forEach(function(value, key){
        object[key] = parseInt(value);
    });
    var json = JSON.stringify(object);

    console.log(object)
    fetch('https://zadanie-apis.herokuapp.com/CreateAmounts', {
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

const myFormUpdate = document.getElementById('formPut');

myFormUpdate.addEventListener('submit', function (e) {
    e.preventDefault();

    const formData = new FormData(this);

    var object = formData;
    formData.forEach(function(value, key){
        object[key] = parseInt(value);
    });
    var json = JSON.stringify(object);

    fetch('https://zadanie-apis.herokuapp.com/UpdateExtents/' + formData.get('ExtentID'), {
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

const myFormUpdate2 = document.getElementById('formPut2');

myFormUpdate2.addEventListener('submit', function (e) {
    e.preventDefault();

    const formData = new FormData(this);

    var object = formData;
    formData.forEach(function(value, key){
        if (key != "Seedlings"){
            object[key] = parseInt(value);
        }
        else{
            object[key] = value;
        }
    });
    var json = JSON.stringify(object);

    fetch('https://zadanie-apis.herokuapp.com/UpdateAmounts/' + formData.get('AmountID'), {
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
const deleteTab = document.getElementById('delete');

deleteTab.addEventListener('submit', function (e) {
    e.preventDefault();

    const formData = new FormData(this);
    
    fetch('https://zadanie-apis.herokuapp.com/DeleteExtents/' + formData.get('ExtentId'), {
        method: 'DELETE'
    }).then(function (response) {
        return response.text();
    }).then(function (text) {
        console.log(text);
    }).catch(function (error){
        console.error(error);
    })
});

const deleteTab2 = document.getElementById('delete2');

deleteTab2.addEventListener('submit', function (e) {
    e.preventDefault();

    const formData = new FormData(this);
    
    fetch('https://zadanie-apis.herokuapp.com/DeleteAmounts/' + formData.get('AmountID'), {
        method: 'DELETE'
    }).then(function (response) {
        return response.text();
    }).then(function (text) {
        console.log(text);
    }).catch(function (error){
        console.error(error);
    })
});

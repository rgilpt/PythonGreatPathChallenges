function printPerson(personObject) {
    // Create the list element:

    //something
    let data = document.createElement('div');


    let name = document.createElement('p');
    let node = document.createTextNode(personObject.first_name + " " + personObject.surname);
    let node2 = document.createTextNode("Hello");
    let p2 = document.createElement('p');
    p2.appendChild(node2);
    name.appendChild(node);
    data.appendChild(name);
    data.appendChild(p2);



    let age = document.createElement('p');
    node = document.createTextNode(personObject["rate_interest"]);
    age.appendChild(node);
    data.appendChild(age);


    return data;
}

async function getResponse() {
	const response = await fetch(
		'http://127.0.0.1:8000/students/',
		{
			method: 'GET',
		}
	);
	if (!response.ok) {
		throw new Error("HTTP error! status: ${response.status}");
	}
	const data = await response.json();
	console.log(data);

	for(let i = 0; i < data.length; i++) {
	    document.getElementById('data').appendChild(printPerson(data[i]));
	}
}
getResponse();



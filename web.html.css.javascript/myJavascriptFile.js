function printPerson(personObject) {
    // Create the list element:

    //something
    let data = document.createElement('div');

    let name = document.createElement('p');
    let node = document.createTextNode(personObject.first_name + " " + personObject.surname);
    name.appendChild(node);
    data.appendChild(name);

    let age = document.createElement('p');
    node = document.createTextNode(personObject["rate_interest"]);
    age.appendChild(node);
    data.appendChild(age);


    return data;
}

async function getResponse() {
	const response = await fetch(
		'http://192.168.1.131:8000/students/',
		{
			method: 'GET',
		}
	);
	if (!response.ok) {
		throw new Error(`HTTP error! status: ${response.status}`);
	}
	const data = await response.json();
	console.log(data);
	for(let i = 0; i < 3; i++) {
	    document.getElementById('data').appendChild(printPerson(data[i]));
	}
}
getResponse()



function printPerson(personObject) {
    // Create the list element:

    //something
    let data = document.createElement('div');

    let name = document.createElement('p');
    let node = document.createTextNode(personObject.name + " " + personObject.surname);
    name.appendChild(node);
    data.appendChild(name);

    let age = document.createElement('p');
    node = document.createTextNode(personObject["age"]);
    age.appendChild(node);
    data.appendChild(age);

/
    return data;
}
let person = {
    name : "James",
    surname : "Done",
    age : 42
}
document.getElementById('data').appendChild(printPerson(person));


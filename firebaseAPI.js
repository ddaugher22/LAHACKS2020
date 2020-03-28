// reference to database service
const database = firebase.database();

//Categories
// 1. atHome
// 2. goOutside

//Listeners for buttons

const atHomeButton = document.getElementById('atHomeSuggestion');
const outsideButton = document.getElementById('outsideSuggestion');

atHomeButton.addEventListener('click', (e) => {
    e.preventDefault();
    getSuggestion('home');
});
outsideButton.addEventListener('click', (e) => {
    e.preventDefault();
    getSuggestion('outside');
});


function addSuggestion(category, suggestion) {
    database.ref('/categories/' + category).push(suggestion);
}

function getSuggestion(category) {

    var ref = firebase.database().ref('/categories/' + category);
    var suggestion; 

    ref.once("value").then(function(snapshot) {
        updateSuggestion(getRandomSuggestion(snapshot));
        
    }, function (error) {
        console.log("Error: " + error.code);
    });
    
}

function getRandomSuggestion(snapshot) {

    var suggestion = "";

    var rand = Math.floor(Math.random()*snapshot.numChildren());

    var count = 0;
    var suggestion = "";

    snapshot.forEach(function (childSnapshot) {

        if (count == rand) {
            suggestion = childSnapshot.val();
        }
        count++;
    });

    return suggestion;
}

function updateSuggestion(suggestion) {
    document.getElementById("suggestionText").textContent = suggestion;
}

console.log(getSuggestion('home'));
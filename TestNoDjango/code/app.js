//variables

const btn = document.getElementById('btn');
const quote = document.getElementById('quote');
const author = document.getElementById('author');

// let url ="https://codingaddictla.github.io/random-quotes/quotes.json";
let url ="https://api.paperquotes.com/apiv1/quotes/?tags=love,life&curated=1";
//let url = "https://api.paperquotes.com/apiv1/quotes/?tags=love,life&curated=1 -H 'Authorization:57173bd7dbb33566d4685dd0c307624d2aa84355";
//curl -X GET -H "Authorization: Token {57173bd7dbb33566d4685dd0c307624d2aa84355}" "https://api.paperquotes.com/apiv1/quotes/?tags=love,life&curated=1"


btn.addEventListener('click',getData);

function getData() {
	
	fetch(url)
	
	.then(function (data) {
		return data.json();
	}).then(function (quotes) {
		
		let number = Math.floor(Math.random() * quotes.length);
		
		quote.innerHTML = '<span>"</span>' + quotes[number].quote + '<span>"</span>';
		author.innerHTML = '<span>---</span>' + quotes[number].author;
		
	})
	.catch(function (error) {
		//if there is an error
	});
	
}
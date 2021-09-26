let letters = []; //this is our stack
	let word = 'racecar';
	let rword = ''

	// put letters of word into stack/array
	for (let i = 0; i < word.length; i++){
		letters.push(word[i]);
	}
	console.log(letters)
	//pop off the stack in reverse order
	for (let i = 0; i < word.length; i++){
		rword += letters.pop(); // rword = rword + letters.pop()
	}
	console.log(rword)

	if (rword === word){
		console.log(word + " is a palindrome");
	}
	else{
		console.log(word + " is not a palindrome");
	}
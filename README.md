# Cryptosystems

This project is a python implementation of three Cryptosystems namely Affine, Transposition and RSA Encryptions. 

## Affine Encryption

### Instructions

	To run the affine encryption or decryption:

	1. Choose 1 from the start menu 
	2. Then enter 1 for encryption and 2 for decryption 
      3. After choosing either enter the message to be encrypted and
	4. Finally enter a key to encrypt the message with where key is an integer.

### Concepts Used

	The affine encryption uses the formula
			f(X)=(aX+b)mod26
		For the function to be a bijection,
		gcd(a,26)=1, and "a" is a positive integer less than 26,
		so the possible values for "a" are odd numbers below 26 except 13""")


	In the affine encryption a string and a key are 
	taken as input, and are processed in either of two ways; encryption or decryption.
	For encryption, the letters of the alphabet are mapped to the numbers 0 to 25, 
	for example A is 0, b is 2, C is 2 and so on.
	Then by substituting the values for "X" and using the formula, we produce a new
	map for each character in the string.

	After assigning the new mapping, the characters in the string are taken one by 
	one and translated back to alphabets using the original mapping; thus finishing 
	the encryption process.

	For decryption we take each character in the string and map them using the 
	original map values, using the inverse modulo dictionary and solving
				
					X=((c-b)*inverseA)mod26 
			
	c - is the values in the string we mapped inverseA - is the inverse modulo of "a" 
	listed in the inverse modulo dictionary we provided.

	we produce a new map for each character in the string. Which are then translated 
	back to alphabets using the original mapping; thus finishing the decryption process.

	Since the affine encryption uses a relatively simple algorithm, it can only encrypt 
	or decrypt stirngs of alphabets; so numbers and blank spaces are ingnored.

### Why does it work?

	The encryption works because for given possible values of "a", the formula produces 
	a bijective mapping of the alphabet. Since gcd(a,26)=1 there will be no repeated values.
	The decryption works because the a mod26 gives us a number from 0 to 25 everytime, which 
	the range of our alphabet mapping; hence enabling us to decrypt the messages.



## Transposition Encryption

### Instructions

	To run the Transposition encryption or decryption:

	1. Choose 2 from the start menu 
	2. Then enter 1 for encryption and 2 for decryption 
      3. After choosing either 1 or 2 enter the message to be encrypted or decrypted and
	4. Finally enter a key to encrypt the message with where key is 
	   a single word or a sequence of positive integers separated by whitespace.

### Concepts Used

	The transposition cipher takes an argument of the message to be encrypted and the key for the encryption. 
	The message is a string but the key is a function that maps the message to the new and encrypted message 
	with permutation. This is how the function is represented by the key... [m1,m2,m3...mn] implies that
	f(1)=m1, f(2)=m3... or in other words the first element is moved to the (m1)th position and the second 
	element to the (m2)th position for each block.

	This transpostion cypher has an extra feature in which a word can also be used as a key. This works where
	the word is changed to a list of positive integers as above and the encryption continues from there. For
	example the word 'plan' can be converted to the list [4,2,1,3] since 'p' is the the 4th of the 4 letters 
	in the word based on the alphabet order and 'l' the 2nd 'a' the first and finally 'n' 3rd.

	

### Why does it work?

	When the a message is encrypted with the transposition cypher the message is rearranged by the effect of 
	the function F. Since this rearranged message is different from the original message it is indeed
	encrypted regardless of the degree of secureness. When the encrypted message is decrypted the inverse	
	of F or F^-1 is used and this guarentees that we get the original message from the encrypted message.

## RSA Encryption

### Instructions

	To run the RSA encryption or decryption:

	1. Choose 3 from the start menu 
	2. Then enter 1 for encryption and 2 for decryption 
      3. After choosing either 1 or 2 enter the message to be encrypted or decrypted and
	4. Finally enter a public key or private key to encrypt or decrypt the message respectively. The 'n' and 'e' values 
	are entered separated by white space and the 'n' and 'd' values the same way for decryption.

### Concepts Used

	To encrypt the message the formula em = m^(e)modn is used and for decryption the m = (em)^(d)modn is used.
	When dividing the message into blocks of equal size a concept from our book is used which is this string or
	message into equally sized blocks of 2N digits, where 2N is the largest even number such that the number 
	2525... 25 with 2N digits does not exceed n. For instance for a value of 2537 as our 'n' the string is 
	divided into blocks of size for it is the size of 2525 since 2525 < 2537 < 252525.

	And as was illustrated by example in our textbook the encryption program takes a string of alphabets as a 
	message input and outputs the encrypted message as string of  numbers and the decryption program takes a 
	string of numbers as an input and outputs the decrypted string of alphabets.

	And finally the program works for 'n' values greater than 25 since for n values less than 26 the encryption values
	are not unique for the 26 letters.

### Why does it work?
	An encryption's correcteness is proved by showing the decryption of the encrypted text yields 
	the original text.

	Hence the plaintext message can be quickly recovered from a ciphertext message when the decryp-
	tion key d, an inverse of e modulo (p − 1)(q − 1), is known. This can be shown since 
	if de ≡ 1 (mod (p − 1)(q − 1)), there is an integer k such that de = 1 + k(p − 1)(q − 1). It follows that
	c^d ≡ (m^e)^d = m^de = m^(1+k(p−1)(q−1))(mod n).

	By Fermat’s little theorem, it follows that m^(p−1) ≡ 1 (mod p) and m^(q−1) ≡ 1 (mod q).
	Consequently, c^d ≡ m ⋅ (m^(p−1))^(k(q−1)) ≡ m ⋅ 1 = m (mod p)

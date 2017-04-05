
class myHashTable:
	def __init__(self):
		self.value = ''

	def hashed(self, value):
		# assume value is a string
		# return hashed value
		self.value = value
		lower = self.value.lower()
		return ord(lower[0]) - 97;

	def hashedSS(self, value):
		# return first 3 digits of SS#
		return(value[:3])

	def hashedMult(self, value):
		# return first letters of first & last name, hashed value multiplied
		self.value = value
		value = value.lower()
		sepName = value.split(" ")
		firstName = sepName[0]
		middleName = sepName[1]
		lastName = sepName[2]
		firstLet_firstName = firstName[0] 
		firstLet_middleName = middleName[0]
		firstLet_lastName = lastName[0]
		firstHashedVal = ord(firstLet_firstName) - 97
		secondHashedVal = ord(firstLet_middleName) - 97
		thirdHashedVal = ord(firstLet_lastName) - 97
		return firstHashedVal * secondHashedVal * thirdHashedVal
		# cleaner method
		words = value.split()
		first_letters = []

		for word in words:
			first_letter = word[0]
			first_letters.append(first_letter.lower())

		alphabet_indices = []
		alphabet = 'abcdefghijklmnopqrstuvwxyz'

		for letter in first_letters:
			alphabet_indices.append(alphabet.index(letter))

		product = alphabet_indices[0]

		for i in range (1, len(alphabet_indices)):
			product *= alphabet_indices[i]
		return product

thing = myHashTable()
print thing.hashed('apple')
print thing.hashedSS('12344567')
print thing.hashedMult('Justin Emeka Uzo')



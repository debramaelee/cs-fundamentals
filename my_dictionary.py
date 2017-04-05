class myDictionary:
	def __init__(self):
		self.keys = []
		self.values = []


	def insert_element(self, key, element):
		#insert element into dictionary
		self.keys.append(key)
		self.values.append(element)

	def find_element(self, key):
		# finds element associated with key
		# returns None of key doesn't exist
		for i in range(len(self.keys)):
			if key == self.keys[i]:
				return self.values[i]
				break
			else:
				return None

	def remove_element(self, key):
		# finds element associated with key
		# remove element if it is found
		for i in range(len(self.keys)):
			if key == self.keys[i]:
				del self.values[i]
				del self.keys[i]

	def keys(self):
		# returns all keys
		return self.keys

	def elements(self):
		# returns all elements
		return self.values

	def isEmpty(self):
		# returns if the list is empty
		return self.size() == 0
		# shorthand way of returning true/false


	def size(self):
		# returns size of element list
		return len(self.values)



dictionary = myDictionary()
dictionary.insert_element('email','tamby@hirewire.com')
dictionary.insert_element('password', 'chickennuggets')
dictionary.insert_element('phone', '12345680')

for key in dictionary.keys():
	print(key)
	print(dictionary.find_element(key))

child_dictionary = myDictionaryIO
child_dictionary.insert 

if dictionary.find_element('email') == 'tamby@hirewire.com':
	print('yay')
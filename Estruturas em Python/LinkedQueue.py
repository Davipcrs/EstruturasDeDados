class Node():
	def __init__(self, element):
		self.element = element
		self.next = None
		self.prev = None



class Linked_queue(Node):
	def __init__(self):
		self.head = Node(None)
		self.head.next = None
		self.size = 0
		
		
	def create_list(self, element):
		self.head.element = element
		self.head.next = None
		self.size = 1
		
	def destroy_list(self):
		self.head.element = None
		self.head.next = None
		self.head = None
		self.size = 0
			

	def __len__(self):
		return self.size
		#utilizao da funçao len do python	
			
	def verify_list(self):
	    if self.head.element != None:
		    return "List exist"
			##raise error
			
	    else:
		    return "List do not exist"
			##raise error
			
	##def index_list():
        #criar indexao

	def remove_element_list(self):
		aux_pointer = self.head.next
		self.head = None
		self.head = aux_pointer
		self.size = self.size - 1


	
	def add_element_list(self, element):
		aux_node = Node(element)
		aux_pointer = self.head
		while aux_pointer.next:
			aux_pointer = aux_pointer.next
		aux_pointer.next = aux_node
		self.size = self.size + 1
			
		

	def search_index(self, index):
		aux_pointer = self.head

		if index <= self.size:
			for i in range(int(index)):
				aux_pointer = aux_pointer.next
			return aux_pointer.element
		else:
			print("deu erro!")

	def search_element(self, element):
		aux_pointer = self.head
		counter = 0

		for i in range(self.size):
			if aux_pointer.element == element:
				counter = counter + 1
				return i
				#conferir se roda para elementos repetidos!!!
			aux_pointer = aux_pointer.next
		
		if counter == 0:
			return "Element do not exist in the list"

	def modify_element(self, index, new_element):
		aux_pointer = self.head

		if index <= self.size:
			for i in range(int(index)):
				aux_pointer = aux_pointer.next
			aux_pointer.element = new_element

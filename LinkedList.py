class Node():
	def __init__(self, element):
		self.element = element
		self.next = None
    
    
    
class Linked_list(Node):
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
		#utilizacao da funcao len do python	
			
	def verify_list(self):
	    if self.head.element != None:
		    return "List exist"
			##raise error
			
	    else:
		    return "List do not exist"
			##raise error
			
	##def index_list():
        #criar indexao

	def remove_element_list(self, index):
		aux_pointer = self.head

		if index == 0:
			if self.head.next != None:
				self.head = self.head.next
				self.size = self.size - 1
			else:
				self.head = None
				self.size = 0
		elif index <= self.size:
			for i in range(int(index)):
				
				aux_pointer = aux_pointer.next
			if aux_pointer.next != None:
				
				aux_pointer = aux_pointer.next
				
				self.size = self.size - 1
			else:
				aux_pointer = None
				self.size = self.size - 1

	
	def add_element_list(self, element, index):
		aux_node = Node(element)
		aux_pointer = self.head
		aux_pointer2 = self.head

		if index == 0:
			aux_node.next = self.head
			self.head = aux_node
			self.size = self.size + 1

		elif index == 1:
			aux_pointer = aux_node
			self.head.next = aux_pointer
			self.size = self.size + 1

		elif index < self.size:
			for i in range(int(index)):
				aux_pointer = aux_pointer2 #ex: pos 0
				
				aux_pointer2 = aux_pointer.next #ex: pos 1

			
			
			aux_node.next = aux_pointer2
			aux_pointer.next = aux_node
			self.size = self.size + 1
			

		elif index == self.size:
			while aux_pointer.next:
				aux_pointer = aux_pointer.next
			aux_pointer.next = aux_node
			self.size = self.size + 1
			
		else:
			print("deu erro!")
			#raise error


        	#adicionar o elemento em qualquer posio da lista

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

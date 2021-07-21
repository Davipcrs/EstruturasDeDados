class Modifing_lists(Linked_list, Linked_queue, Linked_stack, Double_Linked_list):
	def concatenation(self, L1, L2):
		aux_pointer_L1 = L1.head
		for i in range(len(L2)):
			for j in range(len(L1)):
				aux_pointer_L1 = aux_pointer_L1.next
			L1.add_element_list(L2.search_index(i), j)
	
		return L1
	def sorting_list(self, L1):
		aux_pointer = L1.head
		lower_number = L1.search_index(0)
		sorted_list = Linked_list()
		pos = 0
		for i in range(len(L1)):
			for i in range(len(L1)):
				if lower_number >= L1.search_index(i):
					lower_number = L1.search_index(i)
					pos = i
			sorted_list.add_element_list(lower_number, i)
			L1.remove_element_list(pos)

		
		return sorted_list


	def invert_stack(self, P1):
		aux_pointer = P1.top
		P2 = Linked_stack()
		while P1.top:
			P2.add_element_list(P1.top.element)
			P1.remove_element_list()
		return P2

		##F(n) = n

	def compare_stack(self, P1, P2):
		aux_pointer1 = P1.top
		aux_pointer2 = P2.top
		counter = 0

		for i in range(len(P1)):
			if aux_pointer1.element == aux_pointer2.element:
				counter = counter + 1
			aux_pointer1 = aux_pointer1.next
			aux_pointer2 = aux_pointer2.next


		if counter == len(P1) and counter == len(P2):
			return "SIM"

		else:
			return "NaO"

		
	
	def parentesis(self, P1):
		counter1 = 0
		counter2 = 0
		while P1.top:
			if P1.top.element == '(':
				counter1 = counter1 + 1

			elif P1.top.element == ')':
				counter2 = counter2 + 1

			P1.remove_element_list()


		if counter1 == counter2:
			return "Correto"

		else:
			return "Incorreto"

	def sorting_using_stack(self, L1):
		P1 = Linked_stack()
		P2 = Linked_stack()
		aux_pointer = L1.head
		lower_number = L1.search_index(0)
		pos = 0
		for i in range(len(L1)):
			lower_number = L1.search_index(0)
			for i in range(len(L1)):
				if lower_number >= L1.search_index(i):
					lower_number = L1.search_index(i)
					pos = i
			P1.add_element_list(lower_number)

		for i in range(len(P1)):
			P2.add_element_list(P1.top)
			P1.remove_element_list()

		return P2

		#F(n) = n^3
	

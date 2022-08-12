class Node():
    def __init__(self, element):
        self.element = element
        self.next = None
        self.index = None



class halfLinkedList():
    def __init__(self):
        self.head = Node(None)
        self.size = None
        self.half = self.head
        self.navigator = self.half
        self.endNode = self.head
        
        
    def create_list(self, element):
        self.head = Node(element)
        self.size = 1
        self.half = self.head
        self.endNode = self.head
        self.setIndex()


    def destructList(self):
        self.head = None
        self.size = None
        self.half = None
        self.navigator = None
        self.endNode = None

    ##Implementar um EndNode aqui para diminuir o tempo de adição
    def addElementEnd(self, element):
        if self.head.next == None:
            self.head.next = Node(element)
            self.endNode = self.head.next
            
        else:
            self.navigator = self.half
            while self.navigator.next != None:
                self.navigator = self.navigator.next

            self.navigator.next = Node(element)

        self.size =+ 1

        self.getHalfList()


    def addElementHalf(self, element):
        self.navigator = self.half
        auxSave = self.half.next
        auxNode = Node(element)
        auxNode.next = auxSave
        self.half.next = auxNode


        self.size =+ 1
        
        self.getHalfList()
        
    def addElementHead(self, element):
        self.navigator = self.head
        self.head = Node(element)
        self.head.next = self.navigator

        self.size =+ 1

        self.getHalfList()


    def setIndex(self):
        indexAux = 0
        whileAux = 0

        self.head.index = 0
        self.navigator = self.head

        while whileAux != self.size:
            self.navigator.index = None
            if self.navigator.index == None:
                self.navigator.index = indexAux

            self.navigator = self.navigator.next
            indexAux =+ 1    

        return self.navigator

    def getHalfList(self):
        self.setIndex()
        aux = self.size / 2
        int(aux)
        self.navigator = self.half

        while self.navigator.index != aux:
            aux =+ 1

        self.half = self.navigator

    def indexConsult(self, auxIndex):
        if auxIndex >= self.size/2:
            self.navigator = self.half
            while self.navigator.index != auxIndex:
                self.navigator= self.navigator.index

        else:
            self.navigator = self.head
            while self.navigator.index != auxIndex:
                self.navigator = self.navigator.next

        return self.navigator.element


    def verifyList(self):
        if self.head == None:
            return "Lista falsa, não existe ponto inicial", self.destructList()

        if self.size == None:

            self.setSize()
            #criar função pra setar o size

        if self.half == None:
            self.getHalfList()

        return True

    def setSize(self):
        self.navigator = self.head
        self.size = 1
        while self.navigator.next != None:
            self.size =+ 1
            self.navigator = self.navigator.next


    def getMax(self):
        self.navigator = self.head
        auxMax = self.navigator.element

        while self.navigator != None:
            if auxMax <= self.navigator.element:
                auxMax = self.navigator.element

            self.navigator = self.navigator.next

        return auxMax



    ##algoritmo para colocar em ordem crescente a lista
    ## descobrir como fazer isso
    ##def cOrder(self, head):
    ##    while head != None:
            

        
        


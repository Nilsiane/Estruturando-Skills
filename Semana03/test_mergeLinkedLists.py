
import pytest
from linkedlist import *

def mergeLinkedLists(linkedList_one, linkedList_two):
    
    #Primeiramente, verifica qual das duas listas começa com o menor elemento.
    #Pois como as listas estão ordenadas, começar com a menor faz sentido, facilita a ordenação
    #Se a lista 2 começar com elementos mais altos, ela se torna a lista 1.
    
    if linkedList_one.head.data > linkedList_two.head.data:
        temp = linkedList_one
        linkedList_one = linkedList_two
        linkedList_two = temp 
    
    #Guarda o tamanho da soma das listas
    len_aux = linkedList_one.length + linkedList_two.length
    
    #Cria os nó com que iremos trabalhar. Nós atuais da lista 1 e 2
    #Os nós recebem o head de cada lista
    current_node_one = linkedList_one.head
    current_node_two = linkedList_two.head
    prev_node = None #Cria um terceiro nó, que recebe o nó anterior ao atual, por enquanto está vazio

    while current_node_one is not None and current_node_two is not None: #Percorre as duas listas ao mesmo tempo.
           
        #Verifica se o elemento nó atual da lista 1 é menor ou igual ao da lista 02, se sim, apenas "andamos" na lista
        if current_node_one.data <= current_node_two.data:
            prev_node = current_node_one
            current_node_one = current_node_one.next
        #caso contrário...
        else:   
            prev_node.next = current_node_two     #nó anterior ao analizado vai apontar para o nó atual 02
            current_node_two = current_node_two.next #o nó atual 02 vai ser atualizado para o seguinte
            prev_node.next.next = current_node_one   #Coloca o nó 01 atual depois do nó que acabou de ser adicionado
            prev_node = prev_node.next  #atualiza prev_node para o próximo nó da lista resultante (que é o recem adicionado).
        
        #Se a lista 01 for menor que a 02, ela terminarar a interação e ainda sobrarão elementos em 02
        #Neste caso, precisamos adicionar os elementos restantes da lista 02 a lista 01
        
        if current_node_one is None:
            linkedList_one.tail.next = current_node_two #A cauda da lista 01 vai apontar para nó 2 atual
            current_node_two.prev = linkedList_one.tail # O nó 02 vai ter um ponteiro aprontando para a cauda
                                                        #Assim mantendo a dupla ligação
            linkedList_one.tail = linkedList_two.tail   # por fim, fazemos a cauda da lista 02 se tornar a da 01 
    
    linkedList_one.length = len_aux
    return linkedList_one

@pytest.fixture(scope="session")
def data():
    
    array = []
    
    # test 1 data
    array.append([[2,6,7,8],[1,3,4,5,9,10]])
    
    # test 2 data
    array.append([[1,2,3,4,5],[6,7,8,9,10]])

    # test 3 data
    array.append([[6,7,8,9,10],[1,2,3,4,5]])

    # test 4 data
    array.append([[1,3,5,7,9],[2,4,6,8,10]])

    # test 5 data
    array.append([[0,1,2,3,4,5,7,8,9,10],[6]])

    # test 6 data
    array.append([[6],[0,1,2,3,4,5,7,8,9,10]])

    # test 7 data
    array.append([[1],[2]])

    # test 8 data
    array.append([[2],[1]])

    # test 9 data
    array.append([[1,1,1,3,4,5,5,5,10],[1,1,2,2,5,6,10,10]])
   
    return array

def test_1(data):
    """
    Test evaluation for [[2,6,7,8],[1,3,4,5,9,10]]
    """
    linkedlist_one = LinkedList()
    for item in data[0][0]:
        linkedlist_one.append(item)

    linkedlist_two = LinkedList()
    for item in data[0][1]:
        linkedlist_two.append(item)

    linkedlist_test = LinkedList()
    for item in [1,2,3,4,5,6,7,8,9,10]:
        linkedlist_test.append(item)
  
    assert mergeLinkedLists(linkedlist_one, linkedlist_two) == linkedlist_test
def test_2(data):
    """
    Test evaluation for [[1,2,3,4,5],[6,7,8,9,10]]
    """
    linkedlist_one = LinkedList()
    for item in data[1][0]:
      linkedlist_one.append(item)

    linkedlist_two = LinkedList()
    for item in data[1][1]:
      linkedlist_two.append(item)

    linkedlist_test = LinkedList()
    for item in [1,2,3,4,5,6,7,8,9,10]:
      linkedlist_test.append(item)

    assert mergeLinkedLists(linkedlist_one, linkedlist_two) == linkedlist_test

def test_3(data):
    """
    Test evaluation for [[6,7,8,9,10],[1,2,3,4,5]]
    """
    linkedlist_one = LinkedList()
    for item in data[2][0]:
      linkedlist_one.append(item)

    linkedlist_two = LinkedList()
    for item in data[2][1]:
      linkedlist_two.append(item)

    linkedlist_test = LinkedList()
    for item in [1,2,3,4,5,6,7,8,9,10]:
      linkedlist_test.append(item)

    assert mergeLinkedLists(linkedlist_one, linkedlist_two) == linkedlist_test

def test_4(data):
    """
    Test evaluation for [[1,3,5,7,9],[2,4,6,8,10]]
    """
    linkedlist_one = LinkedList()
    for item in data[3][0]:
      linkedlist_one.append(item)

    linkedlist_two = LinkedList()
    for item in data[3][1]:
      linkedlist_two.append(item)

    linkedlist_test = LinkedList()
    for item in [1,2,3,4,5,6,7,8,9,10]:
      linkedlist_test.append(item)

    assert mergeLinkedLists(linkedlist_one, linkedlist_two) == linkedlist_test

def test_5(data):
    """
    Test evaluation for [[0,1,2,3,4,5,7,8,9,10],[6]]
    """
    linkedlist_one = LinkedList()
    for item in data[4][0]:
      linkedlist_one.append(item)

    linkedlist_two = LinkedList()
    for item in data[4][1]:
      linkedlist_two.append(item)

    linkedlist_test = LinkedList()
    for item in [0,1,2,3,4,5,6,7,8,9,10]:
      linkedlist_test.append(item)

    assert mergeLinkedLists(linkedlist_one, linkedlist_two) == linkedlist_test

def test_6(data):
    """
    Test evaluation for [[6],[0,1,2,3,4,5,7,8,9,10]]
    """
    linkedlist_one = LinkedList()
    for item in data[5][0]:
      linkedlist_one.append(item)

    linkedlist_two = LinkedList()
    for item in data[5][1]:
      linkedlist_two.append(item)

    linkedlist_test = LinkedList()
    for item in [0,1,2,3,4,5,6,7,8,9,10]:
      linkedlist_test.append(item)

    assert mergeLinkedLists(linkedlist_one, linkedlist_two) == linkedlist_test

def test_7(data):
    """
    Test evaluation for [[1],[2]]
    """
    linkedlist_one = LinkedList()
    for item in data[6][0]:
      linkedlist_one.append(item)

    linkedlist_two = LinkedList()
    for item in data[6][1]:
      linkedlist_two.append(item)

    linkedlist_test = LinkedList()
    for item in [1,2]:
      linkedlist_test.append(item)

    assert mergeLinkedLists(linkedlist_one, linkedlist_two) == linkedlist_test

def test_8(data):
    """
    Test evaluation for [[2],[1]]
    """
    linkedlist_one = LinkedList()
    for item in data[7][0]:
      linkedlist_one.append(item)

    linkedlist_two = LinkedList()
    for item in data[7][1]:
      linkedlist_two.append(item)

    linkedlist_test = LinkedList()
    for item in [1,2]:
      linkedlist_test.append(item)

    assert mergeLinkedLists(linkedlist_one, linkedlist_two) == linkedlist_test

def test_9(data):
    """
    Test evaluation for [[1,1,1,3,4,5,5,5,10],[1,1,2,2,5,6,10,10]]
    """
    linkedlist_one = LinkedList()
    for item in data[8][0]:
      linkedlist_one.append(item)

    linkedlist_two = LinkedList()
    for item in data[8][1]:
      linkedlist_two.append(item)

    linkedlist_test = LinkedList()
    for item in [1,1,1,1,1,2,2,3,4,5,5,5,5,6,10,10,10]:
      linkedlist_test.append(item)

    assert mergeLinkedLists(linkedlist_one, linkedlist_two) == linkedlist_test

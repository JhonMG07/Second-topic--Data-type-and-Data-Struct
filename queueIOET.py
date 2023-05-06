from queue import Queue

# create a queue

my_queue = Queue()

# Add element to the queue
my_queue.put("a")
my_queue.put("b")
my_queue.put("c")

# print the queue
print("Cola inicial:", my_queue.queue)

# save and eliminate the first element 
# el get sirve para hacer pop

first_element = my_queue.get()
print("Primer elemento:", first_element)
print("Cola después de obtener el primer elemento:", my_queue.queue)

# Add the new elemento to the queue
my_queue.put("d")
print("Cola después de agregar un nuevo elemento:", my_queue.queue)

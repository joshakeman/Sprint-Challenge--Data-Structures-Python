class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    self.storage.insert(0, item)
    # self.get()
    # print(self.storage)

    return_list = []
    for i in range(len(self.storage)):
      # print (self.storage[i])
      if self.storage[i] != None:
        # print("true")
        return_list.append(self.storage[i])
      else:
        break
    self.storage.pop()
    return_list.reverse()
    return return_list

  def get(self):

    return_list = []
    for i in range(len(self.storage)):
      # print (self.storage[i])
      if self.storage[i] != None:
        # print("true")
        return_list.append(self.storage[i])
      else:
        break
    self.storage = return_list
    return_list.reverse()
    return return_list


# thing = RingBuffer(5)

# print(thing.append('a'))
# print(thing.append('b'))
# print(thing.get())

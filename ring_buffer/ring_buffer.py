class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    
    # print(self.storage)
    temp = self.get()
    # temp = self.storage

    if len(temp) < 5:
      temp.append(item)
      self.storage = temp + [None]*(5-len(temp))
    elif len(temp) == 5:
      print(self.current)
      temp[self.current] = item
      # temp.pop()
      self.storage = temp
      self.current += 1
      # if self.current < self.capacity:
      #   self.current + 1
      # else:
      #   self.current = 0

    return temp
    # temp = self.get()

    # if len(temp) < 5:
    #   temp.append(item)
    #   self.storage.append(item)
    #   self.storage.pop()
    #   print(self.storage)
    # return temp 

    # # self.get()
    # # print(self.storage)

    # return_list = []
    # for i in range(len(self.storage)):
    #   # print (self.storage[i])
    #   if self.storage[i] != None:
    #     # print("true")
    #     return_list.append(self.storage[i])
    #   else:
    #     break
    # return_list.reverse()
    # return return_list


  def get(self):
    
    return_list = []
    for i in range(len(self.storage)):
      # print (self.storage[i])
      if self.storage[i] != None:
        # print("true")
        return_list.append(self.storage[i])
    
    # self.storage = return_list
    # return_list.reverse()
    return return_list


# thing = RingBuffer(5)

# print(thing.append('a'))
# print(thing.append('b'))
# print(thing.append('c'))
# print(thing.append('d'))
# print(thing.append('e'))
# print(thing.append('f'))
# print(thing.append('g'))
# print(thing.append('h'))
# print(thing.append('i'))






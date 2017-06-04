# TODO: complete this class

class PaginationHelper:

  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
  def __init__(self, collection, items_per_page):
      self.collection = collection
      self.items_per_page = items_per_page
  
  # returns the number of items within the entire collection
  def item_count(self):
      return len(self.collection)
  
  # returns the number of pages
  def page_count(self):
      full_pages, left_items = divmod(self.item_count(), self.items_per_page)
      if not left_items:
          return full_pages
      else:
          return full_pages + 1
      
	
  # returns the number of items on the current page. page_index is zero based
  # this method should return -1 for page_index values that are out of range
  def page_item_count(self,page_index):
        if page_index - 1 >= self.page_count() or page_index - 1 < 0:
            return -1
        else:
            if page_index * self.items_per_page < self.item_count():
                return self.items_per_page
            else:
                # print("ostatnia")
                # print(self.item_count(), self.items_per_page)
                return self.item_count() % self.items_per_page
    
  # determines what page an item is on. Zero based indexes.
  # this method should return -1 for item_index values that are out of range
  def page_index(self,item_index):
      if item_index > self.item_count() and item_index < 0:
          return -1
      return item_index // self.items_per_page
      
  

collection = range(1,25)
helper = PaginationHelper(collection, 11)

print(helper.page_count() == 2)
print(helper.page_index(23) == 2)
print(helper.item_count() == 24)


for _ in range(-5,10):
    print(helper.page_item_count(_))
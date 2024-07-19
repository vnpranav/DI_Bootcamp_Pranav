class Pagination:
   def __init__(self, items=None, pageSize=10):
      self.pageSize = pageSize

      if items is not None:
         self.items = [items[i:i+4] for i in range(0,len(items), 4)]
         self.curr_page = 0
         self.pages = len(self.items) - 1
      else:
         self.items = items

   def getVisibleItems(self):
      if self.items:
         return self.items[self.curr_page]
      
   def nextPage(self):
      if self.curr_page < self.pages:
         self.curr_page += 1

   def prevPage(self):
      if self.curr_page > 0:
         self.curr_page -= 1

   def lastPage(self):
      self.curr_page = self.pages

   def firstPage(self):
      self.curr_page = 0

class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []
        self.page_faults = 0
        self.page_hits = 0

    def access_page(self, page):
        if page not in self.cache:
            # This is a page fault.
            self.page_faults += 1
            if len(self.cache) >= self.capacity:
                self.cache.pop(0)
            self.cache.append(page)
        else:
            self.page_hits += 1
            self.cache.remove(page)
            self.cache.append(page)

    def get_page_faults(self):
        return self.page_faults

    def get_page_hits(self):
        return self.page_hits

    def get_cache(self):
        return self.cache

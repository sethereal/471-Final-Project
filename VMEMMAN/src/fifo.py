class FIFO:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
        self.page_faults = 0
        self.page_hits = 0

    def access_page(self, page):
        if page not in self.queue:
            if len(self.queue) >= self.capacity:
                self.queue.pop(0)
            self.queue.append(page)
            self.page_faults += 1
            return self.page_faults
        else:
            self.page_hits += 1
            return self.page_hits

    def get_page_faults(self):
        return self.page_faults

    def get_page_hits(self):
        return self.page_hits

    def get_queue(self):
        return list(self.queue)

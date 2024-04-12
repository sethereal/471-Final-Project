class MRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
        self.page_faults = 0
        self.page_hits = 0

    def access_page(self, page):
        if page not in self.stack:
            self.page_faults += 1

            if len(self.stack) >= self.capacity:
                self.stack.pop()

            self.stack.append(page)
        else:
            self.page_hits += 1
            self.stack.remove(page)
            self.stack.append(page)

        return self.page_faults

    def get_page_faults(self):
        return self.page_faults

    def get_page_hits(self):
        return self.page_hits

    def get_stack(self):
        return list(self.stack)

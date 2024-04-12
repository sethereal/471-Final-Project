class Optimal:
    def __init__(self, capacity, reference_string):
        self.capacity = capacity
        self.reference_string = reference_string
        self.frames = []
        self.page_faults = 0
        self.page_hits = 0

    def predict(self, current_index):
        farthest_index = -1
        page_to_replace = None
        
        for page in self.frames:
            if page not in self.reference_string[current_index:]:
                return page
            else:
                index = self.reference_string[current_index:].index(page) + current_index
                if index > farthest_index:
                    farthest_index = index
                    page_to_replace = page
        
        return page_to_replace

    def access_page(self, page, current_index):
        if page not in self.frames:
            self.page_faults += 1
            if len(self.frames) >= self.capacity:
                to_replace = self.predict(current_index)
                if to_replace is not None:
                    self.frames.remove(to_replace)
                else:
                    print("Error: No page to replace found.")
            self.frames.append(page)
        else:
            self.page_hits += 1
        return self.page_faults
    
    def get_page_faults(self):
        return self.page_faults

    def get_page_hits(self):
        return self.page_hits

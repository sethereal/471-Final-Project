from threading import Lock 


class SharedBuffer:
    def __init__(self, capacity):
        self.__buffer = []
        self.__capacity = capacity
        self.__total_items = 0
        self.__lock = Lock()
    
    def add_sale_record(self, sale):
        with self.__lock:
            if len(self.__buffer) < self.__capacity:
                self.__buffer.append(sale)
                self.__total_items += 1
           

    def remove_sale_record(self):
        with self.__lock:
            if self.__buffer:
                return self.__buffer.pop(0)
        

    def check_buffer_capacity(self):
        return self.__capacity

    def total_items_produced(self):
        return self.__total_items
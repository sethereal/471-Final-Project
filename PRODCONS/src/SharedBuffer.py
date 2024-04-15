# SharedBuffer.py
from threading import Lock

class SharedBuffer:    
    def __init__(self, capacity):
        self.__buffer = []
        self.__capacity = capacity
        self.__total_items = 0
        self.__lock = Lock()

    # Add a sale record to the buffer in a thread-safe manner
    def add_sale_record(self, sale):
        
        with self.__lock:
            if len(self.__buffer) < self.__capacity:
                self.__buffer.append(sale)
                self.__total_items += 1
                return sale
            else:
                return False
            pass
        pass
    
    # return the top sale record in the buffer
    def peak_top_sale_record(self):
        return self.__buffer[0]
            
    # Remove a sale record from the buffer in a thread-safe manner
    def remove_sale_record(self):        
        with self.__lock:
            if self.__buffer:
                sale_record = self.__buffer.pop(0)
                return sale_record
            else:
                return None
            pass
            
    # Return the capacity of the buffer
    def check_buffer_capacity(self):
        return self.__capacity

    # Return the total number of items produced
    def total_items_produced(self):
        return self.__total_items
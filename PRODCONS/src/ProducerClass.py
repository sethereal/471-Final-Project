#ProducerClass.py
import random
import time
from SharedBuffer import SharedBuffer

class Producer:
    def __init__(self, shared_buffer : SharedBuffer, store_id, max_items=500):
        self.shared_buffer = shared_buffer
        self.items_produced = 0
        self.store_id = store_id
        self.__max_items = max_items
        self.__timeout_min = 0.005
        self.__timeout_max = 0.040
       
    # Generate random sales record data
    def run(self):
        while self.items_produced <= self.__max_items:
            sale = {
                "sale_date": f"{random.randint(1, 30)}/{random.randint(1, 12)}/23",
                "store_id": self.store_id,  
                "register_number": random.randint(1, 6),
                "sale_amount": random.uniform(0.50, 999.99)
            }

            self.shared_buffer.add_sale_record(sale)
            self.items_produced += 1
            time.sleep(random.uniform(self.__timeout_min, self.__timeout_max))
        
        print(f"Producer {self.store_id} finished generating {self.items_produced - 1} items.")
       
       
#ProducerClass.py
import random
import calendar
import time
from .SharedBuffer import SharedBuffer

class Producer:
    def __init__(self, shared_buffer : SharedBuffer, store_id, max_items=500):
        self.shared_buffer = shared_buffer
        self.items_produced = 0
        self.store_id = store_id
        self.__max_items = max_items
        self.__timeout_min = 0.005
        self.__timeout_max = 0.040
       
    # Generate random sales record data
    def produce(self):
        
        while self.items_produced <= self.__max_items:
            month = random.randint(1, 12)
            max_day = calendar.monthrange(2023, month)[1] 
            day = random.randint(1, max_day)
            
            sale = {
                "sale_date": f"{day}/{month}/23",
                "store_id": self.store_id,  
                "register_number": random.randint(1, 6),
                "sale_amount": random.uniform(0.50, 999.99)
            }

            self.shared_buffer.add_sale_record(sale)
            self.items_produced += 1
            time.sleep(random.uniform(self.__timeout_min, self.__timeout_max))
        
        print(f"Producer {self.store_id} finished generating {self.items_produced - 1} items.")
       
       
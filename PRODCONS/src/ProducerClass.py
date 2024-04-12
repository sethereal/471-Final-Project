import random
import time

class ProducerClass:
    def __init__(self, shared_buffer):
        self.shared_buffer = shared_buffer

    def run(self):
        while self.shared_buffer.total_items_produced() < 500:
            # Generate random sales record data
            sale = {
                "sale_date": f"{random.randint(1, 30)}/{random.randint(1, 12)}/23",
                "store_id": random.randint(1, 2),  # Assuming 2 producers
                "register_number": random.randint(1, 6),
                "sale_amount": random.uniform(0.50, 999.99)
            }


            self.shared_buffer.add_sale_record(sale)
            print(f"Producer added sale record: {sale}")
            
            time.sleep(random.uniform(0.005, 0.040))

        print(f"Producer finished generating {self.shared_buffer.total_items_produced()} items.")
# ConsumerClass.py
class ConsumerClass:
    def __init__(self, shared_buffer, storewide_total, month_total, aggregate_total):
        self.__shared_buffer = shared_buffer
        self.__storewide_total = storewide_total
        self.__month_total = month_total
        self.__aggregate_total = aggregate_total
        self.__local_storewide_total = 0
        self.__local_month_total = 0
        self.__local_aggregate_total = 0

    def read_from_buffer(self):
       
            sale_record = self.__shared_buffer.remove_sale_record()
            return sale_record
        

    def __compute_local_stats(self, sale_record):
        self.__local_storewide_total += sale_record["sale_amount"]
        self.__local_month_total += sale_record["sale_amount"]
        self.__local_aggregate_total += sale_record["sale_amount"]

    def update_global_stats(self, storewide_change, month_change, aggregate_change):
        self.__storewide_total.update(storewide_change, 0, 0)
        self.__month_total.update(0, month_change, 0)
        self.__aggregate_total.update(0, 0, aggregate_change)

    def print_local_stats(self):
        print("Consumer Local Statistics:")
        print(f"Storewide Total: {self.__local_storewide_total}")
        print(f"Month-wise Total: {self.__local_month_total}")
        print(f"Aggregate Total: {self.__local_aggregate_total}")

    def consume(self):
        while True:
            sale_record = self.read_from_buffer()
            if sale_record is None:
                break
            self.__compute_local_stats(sale_record)

        storewide_change = self.__local_storewide_total
        month_change = self.__local_month_total
        aggregate_change = self.__local_aggregate_total

        self.update_global_stats(storewide_change, month_change, aggregate_change)
        self.print_local_stats()
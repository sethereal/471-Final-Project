import datetime
from SharedBuffer import SharedBuffer

class Consumer:
    def __init__(self, shared_buffer : SharedBuffer, consumer_id):
        self.__shared_buffer = shared_buffer
        self.__consumer_id = consumer_id
        
        self.__local_storewide_total = 0
        self.__local_month_total = 0
        self.__local_aggregate_total = 0
        self.__current_month = None
        
    # Consume sale records from the queue, compute local stats, and update global stats
    def consume(self):    
        sale_record = self.read_from_buffer()
        self.__compute_local_stats(sale_record)
      
        
    # Read a sale record from the shared buffer and add it to the queue
    def read_from_buffer(self) -> dict:
        top_sale_record = self.__shared_buffer.peak_top_sale_record()

        if top_sale_record["store_id"] == self.__consumer_id:
            sale_record = self.__shared_buffer.remove_sale_record() 
            return sale_record
        return None
            
    # Compute the local stats based on the sale record
    def __compute_local_stats(self, sale_record):        
        if sale_record is None:
            print("Sale_record error")
        elif sale_record["store_id"] == self.__consumer_id:
            self.__local_storewide_total += sale_record["sale_amount"]
            self.update_local_month_total(sale_record)
            self.__local_aggregate_total += sale_record["sale_amount"]

    def update_local_month_total(self, sale_record):
        sale_date = datetime.datetime.strptime(sale_record["sale_date"], "%d/%m/%y")
        sale_month = sale_date.month
        
        if self.__current_month is None or sale_month != self.__current_month:
            self.__current_month = sale_month
            self.__local_month_total = sale_record["sale_amount"]
        else:
            self.__local_month_total += sale_record["sale_amount"]

    def ReportLocalStats(self):
        return (self.__local_storewide_total, self.__local_month_total, self.__local_aggregate_total)
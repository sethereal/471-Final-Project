import datetime

class Consumer:
    def __init__(self, shared_buffer, consumer_id, special_flag):
        self.__shared_buffer = shared_buffer
        self.__consumer_id = consumer_id
        self.__special_flag = special_flag
        self.__local_storewide_total = {}
        self.__local_month_total = {}
        self.__local_aggregate_total = 0

    # Retrieve sales records from the shared buffer and compute local statistics
    def consume(self):
        while not self.__special_flag.is_set():
            sale_record = self.__shared_buffer.remove_sale_record()
            if sale_record is not None:
                self.__compute_local_stats(sale_record)

        return self.ReportLocalStats()

    # Update local statistics based on the given sale record
    def __compute_local_stats(self, sale_record):
        store_id = sale_record["store_id"]
        sale_amount = sale_record["sale_amount"]
        sale_date = datetime.datetime.strptime(sale_record["sale_date"], "%d/%m/%y")
        sale_month = sale_date.month

        self.__update_storewide_total(store_id, sale_amount)
        self.__update_month_total(store_id, sale_month, sale_amount)
        self.__local_aggregate_total += sale_amount

    # Update the local storewide total for the given store ID
    def __update_storewide_total(self, store_id, sale_amount):
        self.__local_storewide_total[store_id] = self.__local_storewide_total.get(store_id, 0) + sale_amount

    # Update the local month-wise total for the given store ID and month
    def __update_month_total(self, store_id, month, sale_amount):
        if store_id not in self.__local_month_total:
            self.__local_month_total[store_id] = {}
        self.__local_month_total[store_id][month] = self.__local_month_total[store_id].get(month, 0) + sale_amount

    # Return the local statistics computed by the consumer
    def ReportLocalStats(self):
        return (self.__local_storewide_total, self.__local_month_total, self.__local_aggregate_total)
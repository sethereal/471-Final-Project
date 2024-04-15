class GlobalStats:
    def __init__(self):
        self.__storewide_total = {}
        self.__month_total = {}
        self.__aggregate_total = 0

    # Update the global statistics with the given local statistics
    def update(self, local_storewide_total, local_month_total, local_aggregate_total):
        for store_id, total in local_storewide_total.items():
            self.__storewide_total[store_id] = self.__storewide_total.get(store_id, 0) + total

        for store_id, month_data in local_month_total.items():
            if store_id not in self.__month_total:
                self.__month_total[store_id] = {}
            for month, total in month_data.items():
                self.__month_total[store_id][month] = self.__month_total[store_id].get(month, 0) + total

        self.__aggregate_total += local_aggregate_total

    # Return the global statistics
    def GetGlobalStats(self):
        return (self.__storewide_total, self.__month_total, self.__aggregate_total)
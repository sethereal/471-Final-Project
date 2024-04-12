from threading import Lock 

class GlobalStats:
    def __init__(self):
        self.__storewide_total = 0
        self.__month_total = 0
        self.__aggregate_total = 0
        self.__lock = Lock()

    def update(self, storewide_change, month_change, aggregate_change):
        with self.__lock:
            self.__storewide_total += storewide_change
            self.__month_total += month_change
            self.__aggregate_total += aggregate_change

    @property
    def storewide_total(self):
        with self.__lock:
            return self.__storewide_total

    @property
    def month_total(self):
        with self.__lock:
            return self.__month_total

    @property
    def aggregate_total(self):
        with self.__lock:
            return self.__aggregate_total
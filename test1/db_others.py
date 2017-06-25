from test1 import request_test
import time
def db_getPrice():
    db_currentPrice = int(request_test.obtain_value("currentPrice"))
    return db_currentPrice
if __name__ == '__main__':
    while request_test.obtain_value("remainTime") > 0:
        try:
            print(db_getPrice())
            time.sleep(1)
        except Exception as e:
            print(e)

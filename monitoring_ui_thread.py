import threading, time, queue

num = 0

class MonitoringQueue():
    monitoring_queue = queue.Queue()
    def __init__(self, parent=None):
        queue_thread = threading.Thread(target=self.read_queue)
        queue_thread.daemon = True
        queue_thread.start()

    def read_queue(self):
        while True:
            print("READ_QUEUE_DATAS : ", self.monitoring_queue.qsize())
            time.sleep(1)
            self.monitoring_queue.put('block.add')
            if (self.monitoring_queue.qsize() % 3) = 0:
                


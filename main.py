import sys, threading, time, queue
from PyQt5 import QtWidgets
from monitoring_layout import Form

monitoring_queue = queue.Queue()

def read_queue():
    while True:
        print("READ_QUEUE_DATAS : ", monitoring_queue.qsize())
        monitoring_queue.put('block.add')
        if monitoring_queue.qsize() % 3 == 0:
            Form.change_frame_color(main_form, 44, 132, 238)
        elif (monitoring_queue.qsize() % 3) == 1:
            Form.change_frame_color(main_form, 231, 76, 60) 
        else:
            Form.change_frame_color(main_form, 241, 196, 15)
        time.sleep(10)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    main_form = Form()

    Form.change_status_text(main_form,"Server Status : CAUTION !!          13:22:09")

    queue_thread = threading.Thread(target=read_queue)
    queue_thread.daemon = True
    queue_thread.start()

    sys.exit(app.exec())

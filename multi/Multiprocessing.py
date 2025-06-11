import platform
import socket
import multiprocessing as mp
import random
import multiprocessing
import time
import gradio as gr
# Sub Program
def sysinfo():
   print("-"*30)
   print("Cấu hình máy tính cá nhân")
   print("-"*30)
   print('Python version:', platform.python_version())
   print('Compiler   :', platform.python_compiler())
   print('System     :', platform.system())
   print('Release    :', platform.release())
   print('Machine    :', platform.machine())
   print('Processor :', platform.processor())
   print('CPU count :', mp.cpu_count())
   print('Interpreter:', platform.architecture()[0])
   print('Host name :', socket.gethostname())
   print('IP Address :', socket.gethostbyname(socket.gethostname()))
   print("-"*30)
   
def append_to_list(lst, num_items):
   """
   Lấy ngẫu nhiên 10 triệu phần tử từ 20 mảng phần tử
   """
   for n in random.sample(range(20000000), num_items):
      lst.append(n)
   print("Phần tử đầu tiên của từng process trong 6 process", lst[0], "\n")

def main(number_of_items, num_proc):
    sysinfo()
    print("Đề bài: Lấy ngẫu nhiên 10 triệu phần tử từ 20 mảng phần tử\n") 
    print("Chương trình đang xử lý ... vui lòng đợi trong giây lát")
    
    # Chương trình bình thường
    start_time = time.time()
   
    append_to_list([], number_of_items)
    end_time = time.time()
    a=end_time - start_time
    print("Chương trình bình thường")
    print("Thời gian thực hiện tuần tự:", a)
    print("-"*30)
    print("\n")
    
    # Chương trình sài multiprocessing
    jobs = []
    start_time = time.time()

    for i in range(num_proc):
       process = multiprocessing.Process(
          target=append_to_list,
          args=([], number_of_items // num_proc)
       )
       print(process)
       jobs.append(process)

    for j in jobs:
       j.start()

    for j in jobs:
       j.join()
    end_time = time.time()
    b=end_time - start_time
    print("Chương trình sài multiprocessing")
    print("-"*30)
    print("Thời gian thực hiện với multiprocessing:", b)
    print("-"*30)
    return a,b

if __name__ == '__main__':
    # number_of_items = 10000000
    # num_proc = 6
    iface = gr.Interface(
        main, 
        inputs=[gr.Number(label="Nhập vào tổng con số cần tìm"),gr.Number(label="Nhập vào số Process(Có thể xem lõi ở cấu hình của máy)"),],
        outputs=[gr.Number(label="Thời gian tuần tự(giây)"),gr.Number(label="Thời gian thực hiện với multiprocessing(giây)"),],
        title="Tìm kiếm số ngẫu nhiên từ một mảng 20 triệu số",
        description="Bạn có thể vào Task manager. Vào phần Performance để xem core đó chính là lõi của máy"
    )
    # Khởi chạy giao diện Gradio với tham số Share=True  
    # Cho phép chia sẻ giao diện dưới dạng ứng dụng web có thể truy cập từ trình duyệt web
    iface.launch(share=True)
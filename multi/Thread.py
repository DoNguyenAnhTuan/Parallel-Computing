import requests
from queue import Queue
from threading import Thread
import time
import os
import gradio as gr

def download_img(img_url: str, directory: str):
    """
    Download image from img_url in the specified directory
    """
    res = requests.get(img_url, stream=True)
    filename = os.path.join(directory, f"{os.path.basename(img_url)}")
    with open(filename, 'wb') as f:
        for block in res.iter_content(1024):
            f.write(block)

def download_img_Thread(directory: str, q: Queue):
    """
    Download image from img_url in the specified directory using threading
    """
    while True:
        img_url = q.get()
        res = requests.get(img_url, stream=True)
        filename = os.path.join(directory, f"{os.path.basename(img_url)}")
        with open(filename, 'wb') as f:
            for block in res.iter_content(1024):
                f.write(block)
        q.task_done()

def main(img_urls, num_threads):
    image_directory='images'
    img_urls = img_urls.split()
    num_threads = int(num_threads)
    start_time = time.time()
    
    # Create directory if it doesn't exist
    if not os.path.exists(image_directory):
        os.makedirs(image_directory)

    # Sequential download
    for img in img_urls:
        download_img(img, image_directory)

    end_time = time.time()
    sequential_time = end_time - start_time
    print("Thời gian thực hiện tuần tự:", sequential_time)
    
    # Threaded download
    start_time = time.time()
    q = Queue()

    # Add image URLs to the queue
    for img_url in img_urls:
        q.put(img_url)

    # Create threads
    for _ in range(num_threads):
        worker = Thread(target=download_img_Thread, args=(image_directory, q))
        worker.daemon = True
        worker.start()

    # Wait for all tasks to complete
    q.join()
    end_time = time.time()
    threading_time = end_time - start_time
    print("Thời gian thực hiện Thread:", threading_time)
    
    return sequential_time, threading_time
# ví dụ
# https://cdn.pixabay.com/photo/2021/07/13/11/34/cat-6463284_640.jpg
# https://cdn.pixabay.com/photo/2016/02/10/16/37/cat-1192026_640.jpg
# https://www.shutterstock.com/image-photo/sitting-sweety-cat-looking-aside-600nw-2323092103.jpg
iface = gr.Interface(
    fn=main,
    inputs=[
        gr.Textbox(lines=5, placeholder="Nhập các URL hình ảnh cách nhau bằng dấu cách", label="Image URLs"),
        gr.Number(label="Nhập vào số lượng Threads"),
    ],
    outputs=[
        gr.Number(label="Thời gian tải xuống tuần tự (giây)"),
        gr.Number(label="Thời gian tải xuống bằng Threading (giây)")
    ],
    title="Trình tải xuống hình ảnh",
    description="Nhập URL hình ảnh, số chủ đề và thư mục để lưu hình ảnh. Hệ thống sẽ tải xuống hình ảnh một cách tuần tự và sử dụng phân luồng, sau đó so sánh thời gian thực hiện."
)

if __name__ == '__main__':
    iface.launch(share=True)

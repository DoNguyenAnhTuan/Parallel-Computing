```markdown
# ⚙️ Parallel Computing with Python

This repository contains hands-on exercises and examples of **parallel computing** techniques in Python. It demonstrates how to utilize CPU cores efficiently using **`multiprocessing`** and **`threading`** for faster data processing and task execution.

---

## 🚀 Key Concepts

- 🔁 **Multithreading** – Ideal for I/O-bound tasks (e.g., file, network)
- 🔀 **Multiprocessing** – Best for CPU-bound tasks (e.g., computations)
- ⏱️ Performance comparison between sequential and parallel approaches

---

## 🧩 Implemented Features

- Task-based parallelism
- Process pool execution
- ThreadPoolExecutor usage
- Real-world examples: matrix operations, file reading, CPU benchmarking

---

## 📂 Structure

```

parallel-computing/
│
├── multiprocessing\_example.py
├── threading\_example.py
├── matrix\_parallel.py
├── cpu\_benchmark.py
└── README.md

````

---

## 🖥️ Requirements

- Python 3.7+
- No external dependencies required (uses built-in `multiprocessing` & `concurrent.futures`)

---

## 💻 How to Run

```bash
python multiprocessing_example.py
python threading_example.py
````

Each script includes performance logs to compare execution time.

---

## 📊 Sample Output

```
Sequential time: 10.02s
Parallel time:    2.41s
Speed-up:         ~4.15x
```

---

## 📬 Author

**Do Nguyen Anh Tuan**
🎓 MSc in IT @ Lac Hong University
🏢 FabLab @ EIU
🔗 [Portfolio Website](https://donguyenanhtuan.github.io/AnhTuan-Portfolio)

---


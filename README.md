# rate_limiter_patterns

A practical Python project demonstrating different rate limiting algorithms and patterns. This repo helps developers understand how rate limiting works under the hood, why it’s important, and how to implement it for real-world use cases.

---

## 📌 What is Rate Limiting?
Rate limiting is a technique used to control the amount of incoming or outgoing traffic in a network, API, or application over a specific time period. It ensures fair usage, avoids abuse, protects resources, and provides a better user experience.

---

## 🚦 Included Algorithms

1. **Fixed Window Counter**
2. **Sliding Window Log**
3. **Sliding Window Counter**
4. **Token Bucket**
5. **Leaky Bucket**

---

## 📁 Folder Structure

```
rate_limiter_patterns/
├── fixed_window.py
├── sliding_window_log.py
├── sliding_window_counter.py
├── token_bucket.py
├── leaky_bucket.py
├── tests/
│   ├── test_fixed_window.py
│   ├── test_sliding_window_log.py
│   └── ...
├── examples/
│   ├── api_rate_limit_example.py
├── README.md
└── requirements.txt
```

---

## ✅ Real-world Use Cases
- API Gateway traffic throttling
- Login attempt protection
- Messaging systems
- Payment gateway requests
- IoT device communication

---

## 🧪 How to Run

1. Clone the repository:
```bash
git clone https://github.com/arunsaiv/rate-limiter-patterns.git
cd rate-limiter-patterns
```

2. (Optional) Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run any algorithm script directly:
```bash
python token_bucket.py
```

---

## 📦 Requirements
```
# requirements.txt
```
(This will be updated as we add dependencies, currently only using built-in modules)

---

## 🙌 Contributing
Pull requests are welcome. Let’s collaborate to build a comprehensive library of rate limiting strategies!

---

## 📜 License
MIT

---

## 💬 Feedback
If you find this useful, give it a ⭐ on GitHub, and feel free to reach out or open an issue for improvements!

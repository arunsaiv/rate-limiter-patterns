# Rate Limiter Patterns

A practical Python project demonstrating different rate limiting algorithms and patterns. This repo helps developers understand how rate limiting works under the hood, why it’s important, and how to implement it for real-world use cases.

---

## 📌 What is Rate Limiting?
Rate limiting is a technique used to control the amount of incoming or outgoing traffic in a network, API, or application over a specific time period. It ensures fair usage, avoids abuse, protects resources, and provides a better user experience.

---

## 📦 Patterns Implemented

| Pattern           | Description |
|------------------|-------------|
| ✅ **Fixed Window**     | Allows a set number of requests in a fixed interval (e.g., 10/minute). |
| ✅ **Rolling Window**   | Similar to fixed but rolls over the interval dynamically. |
| ✅ **Leaky Bucket**     | Enforces a constant outflow rate, handling bursts smoothly. |
| ✅ **Token Bucket**     | Allows bursts and refills tokens over time. |
| ✅ **Distributed Rate Limiting (Redis)** | Ensures rate limits across multiple services/nodes. |

---

## 📁 Folder Structure

```
rate_limiter_patterns/
├── fixed_window.py
├── sliding_window.py
├── distributed_token_bucket.py
├── token_bucket.py
├── leaky_bucket.py
├── tests/
│   ├── test_fixed_window.py
│   ├── test_sliding_window.py
│   └── ...
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
python test_token_bucket.py
```

---

## 📦 Requirements
```
# requirements.txt
```
(This will be need only if you are installing redis for distributed token bucket rate limiter)

---

## 🙌 Contributing
Pull requests are welcome. Let’s collaborate to build a comprehensive library of rate limiting strategies!

---

## 📜 License
MIT

---

## ❤️ Like the Project?

If you found this helpful:
-	⭐ Star the repo
-	📢 Share with others
-	🧠 Contribute ideas or patterns

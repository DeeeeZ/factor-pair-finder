# 🔢 Factor Pair Finder

A beautiful, high-performance web application built with Streamlit that finds all factor pairs of any positive integer (excluding 1 × n).

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28.0+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

- **Fast Algorithm**: Optimized trial division up to √n for efficient factorization
- **Large Number Support**: Handle integers with 18+ digits
- **Beautiful UI**: Modern, responsive design with gradient styling
- **Smart Classification**: Automatically identifies Prime, Semiprime, or Composite numbers
- **Detailed Statistics**: View number of digits, search space, and execution time
- **CSV Export**: Download results for further analysis
- **Input Validation**: Friendly error messages for invalid inputs
- **Result Caching**: Lightning-fast repeat queries with `@st.cache_data`

## 🚀 Quick Start

### Local Installation

1. **Clone or download this repository**

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
streamlit run app.py
```

4. **Open your browser** and navigate to `http://localhost:8501`

## 🌐 Deploy to Streamlit Cloud

1. **Push to GitHub**: Upload this project to a GitHub repository

2. **Visit Streamlit Cloud**: Go to [share.streamlit.io](https://share.streamlit.io)

3. **Deploy**: Click "New app" and select:
   - Repository: Your GitHub repo
   - Branch: `main` (or your default branch)
   - Main file path: `app.py`

4. **Launch**: Click "Deploy" and your app will be live in minutes!

## 📊 How It Works

### Algorithm Overview

The app uses **trial division** to find factor pairs:

1. Takes input number `n`
2. Calculates `√n` (search limit)
3. Tests divisibility from 2 to √n
4. For each divisor `i` where `n % i == 0`, stores pair `(i, n/i)`
5. Excludes trivial pair `(1, n)`

**Time Complexity**: O(√n)
**Space Complexity**: O(k) where k = number of factor pairs

### Number Classification

- **Prime**: No factors besides 1 and itself
- **Semiprime**: Product of exactly two prime numbers (1 factor pair)
- **Composite**: More than one factor pair

## 🧪 Test Cases

| Input | Expected Output | Classification |
|-------|----------------|----------------|
| 20 | (2, 10), (4, 5) | Composite |
| 997 | None (prime) | Prime |
| 34,714,069,601 | (37199, 933199) | Semiprime |
| 1,234,567,890,123,456 | 83 pairs | Composite |

## 📁 Project Structure

```
IntegerFactorization/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🛠️ Tech Stack

- **Python 3.8+**
- **Streamlit 1.28.0+** - Web framework
- **Pandas 2.0.0+** - Data handling and CSV export
- **Custom CSS** - Beautiful gradient styling

## 💡 Usage Tips

1. **Input Format**: Enter numbers with or without commas (e.g., `1234567` or `1,234,567`)
2. **Large Numbers**: The app efficiently handles integers up to 18+ digits
3. **Export Results**: Click "Download as CSV" to save factor pairs
4. **Cached Results**: Searching the same number twice is instant (uses caching)

## 🎨 Customization

### Modify Colors

Edit the CSS gradient in `app.py` (lines 15-85):

```python
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

Replace hex codes with your preferred colors.

### Change Page Layout

In `st.set_page_config()`:
- `layout="centered"` → `layout="wide"` for full-width layout
- Modify `page_title` and `page_icon`

## 📝 Credits

Developed with ❤️ by **Hamzeh Gheidan**

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

**Powered by Streamlit** | Built for efficiency and elegance ⚡

# Factor Pair Finder - Project Documentation

## Project Overview
A Streamlit web application that efficiently finds all factor pairs of any positive integer (excluding 1 × n).

## Tech Stack
- **Python 3.8+**
- **Streamlit 1.28.0+** - Web framework for the UI
- **Pandas 2.0.0+** - Data handling and CSV export functionality
- **Math module** - For efficient square root calculations

## Project Structure
```
IntegerFactorization/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # User-facing documentation
└── CLAUDE.md          # This file - development documentation
```

## Core Algorithm
- **Method**: Trial division from 2 to √n
- **Time Complexity**: O(√n)
- **Space Complexity**: O(k) where k = number of factor pairs
- **Optimization**: Uses `math.isqrt()` for integer square root (faster than `int(math.sqrt())`)

## Key Features Implemented

### 1. Factor Finding Algorithm
- Located in `find_factor_pairs()` function
- Efficiently finds all divisors up to √n
- Returns factor pairs, execution time, and number classification
- Decorated with `@st.cache_data` for performance

### 2. Number Classification
- **Prime**: No factor pairs found
- **Semiprime**: Exactly one factor pair (product of two primes)
- **Composite**: Multiple factor pairs

### 3. Input Validation
- Located in `validate_input()` function
- Strips commas and whitespace
- Validates positive integers only
- Friendly error messages via `st.error()`

### 4. UI Components
- **Header**: Gradient-styled title and subtitle
- **Input Section**: Text input with placeholder examples
- **Stats Panel**: 4-column metrics (digits, search space, time, pairs)
- **Results Table**: Formatted DataFrame with thousand separators
- **Export Button**: CSV download functionality
- **Classification Badge**: Color-coded status (Prime/Semiprime/Composite)

### 5. Styling
- Custom CSS with gradient themes (#667eea to #764ba2)
- Responsive layout with centered design
- Hover effects on buttons
- Color-coded badges for classifications
- Info boxes for educational content

## Performance Optimizations
1. **Caching**: `@st.cache_data` decorator on `find_factor_pairs()`
2. **Efficient Square Root**: `math.isqrt()` instead of `math.sqrt()`
3. **Early Termination**: Only searches up to √n
4. **Session State**: Stores last result for reference

## Testing
All test cases passed:
- ✅ 20 → [(2, 10), (4, 5)] - Composite
- ✅ 997 → [] - Prime
- ✅ 34,714,069,601 → [(37199, 933199)] - Semiprime
- ✅ 1,234,567,890,123,456 → 83 pairs - Composite (1.3s execution time)

## Deployment
Ready for Streamlit Cloud deployment:
1. All dependencies listed in `requirements.txt`
2. No local file dependencies
3. No environment variables required
4. Pure Python implementation (cross-platform compatible)

## Future Enhancement Ideas
- [ ] Add factorization tree visualization
- [ ] Support for prime factorization (not just pairs)
- [ ] Progress bar for very large numbers
- [ ] Batch processing (multiple numbers at once)
- [ ] Historical search results panel
- [ ] Dark/light theme toggle
- [ ] API endpoint for programmatic access

## Code Style Guidelines
- Follow PEP 8 conventions
- Use type hints where applicable
- Add docstrings to all functions
- Keep functions focused and single-purpose
- Use descriptive variable names
- Comment complex logic

## Known Limitations
- Very large numbers (>18 digits) may take longer to process
- No support for negative numbers or decimals
- Memory usage scales with number of factor pairs

## Credits
Developed by Hamzeh Gheidan
Built with Streamlit

---
Last Updated: 2026-01-20

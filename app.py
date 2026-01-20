import streamlit as st
import pandas as pd
import time
import math
from io import StringIO

# Page configuration
st.set_page_config(
    page_title="Factor Pair Finder",
    page_icon="🔢",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for stunning dark theme
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=JetBrains+Mono:wght@400;500&display=swap');

    /* CSS Variables for Dark Theme */
    :root {
        --bg-primary: #0f1419;
        --bg-secondary: #1a1d29;
        --bg-tertiary: #242938;
        --accent-primary: #14b8a6;
        --accent-secondary: #06b6d4;
        --accent-hover: #0d9488;
        --text-primary: #ffffff;
        --text-secondary: #9ca3af;
        --text-muted: #6b7280;
        --border-subtle: #2d3748;
        --success: #10b981;
        --warning: #f59e0b;
        --error: #ef4444;
        --info: #3b82f6;
    }

    /* Global Styles */
    .stApp {
        background-color: var(--bg-primary);
    }

    .main {
        background-color: var(--bg-primary);
    }

    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Custom Header */
    .app-header {
        background: linear-gradient(135deg, var(--bg-secondary) 0%, var(--bg-tertiary) 100%);
        padding: 2.5rem 2rem 2rem 2rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        border: 1px solid var(--border-subtle);
        position: relative;
        overflow: hidden;
    }

    .app-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, var(--accent-primary), var(--accent-secondary));
    }

    .app-title {
        font-family: 'DM Sans', sans-serif;
        font-size: 2.5rem;
        font-weight: 700;
        color: var(--text-primary);
        margin: 0;
        display: flex;
        align-items: center;
        gap: 0.75rem;
        letter-spacing: -0.02em;
    }

    .app-icon {
        font-size: 2.5rem;
        background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .app-subtitle {
        font-family: 'DM Sans', sans-serif;
        font-size: 1rem;
        color: var(--text-secondary);
        margin-top: 0.5rem;
        font-weight: 400;
    }

    .lightning-icon {
        color: var(--accent-primary);
        font-size: 1.1rem;
    }

    /* Section Headers */
    .section-header {
        font-family: 'DM Sans', sans-serif;
        font-size: 1rem;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .section-icon {
        font-size: 1.2rem;
    }

    /* Input Styling */
    .stTextInput > div > div > input {
        background-color: var(--bg-secondary);
        border: 1px solid var(--border-subtle);
        border-radius: 12px;
        color: var(--text-primary);
        font-family: 'JetBrains Mono', monospace;
        font-size: 1.1rem;
        padding: 1rem 1.25rem;
        transition: all 0.3s ease;
    }

    .stTextInput > div > div > input:focus {
        border-color: var(--accent-primary);
        box-shadow: 0 0 0 3px rgba(20, 184, 166, 0.1);
        outline: none;
    }

    .stTextInput > div > div > input::placeholder {
        color: var(--text-muted);
    }

    /* Button Styling */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
        color: var(--text-primary);
        border: none;
        padding: 0.875rem 2rem;
        font-family: 'DM Sans', sans-serif;
        font-size: 1rem;
        font-weight: 600;
        border-radius: 12px;
        transition: all 0.3s ease;
        letter-spacing: 0.02em;
        box-shadow: 0 4px 12px rgba(20, 184, 166, 0.2);
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(20, 184, 166, 0.3);
        background: linear-gradient(135deg, var(--accent-hover), var(--accent-primary));
    }

    .stButton > button:active {
        transform: translateY(0);
    }

    /* Metrics Styling */
    div[data-testid="stMetric"] {
        background-color: var(--bg-secondary);
        padding: 1.25rem;
        border-radius: 12px;
        border: 1px solid var(--border-subtle);
        transition: all 0.3s ease;
    }

    div[data-testid="stMetric"]:hover {
        border-color: var(--accent-primary);
        background-color: var(--bg-tertiary);
    }

    div[data-testid="stMetric"] label {
        font-family: 'DM Sans', sans-serif;
        font-size: 0.75rem;
        color: var(--text-muted);
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    div[data-testid="stMetric"] [data-testid="stMetricValue"] {
        font-family: 'JetBrains Mono', monospace;
        font-size: 1.75rem;
        color: var(--accent-primary);
        font-weight: 600;
    }

    /* Classification Badge */
    .badge-container {
        text-align: center;
        margin: 1.5rem 0;
    }

    .badge {
        display: inline-block;
        padding: 0.625rem 1.5rem;
        border-radius: 24px;
        font-family: 'DM Sans', sans-serif;
        font-weight: 600;
        font-size: 0.875rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        transition: all 0.3s ease;
    }

    .badge-prime {
        background: rgba(16, 185, 129, 0.15);
        color: var(--success);
        border: 1px solid var(--success);
    }

    .badge-semiprime {
        background: rgba(245, 158, 11, 0.15);
        color: var(--warning);
        border: 1px solid var(--warning);
    }

    .badge-composite {
        background: rgba(20, 184, 166, 0.15);
        color: var(--accent-primary);
        border: 1px solid var(--accent-primary);
    }

    /* Info Box */
    .info-box {
        background-color: var(--bg-secondary);
        border-left: 3px solid var(--accent-primary);
        padding: 1rem 1.25rem;
        border-radius: 8px;
        margin: 1rem 0;
        font-family: 'DM Sans', sans-serif;
        color: var(--text-secondary);
        font-size: 0.95rem;
        line-height: 1.6;
    }

    .info-box strong {
        color: var(--text-primary);
    }

    /* Table Styling */
    div[data-testid="stDataFrame"] {
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid var(--border-subtle);
    }

    div[data-testid="stDataFrame"] table {
        background-color: var(--bg-secondary);
    }

    div[data-testid="stDataFrame"] thead tr th {
        background-color: var(--bg-tertiary) !important;
        color: var(--text-primary) !important;
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 600 !important;
        font-size: 0.875rem !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        padding: 1rem !important;
        border-bottom: 2px solid var(--accent-primary) !important;
    }

    div[data-testid="stDataFrame"] tbody tr td {
        background-color: var(--bg-secondary) !important;
        color: var(--text-secondary) !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 0.9rem !important;
        padding: 0.875rem 1rem !important;
        border-bottom: 1px solid var(--border-subtle) !important;
    }

    div[data-testid="stDataFrame"] tbody tr:hover td {
        background-color: var(--bg-tertiary) !important;
        color: var(--text-primary) !important;
    }

    /* Alert Styling */
    .stSuccess, .stInfo, .stError {
        background-color: var(--bg-secondary);
        border-radius: 12px;
        border-left: 3px solid;
        padding: 1rem 1.25rem;
        font-family: 'DM Sans', sans-serif;
    }

    .stSuccess {
        border-left-color: var(--success);
        color: var(--success);
    }

    .stInfo {
        border-left-color: var(--info);
        color: var(--info);
    }

    .stError {
        border-left-color: var(--error);
        color: var(--error);
    }

    /* Download Button */
    .stDownloadButton > button {
        width: 100%;
        background-color: var(--bg-secondary);
        color: var(--text-primary);
        border: 1px solid var(--border-subtle);
        padding: 0.875rem 2rem;
        font-family: 'DM Sans', sans-serif;
        font-size: 1rem;
        font-weight: 600;
        border-radius: 12px;
        transition: all 0.3s ease;
    }

    .stDownloadButton > button:hover {
        background-color: var(--bg-tertiary);
        border-color: var(--accent-primary);
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(20, 184, 166, 0.15);
    }

    /* Divider */
    hr {
        border: none;
        border-top: 1px solid var(--border-subtle);
        margin: 2rem 0;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: var(--text-muted);
        font-family: 'DM Sans', sans-serif;
        font-size: 0.875rem;
        padding: 2rem 0 1rem 0;
    }

    /* Spinner Override */
    .stSpinner > div {
        border-top-color: var(--accent-primary) !important;
    }

    /* Animation */
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .fade-in {
        animation: fadeIn 0.5s ease-out;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def find_factor_pairs(n):
    """
    Find all factor pairs of n (excluding 1 × n) using trial division.

    Args:
        n: Positive integer to factorize

    Returns:
        tuple: (list of factor pairs, execution time, classification)
    """
    start_time = time.time()

    if n < 2:
        return [], time.time() - start_time, "Invalid"

    factors = []
    sqrt_n = int(math.isqrt(n))

    # Trial division from 2 to √n
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            factors.append((i, n // i))

    execution_time = time.time() - start_time

    # Classify the number
    if len(factors) == 0:
        classification = "Prime"
    elif len(factors) == 1:
        classification = "Semiprime"
    else:
        classification = "Composite"

    return factors, execution_time, classification

def format_number(num):
    """Format number with thousand separators."""
    return f"{num:,}"

def validate_input(input_str):
    """
    Validate and parse user input.

    Args:
        input_str: String input from user

    Returns:
        tuple: (is_valid, parsed_number, error_message)
    """
    if not input_str or input_str.strip() == "":
        return False, None, "Please enter a number."

    # Remove commas and whitespace
    cleaned = input_str.replace(",", "").replace(" ", "").strip()

    # Check if it's a valid integer
    if not cleaned.isdigit():
        return False, None, "Please enter a valid positive integer."

    try:
        number = int(cleaned)
        if number < 2:
            return False, None, "Please enter a number greater than 1."
        return True, number, None
    except ValueError:
        return False, None, "Invalid number format."

def get_classification_badge(classification):
    """Return HTML badge based on classification."""
    if classification == "Prime":
        return '<span class="badge badge-prime">PRIME</span>'
    elif classification == "Semiprime":
        return '<span class="badge badge-semiprime">SEMIPRIME</span>'
    else:
        return '<span class="badge badge-composite">COMPOSITE</span>'

def get_classification_explanation(classification):
    """Return explanation for number classification."""
    explanations = {
        "Prime": "A prime number has no factors other than 1 and itself.",
        "Semiprime": "A semiprime is the product of exactly two prime numbers.",
        "Composite": "A composite number has more than two factor pairs."
    }
    return explanations.get(classification, "")

# Main App
def main():
    # Header
    st.markdown("""
    <div class="app-header">
        <h1 class="app-title">
            <span class="app-icon">🔢</span>
            Factor Pair Finder
        </h1>
        <p class="app-subtitle">
            Discover all factor pairs of any integer with lightning speed <span class="lightning-icon">⚡</span>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Input Section
    st.markdown('<div class="section-header"><span class="section-icon">📊</span> Enter a Number</div>', unsafe_allow_html=True)
    number_input = st.text_input(
        "Enter any positive integer (commas allowed)",
        placeholder="e.g., 12,312,312 or 997",
        label_visibility="collapsed"
    )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        find_button = st.button("🔍 Find Factors", use_container_width=True)

    # Process when button is clicked
    if find_button:
        is_valid, number, error_msg = validate_input(number_input)

        if not is_valid:
            st.error(f"❌ {error_msg}")
        else:
            # Show spinner while calculating
            with st.spinner(f"🔎 Searching for factor pairs of {format_number(number)}..."):
                factors, exec_time, classification = find_factor_pairs(number)

            # Store in session state for export
            st.session_state['last_result'] = {
                'number': number,
                'factors': factors,
                'exec_time': exec_time,
                'classification': classification
            }

            # Display results
            st.markdown("---")
            st.markdown('<div class="section-header"><span class="section-icon">📈</span> Results</div>', unsafe_allow_html=True)

            # Stats Panel
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric(
                    "Number of Digits",
                    len(str(number)),
                    help="Total digits in the input number"
                )

            with col2:
                sqrt_n = int(math.isqrt(number))
                st.metric(
                    "Search Space",
                    format_number(sqrt_n - 1),
                    help=f"Checked from 2 to √n ≈ {format_number(sqrt_n)}"
                )

            with col3:
                st.metric(
                    "Execution Time",
                    f"{exec_time*1000:.2f} ms",
                    help="Time taken to find all factors"
                )

            with col4:
                st.metric(
                    "Factor Pairs",
                    len(factors),
                    help="Total factor pairs found (excluding 1 × n)"
                )

            # Classification Badge
            st.markdown('<div class="section-header" style="margin-top: 2rem;">Number Classification</div>', unsafe_allow_html=True)
            badge_html = get_classification_badge(classification)
            st.markdown(f'<div class="badge-container">{badge_html}</div>', unsafe_allow_html=True)

            explanation = get_classification_explanation(classification)
            if explanation:
                st.markdown(f'<div class="info-box">💡 <strong>What is this?</strong> {explanation}</div>', unsafe_allow_html=True)

            # Results Table
            if len(factors) > 0:
                st.markdown('<div class="section-header" style="margin-top: 2rem;"><span class="section-icon">🎯</span> Factor Pairs</div>', unsafe_allow_html=True)

                # Create DataFrame with formatted numbers
                df = pd.DataFrame(factors, columns=["Factor A", "Factor B"])
                df["Factor A"] = df["Factor A"].apply(format_number)
                df["Factor B"] = df["Factor B"].apply(format_number)

                # Add index starting from 1
                df.index = range(1, len(df) + 1)

                # Display table
                st.dataframe(
                    df,
                    use_container_width=True,
                    height=min(400, (len(factors) + 1) * 35 + 38)
                )

                st.success(f"✅ Found {len(factors)} factor pair{'s' if len(factors) != 1 else ''} for {format_number(number)}")

                # Export Section
                st.markdown('<div class="section-header" style="margin-top: 2rem;"><span class="section-icon">💾</span> Export Results</div>', unsafe_allow_html=True)

                # Create CSV
                csv_buffer = StringIO()
                export_df = pd.DataFrame(factors, columns=["Factor A", "Factor B"])
                export_df.to_csv(csv_buffer, index=False)
                csv_data = csv_buffer.getvalue()

                col1, col2, col3 = st.columns([1, 2, 1])
                with col2:
                    st.download_button(
                        label="📥 Download as CSV",
                        data=csv_data,
                        file_name=f"factors_{number}.csv",
                        mime="text/csv",
                        use_container_width=True
                    )
            else:
                st.info(f"🎉 **{format_number(number)}** is a prime number! It has no factor pairs (except 1 × {format_number(number)}).")

    # Show cached results if available
    elif 'last_result' in st.session_state:
        result = st.session_state['last_result']
        st.info(f"ℹ️ Showing cached results for {format_number(result['number'])}. Enter a new number to search again.")

    # Footer
    st.markdown("---")
    st.markdown(
        '<p class="footer">Built with ❤️ by Hamzeh Gheidan | Powered by Streamlit</p>',
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()

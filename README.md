# 💹 AI-Powered Financial & Web Agent

This project is a **Streamlit-based AI application** that integrates **financial analysis and web search capabilities** using **Groq's LLaMA-3.3-70B model**. The AI agents retrieve up-to-date stock market data and general web information to provide insightful responses with sources.

## 🚀 Features
- **📊 Financial Analysis:** Fetches stock fundamentals, company info, and analyst recommendations using Yahoo Finance.
- **🌐 Web Search:** Provides real-time web search results using DuckDuckGo.
- **💬 AI-Powered Responses:** Uses Groq's LLaMA-3.3-70B for intelligent query processing.
- **📡 Streaming Output:** Displays responses in real-time as they are generated.
- **🎨 Beautiful Streamlit UI:** Interactive and user-friendly interface for seamless experience.

## 🛠️ Installation
### **1. Clone the Repository**
```bash
git clone https://github.com/your-repo/financial-web-agent.git
cd financial-web-agent
```

### **2. Create a Virtual Environment (Optional but Recommended)**
```bash
python -m venv env
source env/bin/activate  # On macOS/Linux
env\Scripts\activate   # On Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Set Up API Keys**
Ensure you have a `.env` file in the root directory and add the following:
```ini
GROQ_API_KEY=your_api_key_here
```

## 🎯 Usage
### **Run the Streamlit App**
```bash
streamlit run app.py
```
- Open the browser at `http://localhost:8501`
- Enter a **financial or general query**
- Click "**Get Response**" and wait for AI-generated insights

## 📝 Example Queries
- *"Summarize and compare analyst recommendations and fundamentals for TESLA vs NVIDIA stocks."*
- *"What are the latest trends in AI and machine learning?"*
- *"Give me the stock price and company details of Apple."*

## 🔧 Troubleshooting
**1️⃣ ModuleNotFoundError:** Install missing dependencies:
```bash
pip install -r requirements.txt
```

**2️⃣ API Errors:** Ensure your `.env` file contains the correct `GROQ_API_KEY`.

**3️⃣ Port Already in Use:** Run Streamlit on a different port:
```bash
streamlit run app.py --server.port 8502
```

## 📜 License
This project is licensed under the **MIT License**.

## 📬 Contact
For issues or suggestions, reach out via [GitHub Issues](https://github.com/your-repo/issues).

---

🔥 **Empower your financial decisions with AI!** 🚀



# 📊 Stock Research Tool with Data Analytics

## 📌 Description
This project enables users to effortlessly analyze company fundamentals, providing clear insights through intuitive data visualization techniques. It simplifies financial analysis, making it easier to understand a company's performance at a glance.

## 🚀 Features
✅ **Interactive Data Visualization** – Visualize trends and patterns for better insights.  
✅ **Company Overview & Business Model** – Detailed explanation of the company’s operations.  
✅ **Financial Data Sheets** – Access structured company financial data for deeper analysis.  

---

## ⚡ Installation Guide

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/Mahidhar-Reddy-karakala/GenAi-stock-Research-Tool.git
```

### 2️⃣ Create and Activate a Virtual Environment
```sh
python -m venv venv
```

### 3️⃣ Activate the Virtual Environment
**Windows:**  
```sh
venv\Scripts\activate
```
**Mac/Linux:**  
```sh
source venv/bin/activate
```

### 4️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

---

## 🔐 Setting Up Environment Variables
1. Create a `.env` file in the project root directory.
2. Add the required variables as shown below:
   ```
   API_KEY=your_api_key_here
   DATABASE_URL=your_database_url_here
   ```
3. Save the file and proceed with running the application.
4. Ensure the `.env` file is **not** committed to Git by adding it to `.gitignore`:
   ```
   .env
   ```

---

## ▶️ Run the Application
### **Using Command Prompt or Terminal**
1. Navigate to the project directory:
   ```sh
   cd GenAi-stock-Research-Tool
   ```
2. Activate the virtual environment:
   - **Windows:**
     ```sh
     venv\Scripts\activate
     ```
   - **Mac/Linux:**
     ```sh
     source venv/bin/activate
     ```
3. Run the application:
   ```sh
   streamlit run StockData.py
   ```

### **Using VS Code**
1. Open VS Code and navigate to the project folder.
2. Open a new terminal (Ctrl + `).
3. Activate the virtual environment as shown above.
4. Run the application using:
   ```sh
   streamlit run StockData.py
   ```

---

## 🤝 Contributing
Feel free to fork this repository and submit pull requests for improvements.

## 📜 License
This project is licensed under the **MIT License**.

✅ Now you're all set! Start exploring financial insights effortlessly. 🚀📈

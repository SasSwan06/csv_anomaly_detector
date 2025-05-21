# 📊 CSV Anomaly Detector

**A Streamlit-based web application to detect and flag anomalies in CSV datasets.**  
Designed for data analysts, scientists, and developers, this tool supports various anomaly detection techniques and provides suggestions for preprocessing improvements.

---

## 🚀 Features

- 📂 Upload any CSV file with numerical data
- ⚠️ Detect anomalies using:
  - Interquartile Range (IQR)
  - Skewness analysis
  - (More methods coming soon: Z-Score, Isolation Forest, etc.)
- 🧠 Understand the *why* behind flagged anomalies
- 🔧 Get preprocessing suggestions (e.g., winsorization)
- 📈 Visualize skewed data and distributions (optional)
- 💡 Easily extendable for additional detection methods

---

## 📦 Installation

```bash
git clone https://github.com/your-username/csv-anomaly-detector.git
cd csv-anomaly-detector
pip install -r requirements.txt
````

---

## ▶️ Running the App

```bash
streamlit run app.py
```

Then open your browser and go to `http://localhost:8501`.

---

## 📝 Usage

1. Upload your `.csv` file.
2. The app will:

   * Display a preview of your data
   * Run anomaly detection on numerical columns
   * Highlight rows and columns with anomalies
3. Review flagged results and suggested fixes.

---

## 📌 Example Output

* Outlier summary by column
* Skewness values and interpretation
* CSV row indices with anomalies
* Optionally save results to file

---

## 🛠 Technologies Used

* Python (Pandas, NumPy, SciPy)
* Streamlit
* Seaborn / Matplotlib (for optional visualization)

---

## 🔮 Roadmap

* [ ] Add Z-Score and MAD-based detection
* [ ] Integrate Isolation Forest / LOF for multivariate analysis
* [ ] Allow user-defined thresholds and export reports
* [ ] Add categorical anomaly detection support

---

## 🤝 Contributing

Contributions are welcome! If you'd like to add features or fix issues:

1. Fork the repo
2. Create your feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a Pull Request

---

## 📄 License

MIT License

---

## 👩‍💻 Author

LinkedIn: https://www.linkedin.com/in/safura-kasu-544b50281/
Email: safurakasu@gmail.com




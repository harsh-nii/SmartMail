# 📧 SmartMail: Personalized Email Automation Dashboard

**SmartMail** is an intuitive Streamlit-based web application that helps you send personalized bulk emails using the Gmail API. Simply upload a CSV file, compose an email with placeholders, and let SmartMail handle the rest! 🚀

---

## 🚀 Features

- **CSV Upload**: Upload a CSV file containing recipient details.
- **Personalized Emails**: Use placeholders like `{Name}` or `{ColumnName}` to customize each email.
- **Bulk Email Sending**: Authenticate with Gmail to send emails to all recipients in the uploaded file.
- **User-Friendly Dashboard**: A clean and interactive UI for seamless navigation.
- **Real-Time Feedback**: View email-sending progress and responses directly on the dashboard.

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: Gmail API
- **Language**: Python
- **Data Handling**: Pandas

---

## 📂 File Structure

```
SmartMail/
├── app.py                # Main application script
├── credentials.json      # Gmail API credentials (not included in repository for security reasons)
├── example.csv           # Example CSV file with sample data
├── README.md             # Documentation for the project
└── requirements.txt      # Required Python packages
```

---

## 🛠️ Prerequisites

1. **Python** (version 3.7 or higher)
2. **Google Cloud Account** to enable Gmail API and generate `credentials.json`.
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🔧 Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/SmartMail.git
   cd SmartMail
   ```

2. **Enable Gmail API:**
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project or use an existing one.
   - Enable the **Gmail API**.
   - Generate OAuth 2.0 credentials and download the `credentials.json` file.
   - Place the `credentials.json` file in the root directory of the project.

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

4. **Access the app:**
   - Open the link provided in the terminal (default: `http://localhost:8501`).

---

## 📂 Example CSV File

Here’s how your CSV file should look:

| Name    | Email              | CustomField |
|---------|--------------------|-------------|
| Alice   | alice@example.com  | Example1    |
| Bob     | bob@example.com    | Example2    |

- Use the column names (e.g., `{Name}` or `{CustomField}`) as placeholders in the email body.

---

## ✍️ Usage Guide

1. **Upload CSV**: Upload a CSV file with at least an `Email` column.
2. **Compose Email**:
   - Write an email subject.
   - Draft the email body using placeholders (e.g., `{Name}`).
3. **Authenticate Gmail**: Click on "Authenticate & Send Emails" to authenticate with Gmail.
4. **Send Emails**: SmartMail sends personalized emails to each recipient and displays the progress.

---

## ⚠️ Notes

1. The Gmail API has daily limits; ensure you don’t exceed your quota.
2. `credentials.json` should not be shared publicly. Add it to `.gitignore`.

---

## 🤝 Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## 🛡️ License

This project is licensed under the MIT License. See `LICENSE` for more details.

---

## 🙌 Acknowledgments

- [Streamlit](https://streamlit.io/)
- [Google Gmail API](https://developers.google.com/gmail)
- Community for inspiration and feedback.

---

## 🧑‍💻 Author

[Harshini Shivaratri](https://github.com/harsh-nii)

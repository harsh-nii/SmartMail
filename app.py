import streamlit as st
import pandas as pd
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from email.mime.text import MIMEText
import base64

# Set page configuration
st.set_page_config(page_title="SmartMail", page_icon="📧", layout="wide")

# Title and Description
st.title("📧SmartMail")
st.markdown("""
    Use this dashboard to upload a CSV file, compose personalized emails using placeholders, and send them using Gmail.
    - **Step 1**: Upload a CSV file with recipient details (e.g., Name, Email, etc.).
    - **Step 2**: Write the email subject and body. Use placeholders like `{ColumnName}` to personalize.
    - **Step 3**: Authenticate Gmail and send emails in bulk.
""")

# File Upload Section
st.sidebar.header("📂 Upload CSV File")
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"], help="Ensure the CSV includes an 'Email' column.")

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.subheader("Uploaded Data Preview")
    st.dataframe(data, use_container_width=True)

    # Placeholder Information
    st.markdown("### 🛠️ Available Placeholders")
    st.info(", ".join(f"`{{{col}}}`" for col in data.columns))

    # Select Primary Column for Entity Names
    st.sidebar.subheader("⚙️ Settings")
    column = st.sidebar.selectbox("Select Primary Column for Entity Names", data.columns, help="This column will be used to identify entities.")
else:
    st.warning("No file uploaded yet. Please upload a CSV file to proceed.")

# Gmail OAuth Authentication Function
def authenticate_gmail():
    SCOPES = ['https://www.googleapis.com/auth/gmail.send']
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    return creds

# Email Sending Function
def send_email_gmail(creds, subject, body, to_email):
    try:
        service = build('gmail', 'v1', credentials=creds)
        message = MIMEText(body)
        message['to'] = to_email
        message['subject'] = subject
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        service.users().messages().send(userId="me", body={'raw': raw_message}).execute()
        return "✅ Email sent successfully!"
    except Exception as e:
        return f"❌ An error occurred: {e}"

# Email Composition Section
st.sidebar.header("✍️ Compose Email")
subject = st.sidebar.text_input("Enter Email Subject", help="Provide a subject line for the email.")
body = st.sidebar.text_area("Enter Email Body", placeholder="Use placeholders like {Name} to personalize your message.", height=200)

# Authentication and Email Sending
if st.sidebar.button("🚀 Authenticate & Send Emails"):
    if not uploaded_file:
        st.sidebar.error("Please upload a CSV file before sending emails.")
    elif 'Email' not in data.columns:
        st.sidebar.error("The uploaded CSV must include an 'Email' column.")
    elif not subject or not body:
        st.sidebar.error("Please provide both an email subject and body.")
    else:
        creds = authenticate_gmail()  # Authenticate Gmail
        progress = st.progress(0)  # Progress bar

        for index, row in data.iterrows():
            to_email = row.get('Email', '').strip()  # Ensure correct 'Email' column

            if not to_email:
                st.warning(f"Row {index + 1}: No recipient email found. Skipping this entry.")
                continue

            # Replace placeholders with row data
            email_body = body
            for col in data.columns:
                email_body = email_body.replace(f"{{{col}}}", str(row[col]))

            # Send email and display response
            response = send_email_gmail(creds, subject, email_body, to_email)
            st.write(f"**To {to_email}:** {response}")

            # Update progress bar
            progress.progress((index + 1) / len(data))

        st.success("✅ All emails processed!")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit and Gmail API.")

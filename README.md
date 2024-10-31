# Submission Details

- Name: Winnie Chu

# Issues

- Unable to run my application's inference engine on Streamlit due to conflicting dependencies issue (discovered this after hours of troubleshooting). The application is able to run on a local server. Instructions are provided below.

# How to Run App Locally

1. Clone repository using `git clone https://github.com/darewinnie/w-capstone.git`
2. Create virtual environment by entering the following commands in the terminal:
   - `python3 -m venv venv`
   - `source venv/bin/activate`
3. Install dependencies by entering `pip install -r requirements.txt` in the terminal.
4. Create a folder call `.streamlit`
5. Create a file `secrets.toml` in `.streamlit` folder.
   - Enter `password="12345"` in the `secrets.toml` file
6. Create a `.env` file in the project root folder and insert the following:
   - `OPENAI_API_KEY="<YOUR OPENAI KEY>"`
   - `OPENAI_MODEL_ANME="gpt-4o-mini"`
7. Run the application using `streamlit run main.py`.

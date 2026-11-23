# AI Storyboard Creator (Local Setup)

This is the local version of your AI Storyboard Creator. Follow these simple steps to set up and run the application on your computer.

## 🛠️ Prerequisites
Make sure you have **Python 3.8+** installed on your system.

## 📦 Installation
1. Open your terminal (macOS/Linux) or Command Prompt/PowerShell (Windows).
2. Navigate to this unzipped project directory:
   ```bash
   cd path/to/ai_storyboard_local
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## 🔑 Configure API Key
You must set your Groq API key as an environment variable so the application can access it.

*   **Windows (Command Prompt):**
    ```cmd
    set GROQ_API_KEY=your_actual_groq_api_key_here
    ```
*   **Windows (PowerShell):**
    ```powershell
    $env:GROQ_API_KEY="your_actual_groq_api_key_here"
    ```
*   **macOS / Linux:**
    ```bash
    export GROQ_API_KEY="your_actual_groq_api_key_here"
    ```

## 🚀 Running the App
Once your API key is configured, start the application by running:
```bash
python app.py
```
Open the local web link (usually `http://127.0.0.1:7860`) displayed in your terminal to use your interface!

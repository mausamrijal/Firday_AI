# Friday AI - Your Personal Voice-Activated Assistant

Friday AI is a **Python-based personal assistant** that allows you to interact with your computer using **voice commands**. It leverages **Gemini AI** to generate and execute **bash commands** based on your instructions. The tool also includes **safety features** to prevent accidental execution of dangerous commands.

---
## 🚀 Features

✅ **🎤 Voice-to-Text:** Speak to Friday AI, and it will convert your speech into text.  
✅ **🤖 Gemini AI Integration:** Uses Gemini AI to generate appropriate bash commands for your requests.  
✅ **🔒 Safe Command Execution:** Detects dangerous commands (e.g., `rm`, `shutdown`) and asks for confirmation before execution.  
✅ **🔊 Text-to-Speech Feedback:** Provides audible feedback using text-to-speech.  
✅ **🛠️ Customizable:** Easily extendable with additional features or integrations.  

---
## 📥 Installation
speech_recognition: For voice-to-text functionality.

google.generativeai: For interacting with Gemini AI.

os: For executing system commands.

subprocess: For executing bash commands safely.

pyttsx3: For text-to-speech feedback.
Clone the repository:

```bash
git clone https://github.com/your-username/friday-ai.git

# Navigate to the directory
cd friday-ai

#Creating a Virtual Environment
python -m venv env

#macOS and Linux
source env/bin/activate

#macOS and Linux
env\Scripts\activate.bat

# Install dependencies
pip install pyfiglet SpeechRecognition google-generativeai pyttsx3
# Clone the repository





# Run the application
python main.py
```

---
## 📂 Repository Structure

```
friday-ai/
├── main.py                # Main Python script
├── README.md              # Project documentation
├── requirements.txt       # List of dependencies
├── LICENSE                # License file
└── .gitignore             # Files to ignore in Git
```

---
## 🖥️ Screenshots

### 🎉 Welcome Screen
```
  _____ _ _     _    ___   _
 |  ___(_) | __| |  / _ \ (_)
 | |_  | | |/ _` | | | | | |
 |  _| | | | (_| | | |_| | |
 |_|   |_|_|\__,_|  \___/ |_|

Listening...
You said: Open Chrome
Generated command: google-chrome
Executing command: google-chrome
Command executed successfully.
```

---
## 📝 Usage Instructions

1. **Run `main.py`**
2. **Speak your command** (e.g., "Open Chrome")
3. **Friday AI processes and executes the command**
4. **If a dangerous command is detected**, it asks for confirmation before execution
5. **Receives voice feedback about the execution status**

---
## 🛠️ Customization
You can extend **Friday AI** by adding more integrations, commands, or voice processing capabilities. Modify `main.py` and implement your own features!

---
## 📜 License
This project is licensed under the **MIT License**.

---
## 🤝 Contributing
Feel free to fork the repository, make changes, and submit a **pull request**! 😊


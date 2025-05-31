# AI Travel Agent - Simplified

A streamlined AI-powered travel planning assistant built with CrewAI and Google's Gemini AI. This tool helps you choose the perfect travel destination based on your preferences, budget, and travel dates.

## 🌟 Features

- **Smart Destination Recommendations**: Get personalized city suggestions based on your interests
- **Real-time Information**: Uses live web search to provide current travel information
- **Google Gemini Integration**: Powered by Google's advanced AI for intelligent responses
- **Simple Setup**: Minimal configuration required to get started
- **Comprehensive Debugging**: Built-in diagnostic tools to troubleshoot API issues

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google Cloud account with Generative AI API access
- Serper.dev account for web search functionality

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/naakaarafr/AI-Travel-Agent-Simplified.git
   cd AI-Travel-Agent-Simplified
   ```

2. **Install dependencies**
   ```bash
   pip install crewai langchain-google-genai crewai-tools python-dotenv requests
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   SERPER_API_KEY=your_serper_api_key_here
   ```

### Getting API Keys

#### Google API Key
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the **Generative AI API**
4. Go to **APIs & Services > Credentials**
5. Click **Create Credentials > API Key**
6. Copy the API key to your `.env` file

#### Serper API Key
1. Visit [Serper.dev](https://serper.dev/)
2. Sign up for a free account
3. Get your API key from the dashboard
4. Add it to your `.env` file

## 🔧 Usage

### 1. Test Your Setup (Recommended)

Before running the main application, test your API connections:

```bash
python debug_api.py
```

This will verify:
- ✅ Internet connectivity
- ✅ Google API key validity
- ✅ Serper API key functionality
- ✅ CrewAI + Gemini integration

### 2. Run the Travel Planner

```bash
python crew.py
```

Follow the interactive prompts:
- **Origin**: Where you're traveling from
- **Cities**: Cities you're considering
- **Travel dates**: When you plan to travel
- **Interests**: Your travel preferences (food, museums, nightlife, etc.)

### Example Session

```
AI Trip Planner - Simplified Version
==================================================
From where are you traveling? (e.g., New York): London
What cities are you considering? (e.g., Paris, Tokyo): Barcelona, Amsterdam, Prague
When are you traveling? (e.g., June 2024): September 2024
What are your interests? (e.g., food, museums): architecture, local cuisine, nightlife

🚀 Planning your trip...
```

## 📁 Project Structure

```
AI-Travel-Agent-Simplified/
├── crew.py           # Main application file
├── config.py         # Configuration to force Gemini usage
├── debug_api.py      # API diagnostic tool
├── .env              # Environment variables (create this)
└── README.md         # This file
```

## 🛠️ Files Explained

### `crew.py`
The main application that:
- Creates a travel expert AI agent
- Processes user input
- Generates personalized destination recommendations
- Handles errors gracefully

### `config.py`
Configuration file that:
- Forces CrewAI to use Gemini exclusively
- Prevents OpenAI API calls
- Validates environment variables

### `debug_api.py`
Diagnostic utility that:
- Tests internet connectivity
- Validates API keys
- Verifies CrewAI integration
- Provides troubleshooting guidance

## 🔍 Troubleshooting

### Common Issues

**❌ Google API Key Error**
```
Solution: 
1. Ensure Generative AI API is enabled in Google Cloud Console
2. Check that billing is set up on your Google Cloud account
3. Verify the API key is correctly added to .env file
```

**❌ Serper API Error**
```
Solution:
1. Verify your Serper API key at serper.dev
2. Check that you haven't exceeded your API quota
3. Ensure the key is correctly formatted in .env
```

**❌ Import Errors**
```bash
# Install missing dependencies
pip install crewai langchain-google-genai crewai-tools python-dotenv requests
```

### Debug Mode

Run the diagnostic tool for detailed troubleshooting:
```bash
python debug_api.py
```

## 🎯 How It Works

1. **Agent Creation**: Creates a specialized travel expert AI agent using Gemini
2. **User Input**: Collects your travel preferences and constraints
3. **Web Search**: Uses Serper API to gather current travel information
4. **AI Analysis**: Gemini processes the data and generates recommendations
5. **Output**: Provides personalized destination advice with reasoning

## 🌐 API Usage

This project uses:
- **Google Gemini 2.0 Flash**: For intelligent text generation and reasoning
- **Serper API**: For real-time web search capabilities
- **CrewAI Framework**: For orchestrating AI agents and tasks

## 📋 Requirements

```
crewai>=0.1.0
langchain-google-genai>=1.0.0
crewai-tools>=0.1.0
python-dotenv>=1.0.0
requests>=2.25.0
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [CrewAI](https://github.com/joaomdmoura/crewAI) for the AI agent framework
- [Google Gemini](https://deepmind.google/technologies/gemini/) for the language model
- [Serper](https://serper.dev/) for web search capabilities

## 📞 Support

If you encounter issues:

1. Run `python debug_api.py` first
2. Check the troubleshooting section above
3. Open an issue on GitHub with:
   - Error message
   - Steps to reproduce
   - Output from debug_api.py

---

**Made with ❤️ by [naakaarafr](https://github.com/naakaarafr)**

*Happy Traveling! ✈️🌍*

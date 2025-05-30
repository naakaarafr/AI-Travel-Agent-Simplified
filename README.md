# 🌍 AI Travel Agent - Simplified

An intelligent multi-agent travel planning system powered by Google's Gemini AI and CrewAI. This application uses specialized AI agents to analyze destinations, provide local insights, and create comprehensive 7-day travel itineraries tailored to your preferences.

## 🚀 Features

### 🤖 Multi-Agent Architecture
- **City Selection Agent**: Analyzes weather, costs, activities, and traveler preferences to recommend the best destination
- **Local Expert Agent**: Provides insider knowledge, hidden gems, cultural insights, and authentic local recommendations
- **Travel Concierge Agent**: Creates detailed itineraries with accommodations, dining, activities, and budget planning

### 🔧 Comprehensive Tools
- **Weather Forecasting**: Real-time weather data for travel planning
- **Flight Price Search**: Find the best flight deals between destinations
- **Hotel Recommendations**: Accommodations across different budget ranges
- **Restaurant Discovery**: Local dining recommendations and authentic cuisine
- **Attraction Finding**: Activities and sights matching your interests
- **Hidden Gems**: Off-the-beaten-path local secrets
- **Cultural Insights**: Local customs, etiquette, and cultural tips
- **Transportation**: Local transport options and navigation tips
- **Event Discovery**: Seasonal events, festivals, and special activities
- **Safety Information**: Travel advisories and safety recommendations
- **Budget Calculator**: Expense calculations and cost estimations

## 📋 Prerequisites

Before you begin, ensure you have:

- Python 3.8 or higher
- Google Cloud Platform account with Generative AI API enabled
- Serper.dev account for web search functionality

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/naakaarafr/AI-Travel-Agent-Simplified.git
   cd AI-Travel-Agent-Simplified
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   Create a `.env` file in the project root:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   SERPER_API_KEY=your_serper_api_key_here
   ```

## 🔑 API Setup

### Google Gemini API
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the **Generative AI API**
4. Create credentials (API Key)
5. Add the API key to your `.env` file

### Serper API (Web Search)
1. Visit [Serper.dev](https://serper.dev/)
2. Sign up for a free account
3. Generate an API key
4. Add the API key to your `.env` file

## 🚀 Usage

### Quick Start
```bash
python crew.py
```

### Diagnostic Testing
Before running the main application, test your setup:
```bash
python debug_api.py
```

This will verify:
- ✅ Internet connectivity
- ✅ Google API key validity
- ✅ Serper API functionality
- ✅ CrewAI + Gemini integration

### Interactive Experience
When you run the application, you'll be prompted for:

1. **Origin City**: Where you're traveling from (e.g., "New York")
2. **Destination Options**: Cities you're considering (e.g., "Paris, Tokyo, Barcelona")
3. **Travel Dates**: When you plan to travel (e.g., "June 15-22, 2024")
4. **Interests**: Your travel preferences (e.g., "food, museums, nightlife")

## 📁 Project Structure

```
ai-travel-agent-simplified/
├── agents.py          # AI agent definitions and configurations
├── tasks.py           # Task definitions for each agent
├── tools.py           # Custom tools for web search, calculations, etc.
├── crew.py            # Main application and crew orchestration
├── debug_api.py       # API diagnostic and testing script
├── config.py          # Configuration and environment setup
├── requirements.txt   # Python dependencies
├── .env              # Environment variables (create this)
└── README.md         # This file
```

## 🧠 How It Works

### 1. City Selection Phase
The **City Selection Agent** analyzes:
- Weather conditions and forecasts
- Flight costs from your origin
- Accommodation availability and pricing
- Seasonal events and festivals
- Safety considerations
- Alignment with your interests

### 2. Local Expert Phase
The **Local Expert Agent** provides:
- Hidden gems and local secrets
- Cultural insights and etiquette tips
- Authentic dining recommendations
- Best times to visit attractions
- Local transportation advice
- Safety tips and areas to avoid

### 3. Itinerary Creation Phase
The **Travel Concierge Agent** creates:
- Detailed 7-day daily schedules
- Specific hotel recommendations with pricing
- Restaurant suggestions for every meal
- Transportation logistics
- Comprehensive budget breakdown
- Weather-appropriate packing list

## 💡 Example Output

The system generates a comprehensive travel plan including:

```markdown
# 7-Day Tokyo Itinerary - AI Travel Agent

## Day 1: Arrival & Shibuya Exploration
**Morning (9:00 AM)**
- Arrive at Haneda Airport
- Take Airport Express to Shibuya (¥400, 30 minutes)
- Check into Hotel Gracery Shinjuku (¥12,000/night)

**Afternoon (2:00 PM)**
- Lunch at Sushi Jiro (¥3,000)
- Explore Shibuya Crossing
- Visit Meiji Shrine (Free entry)

**Evening (7:00 PM)**
- Dinner at Izakaya Torikizoku (¥2,500)
- Explore Golden Gai district

## Budget Breakdown
- Accommodation: ¥84,000 (7 nights)
- Food: ¥21,000 (¥3,000/day)
- Transportation: ¥5,000
- Activities: ¥8,000
- **Total: ¥118,000 (~$800 USD)**
```

## 🔧 Customization

### Adding New Tools
Create custom tools in `tools.py`:

```python
@tool("Your custom tool")
def custom_tool(parameter: str) -> str:
    """
    Description of what your tool does.
    
    Args:
        parameter (str): Description of the parameter
    
    Returns:
        str: Description of the return value
    """
    # Your implementation here
    return "Tool result"
```

### Modifying Agent Behavior
Adjust agent personalities and goals in `agents.py`:

```python
custom_agent = Agent(
    role="Your Custom Role",
    goal="Your specific goal",
    backstory="Your agent's background",
    tools=YOUR_TOOLS,
    llm=llm
)
```

## 🐛 Troubleshooting

### Common Issues

**"API key not found" Error**
- Ensure your `.env` file is in the project root
- Check that variable names match exactly: `GOOGLE_API_KEY`, `SERPER_API_KEY`

**"Failed to initialize Gemini LLM" Error**
- Verify your Google API key is valid
- Ensure Generative AI API is enabled in Google Cloud Console
- Check if billing is enabled on your Google Cloud account

**"Connection timeout" Error**
- Check your internet connection
- Try running `debug_api.py` to diagnose connectivity issues
- Consider firewall or proxy restrictions

### Getting Help
1. Run `python debug_api.py` to identify specific issues
2. Check the console output for detailed error messages
3. Ensure all API keys are properly configured

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- [CrewAI](https://github.com/joaomdmoura/crewAI) - Multi-agent framework
- [Google Gemini](https://deepmind.google/technologies/gemini/) - Large language model
- [Serper.dev](https://serper.dev/) - Web search API
- [LangChain](https://langchain.com/) - LLM application framework

## 👨‍💻 Author

**naakaarafr**
- GitHub: [@naakaarafr](https://github.com/naakaarafr)

---

⭐ **Star this repo if you found it helpful!**

*Built with ❤️ and AI*

# Simplified crew.py with better error handling and debugging
import os
from dotenv import load_dotenv

# Load environment variables first
load_dotenv()

# FORCE CrewAI to avoid OpenAI
os.environ["OPENAI_API_KEY"] = ""
os.environ["OPENAI_MODEL_NAME"] = ""

print("🔧 Starting AI Trip Planner...")
print(f"📍 Google API Key: {'✅ Found' if os.getenv('GOOGLE_API_KEY') else '❌ Missing'}")
print(f"🔍 Serper API Key: {'✅ Found' if os.getenv('SERPER_API_KEY') else '❌ Missing'}")

try:
    from crewai import Agent, Task, Crew, Process
    from langchain_google_genai import ChatGoogleGenerativeAI
    from crewai_tools import SerperDevTool
    print("✅ All imports successful")
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Run: pip install crewai langchain-google-genai crewai-tools")
    exit(1)

# Initialize Gemini LLM with error handling
try:
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",  # Use stable model
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.5,
        verbose=False  # Reduce verbosity for cleaner output
    )
    
    # Test the LLM connection
    test_response = llm.invoke("Hello")
    print("✅ Gemini LLM connection successful")
    
except Exception as e:
    print(f"❌ Failed to initialize Gemini LLM: {e}")
    print("Please check your GOOGLE_API_KEY in the .env file")
    exit(1)

# Initialize search tool
try:
    search_tool = SerperDevTool()
    print("✅ Search tool initialized")
except Exception as e:
    print(f"❌ Failed to initialize search tool: {e}")
    print("Please check your SERPER_API_KEY in the .env file")
    exit(1)

# Create a simple agent for testing
city_agent = Agent(
    role="City Selection Expert",
    goal="Help select the best travel destination",
    backstory="You are an expert travel advisor who helps people choose destinations.",
    llm=llm,
    tools=[search_tool],
    verbose=True,
    allow_delegation=False
)

# Create a simple task
city_task = Task(
    description="""
    Based on the user's input, recommend the best city for travel.
    Consider weather, costs, and activities.
    
    User details:
    - Origin: {origin}
    - Cities considering: {cities}
    - Travel dates: {date_range}
    - Interests: {interests}
    
    Provide a brief recommendation with reasoning.
    """,
    agent=city_agent,
    expected_output="A city recommendation with brief reasoning"
)

def get_simple_input():
    """Get simplified user input"""
    print("\n" + "="*50)
    print("AI Trip Planner - Simplified Version")
    print("="*50)
    
    origin = input("From where are you traveling? (e.g., New York): ").strip()
    cities = input("What cities are you considering? (e.g., Paris, Tokyo): ").strip()
    date_range = input("When are you traveling? (e.g., June 2024): ").strip()
    interests = input("What are your interests? (e.g., food, museums): ").strip()
    
    return origin, cities, date_range, interests

def main():
    """Main function with comprehensive error handling"""
    try:
        # Get user input
        origin, cities, date_range, interests = get_simple_input()
        
        if not all([origin, cities, date_range, interests]):
            print("❌ Please provide all required information")
            return
        
        print("\n🚀 Planning your trip...")
        
        # Create crew
        crew = Crew(
            agents=[city_agent],
            tasks=[city_task],
            process=Process.sequential,
            verbose=True,
            manager_llm=llm
        )
        
        # Execute with detailed error handling
        print("🔄 Starting crew execution...")
        result = crew.kickoff(inputs={
            'origin': origin,
            'cities': cities,
            'date_range': date_range,
            'interests': interests
        })
        
        print("\n" + "="*60)
        print("🎉 TRIP RECOMMENDATION")
        print("="*60)
        print(result)
        
    except KeyboardInterrupt:
        print("\n❌ Cancelled by user")
    except Exception as e:
        print(f"\n❌ Error during execution: {e}")
        print(f"Error type: {type(e).__name__}")
        
        # Provide specific error guidance
        if "401" in str(e) or "API key" in str(e):
            print("🔑 This looks like an API key issue")
            print("1. Check your GOOGLE_API_KEY in .env file")
            print("2. Make sure the API key has Generative AI API enabled")
            print("3. Check if you have billing enabled on Google Cloud")
        elif "timeout" in str(e).lower() or "connection" in str(e).lower():
            print("🌐 This looks like a connection issue")
            print("1. Check your internet connection")
            print("2. Try again in a few minutes")
            print("3. Check if your firewall is blocking the connection")
        else:
            print("🔧 Run debug_api.py first to diagnose the issue")

if __name__ == "__main__":
    main()
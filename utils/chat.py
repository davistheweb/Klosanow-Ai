import os
from google import genai
from dotenv import load_dotenv
from helper import GET_RESPONSIBILITIES
from fastapi import HTTPException
load_dotenv()


def Klosanow_Chat(prompt = '') ->str:
    try:
        client = genai.Client(api_key=  os.getenv('GEMINI_API_KEY'));
        
        RESPONSIBILITIES = GET_RESPONSIBILITIES()
        
        # recent_chats = [
    	# {'role': 'user', 'text': 'Hey Man' },
    	# {'role': 'model', 'text' : 'Hey there! How can I help you today?'},
    	# {'role':  'user', 'text': 'What is python snake'},
    	# {'role' : 'model', 'text' : "That's an interesting question because \"Python\" can refer to two very different things!.  **The Animal:** A **python** is a type of large, non-venomous constrictor snake native to Africa, Asia, and Australia. They kill their prey by coiling around them and suffocating them (constriction) rather than using venom. There are many different species, including the reticulated python (one of the longest snakes in the world), the ball python (a popular pet), and the Burmese python. **The Programming Language:** **Python** is also a very popular and powerful high-level **programming language**. It's known for its readability, versatility, and extensive libraries. It's widely used for:*   Web development (e.g., Django, Flask) *   Data science and analysis *   Artificial intelligence and machine learning*   Automation and scripting *   Scientific computing*   Game development **Which one were you curious about?** Let me know, and I can tell you more!"}
		# ]
        
        response = client.models.generate_content( model="gemini-2.0-flash", contents=f"{RESPONSIBILITIES} \n User_Chat:{prompt}", )
        
        return response.text
    except Exception as e:
     raise HTTPException(status_code=500, detail=str(e))
    # print(str(e))

# print(Klosanow_Chat("Who are you and What was my last prompt"))
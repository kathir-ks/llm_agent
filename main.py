import google.generativeai as genai

from agent import Agent

GOOGLE_API_KEY = "AIzaSyCc4o3_ZNbpwLGisP1SRw_hQaWTzo0wavE"

genai.configure(api_key = GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

agent = Agent(name="Engineer", system_message = "You act as an engineer to help me with a house plan", model= model, max_iter = 10)

agent._start_("Explain the basics to consider while making a house plan")
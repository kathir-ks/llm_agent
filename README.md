# llm_agent
 An agent library written using google's generativeai , a python package used to access the models gemini pro and gemini pro vision.[In early stages]

## Single Agent Chat

```
import google.generativeai as genai

from agent import Agent
from groupchat import GroupChat

GOOGLE_API_KEY = ""

genai.configure(api_key = GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

agent = Agent(name="Engineer", system_message = "You are an engineer. You will help me build a house plan", model= model, max_iter = 10)

agent._start_("Start creating the plan")
```

## Multi Agent Chat

```
import google.generativeai as genai

from agent import Agent
from groupchat import GroupChat

GOOGLE_API_KEY = ""

genai.configure(api_key = GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

user_agent = Agent(name="user", system_message="create a neuron emitter.First start with the help from scientist. Ask for the user input often", model = model , max_iter = 10)

agent1 = Agent(name="Engineer", system_message = "You are an engineer. You will build a neuron emitter based on the guidance from a scientist.You can ask help to a Scientist whenever needed.You can also ask feedback from a user", model= model, max_iter = 10)

agent2 = Agent(name="Scientist", system_message = "You are an scientist. You will help the Engineer data about neurons. You can also ask feedback from user. Ask for the user input ofter", model = model , max_iter=10)

group = GroupChat(agents=[user_agent, agent1, agent2], model=model)

group._run_conversation_("Start the process of building a neuron emitter", agent = user_agent)
```


Got inspired from Autogen

Feel free to contact me if you wish to contribute (mailto:kathirksw@gmail.com)





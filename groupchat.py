from agent import Agent
from typing import Dict, List, Optional, Union

class GroupChat:
    def __init__(self, agents:List[Agent], model, max_iter:int = 10):
        self.agents = agents
        self.messages = ""
        self.model = model
        self.max_iter = max_iter
        self.agent: Optional[Agent] = agents[0] if agents else None

        # self.messages = f"You are a conversation manager. Based on a conversation history you will choose the next agent to speak. You have the follwing agents {self.agent_names} and their roles are given by the following messages {self._sys_messages_}. Select the agent the will be the best to speak next"
        # for member in self.members:
        #     self.messages += member.history

    def _sys_messages_(self):
        return [agent.system_message for agent in self.agents]

    def _agent_by_name_(self, name:str) -> Agent:
        for agent in self.agents:
            if agent.name == name:
                return agent

    def _run_conversation_(self, prompt:str, agent:Agent):
        self.agent = agent
        self.messages += f"\"text\":"+ prompt + f"\"role\":\"{self.agent.name}\""

        for i in range(self.max_iter):
            next = self._select_next_()
            next = next.text
            print(next)
            self.agent = self._agent_by_name_(next)

            if self.agent is not None:
                response = self.agent.__generate__(agent.history)
                if self.agent.name!="user":
                    response = response.text
                if self.agent.name == "user" and "exit" in response:
                    print("Terminated by user...")
                    return

                if self.agent.name != "user":
                    print(response)
            
                self.messages += f"\"text\":"+ response + f"\"role\":\"{self.agent.name}\""
                
                print(self.messages)

                for ag in self.agents:
                    if ag.name != self.agent.name:
                        ag.history = ag.history + f"\"text\":"+ response + f"\"role\":\"{self.agent.name}\""
            else:
                print(f"No agent found with the name: {next}")
                # Handle this case according to your requirements

    def agent_names(self):
        return [agent.name for agent in self.agents]
    
    def _select_next_(self):
        return self.model.generate_content(self.messages+f"\"text\":\"Based on the above conversation choose the next agent to speak from {self.agent_names()} only return the agent name, \"role\":\"system\"")
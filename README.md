## Multi-Agent AI Search Assistant

##  ![image](https://github.com/user-attachments/assets/7df11bdd-6df9-4616-9699-f9b03d6184b4)


### Project Overview
AI-powered Multi-Agent Search Assistant is a cutting-edge system that combines multiple AI agents to search the web, analyze data, and craft the most accurate and contextually relevant answers. This project leverages powerful frameworks like LangChain, LangGraph, and Streamlit to deliver a seamless and interactive experience. Whether you're seeking up-to-date news or complex research answers, this assistant is designed to provide you with insightful, real-time responses.

#### Key Features
AI Agents at Work: Harnesses multiple agents to perform web searches and intelligently craft responses.

Real-Time Search and Answering: Integrates real-time web search with intelligent answer generation.

Streamlit User Interface: Provides a beautiful and interactive UI for users to ask questions and receive AI-powered answers instantly.

Customizable Prompts: Allows tailored search and response generation based on specific user queries.

#### Tech Stack
##### LangChain: A robust framework for building AI-driven applications, used here for managing LLM chains and interacting with large language models.

##### LangGraph: A powerful graph-based framework for representing, executing, and chaining agent-based workflows.

##### Streamlit: An easy-to-use tool for creating beautiful, interactive UIs for machine learning and data science applications.

##### OpenAI GPT-3.5: Utilized for generating responses based on search results.

##### Tavily: A dynamic tool for fetching real-time search results from the web.

#### Features Overview
Multi-Agent Workflow
This project utilizes a two-step process involving:

##### Search Agent: Fetches relevant search results.

##### Answer Agent: Synthesizes those results to provide the final answer.

#### Real-Time Information
By connecting to the Tavily search tool, the assistant retrieves up-to-date information from the web, ensuring that users get answers relevant to the most recent events.

#### Streamlit UI
The Streamlit interface allows users to ask questions naturally, making it easy to interact with the assistant. The UI is simple yet effective, offering a smooth and intuitive experience.

#### Custom Answer Generation
The answer generation leverages GPT-3.5 through LangChain, creating responses based on search results and ensuring that answers are tailored to the question asked.

#### How It Works
##### Search Agent:

The user asks a question, and the search agent uses the Tavily tool to perform a web search and retrieve relevant results.

##### Answer Agent:

The answer agent then takes the search results and crafts a detailed, insightful answer using GPT-3.5.

#### UI Integration:

The entire process is handled behind the scenes, while the user interacts seamlessly with the app through an intuitive Streamlit interface.

##### Example Use Cases
###### Stay Up-to-Date: Ask about the latest news in AI, technology, or any other field, and get real-time updates.

###### Research Assistance: Get in-depth answers to your academic or professional questions.

###### Problem-Solving: Whether it's a complex question or a simple inquiry, this assistant provides reliable solutions.

##### Future Improvements
More Sources: Integrate additional data sources and APIs to expand the range of information available.

Contextual Memory: Allow the system to remember previous queries for a more personalized experience.

Voice Interaction: Add a voice input feature for hands-free question-asking.

#### Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request. If you have suggestions or ideas for improvement, open an issue, and we'll discuss it!

##### License
This project is licensed under the MIT License – see the LICENSE file for details.

##### Built By
Satyam Tiwari

##### Acknowledgements
###### LangChain: For providing a framework for building LLM-based applications.

###### LangGraph: For enabling graph-based workflows.

###### Streamlit: For making it easy to create beautiful and functional UIs.

###### OpenAI: For providing GPT models.

###### Tavily: For providing a great web search tool.

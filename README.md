# **Project: Multi-Agent System with Web Search and Groq Integration**

This project demonstrates a **multi-agent system** where agents collaborate to perform tasks such as web searching, information retrieval, and response generation. The system leverages **Groq's LLM (Llama 3.1 70B)** for natural language understanding and **DuckDuckGo** for real-time web searches. Each agent is designed to handle specific tasks, ensuring modularity, scalability, and efficiency.

---

## **Key Features**
1. **Multi-Agent Architecture**: Multiple agents work together, each specializing in a specific task (e.g., web search, data processing, response generation).
2. **Web Search Integration**: Uses **DuckDuckGo** to perform real-time web searches and retrieve relevant information.
3. **LLM-Powered Responses**: Leverages **Groq's Llama 3.1 70B** model for generating accurate, context-aware, and well-structured responses.
4. **Task Specialization**: Each agent is designed with a specific role, ensuring efficient task distribution and collaboration.
5. **Transparency and Debugging**: Supports `debug_mode` and `show_tool_calls` for better development, troubleshooting, and transparency.
6. **Streaming Responses**: Provides real-time streaming of responses for a seamless user experience.

---

## **Agents in the System**
1. **Web Search Agent**:
   - **Role**: Performs web searches using **DuckDuckGo**.
   - **Features**:
     - Retrieves real-time information from the web.
     - Ensures responses include the source of information for credibility.
   - **Example Task**: "Who is Elon Musk?"

2. **Data Processing Agent**:
   - **Role**: Processes and structures the data retrieved by the Web Search Agent.
   - **Features**:
     - Cleans and organizes raw data.
     - Prepares data for further analysis or response generation.

3. **Response Generation Agent**:
   - **Role**: Generates concise and accurate responses using **Groq's LLM**.
   - **Features**:
     - Combines processed data with natural language generation.
     - Ensures responses are context-aware and well-structured.

---

## **Use Cases**
- **Collaborative Information Retrieval**: Agents work together to find, process, and present information from the web.
- **Research and Analysis**: Assist researchers by gathering, organizing, and summarizing data from multiple sources.
- **Fact-Checking and Verification**: Verify information by retrieving and citing credible sources.
- **Educational Assistance**: Provide students and learners with accurate, well-referenced, and easy-to-understand answers.

---

## **Example Workflow**
1. **User Query**: A user asks a question, e.g., "Who is Elon Musk?"
2. **Web Search Agent**: Performs a web search using **DuckDuckGo** and retrieves relevant information.
3. **Data Processing Agent**: Processes the raw data, ensuring it is clean and structured.
4. **Response Generation Agent**: Generates a concise and well-structured response using **Groq's LLM**.
5. **Output**: The final response is streamed to the user in real-time, including the source of information.

---

## **Dependencies**
- `phi.agent`: For creating and managing agents.
- `phi.model.groq`: For integrating Groq's LLM.
- `phi.tools.duckduckgo`: For web search functionality.
- `dotenv`: For loading environment variables (e.g., API keys).

---

## **Environment Variables**
- Ensure your `.env` file contains the necessary API keys for **Groq** and any other required services.

---

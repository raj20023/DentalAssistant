# Clinic Appointment Booking AI Assistant

This project is a basic AI assistant built using Python and LangChain that simulates booking an appointment for a dental clinic. The assistant handles a simple conversation flow, asking for a date and time to book an appointment based on user input.

## Features

- **Natural Language Understanding:** Understands when a user wants to book an appointment.
- **Dynamic Conversation Flow:** Responds dynamically and contextually to user inputs.
- **Simulated Appointment Booking:** Simulates the booking process by storing appointment details in memory.

## Prerequisites

- Python 3.8 or higher
- An OpenAI API key

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/clinic-appointment-ai-assistant.git
    cd clinic-appointment-ai-assistant
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your OpenAI API key:**

   Ensure you have your OpenAI API key set up as an environment variable. You can do this by adding the following line to your shell configuration file (e.g., `.bashrc`, `.zshrc`) or by setting it directly in your terminal session:

   ```bash
   export OPENAI_API_KEY='your_openai_api_key'
   ```

   Replace `'your_openai_api_key'` with your actual OpenAI API key.

   On Windows Command Prompt, use:

   ```cmd
   set OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

1. **Run the Python script:**

   ```bash
   python app.py
   ```

2. **Interact with the AI Assistant:**

   Start a conversation by typing messages. The AI assistant will respond dynamically. To book an appointment, provide a request like "I would like to book an appointment," and follow the prompts.

   Example conversation:
   ```plaintext
   Patient: Hi, I would like to book an appointment.
   Agent: Can you provide the date for the appointment?
   Patient: August 10th
   Agent: Can you provide the time for the appointment?
   Patient: 10 AM
   Agent: Booking your appointment for August 10th at 10 AM... Done! Your appointment is confirmed.
   ```

## Project Structure

- `app.py`: The main Python script that runs the AI assistant.
- `requirements.txt`: Lists all Python dependencies required for the project.
- `README.md`: Project documentation and setup instructions.

## How It Works

1. **Initialize LangChain:** Sets up a basic conversational agent using LangChain's `ChatOpenAI` model.
2. **Conversation Flow Management:** The assistant detects when a user wants to book an appointment using keyword matching.
3. **Simulated Booking:** Once the date and time are provided, it confirms the appointment.

## Future Enhancements

- Integrate with real scheduling APIs (e.g., Google Calendar, Outlook).
- Add more robust natural language understanding (NLU) for varied user inputs.
- Improve conversation flow for error handling and additional features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain) for the conversational agent framework.
- [OpenAI](https://openai.com) for the language model API.

## Contact

For any questions or feedback, please contact [rajp20023@gmail.com](mailto:rajp20023@gmail.com).

### Key Updates:
- **API Key Setup Instructions:** Added instructions to set up the OpenAI API key as an environment variable.
- **Minor Formatting:** Clarified sections for better readability.

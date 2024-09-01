from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# Initialize the chat model
chat = ChatOpenAI(
    temperature=0.7
)  # Ensure your OpenAI API key is set as an environment variable

# Dictionary to store the state of the conversation
appointment_details = {"date": None, "time": None}
booking_requested = False  # Flag to track if a booking request was made


def generate_response(messages):
    """
    Generate a response from the AI model based on the provided messages.

    Args:
        messages (list): List of messages in the conversation.

    Returns:
        str: The AI-generated response.
    """
    return chat.invoke(messages).content


def book_appointment():
    """
    Simulate booking an appointment using the stored details.

    Returns:
        str: Confirmation message for the appointment.
    """
    return f"Booking your appointment for {appointment_details['date']} at {appointment_details['time']}... Done! Your appointment is confirmed."


def is_booking_request(user_input):
    """
    Check if the user's input indicates a request to book an appointment.

    Args:
        user_input (str): The input message from the user.

    Returns:
        bool: True if the input contains keywords related to booking, False otherwise.
    """
    keywords = ["appointment", "book", "schedule", "reservation"]
    return any(keyword in user_input.lower() for keyword in keywords)


def conversation_flow():
    """
    Manage the conversation flow for booking an appointment.
    Asks for date and time based on user input and confirms the booking.
    """
    global booking_requested

    messages = [
        SystemMessage(
            content="You are an AI assistant for a dental clinic. Your job is to help book appointments."
        )
    ]

    user_input = input("Patient: ")
    messages.append(HumanMessage(content=user_input))

    while True:
        if is_booking_request(user_input):
            booking_requested = True

        if booking_requested:
            if appointment_details["date"] is None:
                user_date = input(
                    "Agent: Can you provide the date for the appointment? \nPatient: "
                )
                appointment_details["date"] = user_date
                messages.append(
                    HumanMessage(
                        content=f"The appointment date is {user_date}."
                    )
                )

            if appointment_details["time"] is None:
                user_time = input(
                    "Agent: Can you provide the time for the appointment? \nPatient: "
                )
                appointment_details["time"] = user_time
                messages.append(
                    HumanMessage(
                        content=f"The appointment time is {user_time}."
                    )
                )

            if appointment_details["date"] and appointment_details["time"]:
                confirmation = book_appointment()
                print(f"Agent: {confirmation}")
                break

        response = generate_response(messages)
        print(f"Agent: {response}")

        user_input = input("Patient: ")
        messages.append(HumanMessage(content=user_input))


# Run the conversation flow
conversation_flow()

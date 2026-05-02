# main.py

def classify_complaint(text):
    if "delay" in text.lower():
        return "Flight Delay Issue"
    elif "baggage" in text.lower():
        return "Baggage Issue"
    else:
        return "General Query"


def generate_response(category):
    responses = {
        "Flight Delay Issue": "We apologize for the delay. Please check updated timings.",
        "Baggage Issue": "Please contact baggage support at the airport.",
        "General Query": "Our support team will assist you shortly."
    }
    return responses.get(category, "Support will contact you.")


if __name__ == "__main__":
    complaint = input("Enter complaint: ")
    category = classify_complaint(complaint)
    response = generate_response(category)

    print("Category:", category)
    print("Response:", response)
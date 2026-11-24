from openai import OpenAI

client = OpenAI()


def verify(customer):
    # DEMO: sensitive fields are sent to the model in the prompt.
    prompt = f"Check this applicant. SSN: {customer.ssn}, born {customer.date_of_birth}, card {customer.card_number}"
    return client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
    )

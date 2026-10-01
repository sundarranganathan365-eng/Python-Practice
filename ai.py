from google import genai

client = genai.Client(api_key="")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="create a quote to the sentence here " + ask
)
ask=input("WHAT the mood ")
print(response.text)

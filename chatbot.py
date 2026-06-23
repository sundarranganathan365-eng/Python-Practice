import google.generativeai as genai
genai.configure(api_key="")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=input("You:")
)

print(response.text)
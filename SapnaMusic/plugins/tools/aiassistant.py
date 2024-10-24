import requests
import urllib.parse

def ask_query(query, model=None):
    default_model = 'claude-sonnet-3.5'
    system_prompt = None

    if model is None or model == default_model:
        system_prompt = "You are a helpful assistant. Your name is Nexio, and your owner's name is Sachin, known as @V_VIP_OWNER "

    encoded_query = urllib.parse.quote(query)
    encoded_system_prompt = urllib.parse.quote(system_prompt) if system_prompt else ""

    model = model or default_model
    url = f"https://chatwithai.codesearch.workers.dev/?chat={encoded_query}&model={model}"

    if system_prompt:
        url += f"&system={encoded_system_prompt}"

    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("result", "No response found.")
    else:
        return "Error fetching response from API."

print(ask_query("who are you"))

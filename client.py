def chat_with_gemini(messages, model="google/gemini-2.5-pro"):
    import os
    import requests
    from dotenv import load_dotenv
    load_dotenv()
    
    
    api_key = os.getenv("OPENROUTER_API_KEY")
    base_url = os.getenv("OPENROUTER_API_BASE_URL", "https://openrouter.ai/api/v1")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": messages,
    }

    # print("🔽 Request payload:")
    # print(payload)

    response = requests.post(base_url, headers=headers, json=payload)

    # print("🔼 Raw Response Text:")
    # print(response.text) 

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Gemini Error: {response.status_code} - {response.text}")

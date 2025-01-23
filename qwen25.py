from phi.tool import Tool

class Qwen25(Tool):
    def __init__(self, api_key, api_base="YOUR_API_BASE"): # Replace with your base URL
        super().__init__(name="Qwen-2.5")
        self.api_key = api_key
        self.api_base = api_base

    def execute(self, text):
        import requests
        headers = {"Authorization": f"Bearer {self.api_key}"} # Adapt authentication as needed
        data = {"prompt": text} # Adjust request body as needed per API spec
        response = requests.post(f"{self.api_base}/v1/chat/completions", headers=headers, json=data).json()
        return response.get("choices", [{}])[0].get("message", {}).get("content", "")  # Extract response text, adjust based on your API's response structure

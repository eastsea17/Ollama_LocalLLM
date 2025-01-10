import requests

# Ollama 설정
ollama_base_url = "http://localhost:11434"  # Ollama API 주소
model_name = "gemma2"  # 사용할 모델 이름

def generate_with_ollama(prompt, context=[]):
    """Ollama API를 사용하여 텍스트를 생성하는 함수"""
    try:
        response = requests.post(
            f"{ollama_base_url}/api/generate",
            json={
                "model": model_name,
                "prompt": prompt,
                "context": context,
                "stream": False,  # 스트리밍 비활성화
                "options": {
                    "temperature": 0, # 일관된 출력을 위해 temperature 를 0 으로 설정
                }
            },
        )
        response.raise_for_status()  # 오류 발생 시 예외 발생

        # JSON 응답 파싱
        response_data = response.json()
        return response_data["response"], response_data.get("context", [])

    except requests.exceptions.RequestException as e:
        print(f"Ollama API 호출 중 오류 발생: {e}")
        return None, []

# 간단한 프롬프트로 테스트
prompt = "Tell me a short joke."
response, _ = generate_with_ollama(prompt)

if response:
    print(f"Ollama 응답: {response}")
else:
    print("Ollama API 호출 실패.")

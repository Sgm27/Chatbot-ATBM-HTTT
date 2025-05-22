from openai import OpenAI
import concurrent.futures
import time

client = OpenAI(api_key="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",
                base_url="https://integrate.api.nvidia.com/v1")

def make_request(request_id):
    start_time = time.time()
    print(f"Starting request {request_id}")
    
    response = client.chat.completions.create(
        model="meta/llama-3.3-70b-instruc",
        messages=[
            {"role": "system", "content": "Bạn là trợ lý thông minh, Chỉ trả lười bằng tiếng Việt"},
            {"role": "user", "content": f"Tiểu sử chủ tịch Hồ Chí Minh (Yêu cầu #{request_id})"}],
        stream=False  # Setting stream to False for concurrent requests
    )
    
    end_time = time.time()
    print(f"Request {request_id} completed in {end_time - start_time:.2f} seconds")
    return response.choices[0].message.content

# Number of concurrent requests
num_requests = 100

# Run requests concurrently
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(make_request, i) for i in range(num_requests)]
    
    # Process results as they complete
    for future in concurrent.futures.as_completed(futures):
        try:
            result = future.result()
            print(f"Response length: {len(result)} characters")
        except Exception as e:
            print(f"Request failed: {e}")

print(f"All {num_requests} requests completed.")

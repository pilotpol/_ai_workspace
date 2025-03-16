## สิ่งที่ต้องเตรียมก่อนเริ่ม Workshop
1. Project my-first-workshop ที่สร้างไว้แล้ว
2. File 1_start_basic_project.py ที่อยู่ใน Directory my-first-workshop/src
3. สร้างไฟล์ __init__.py ใน Directory my-first-workshop/src
<br/>

## จุดประสงค์ของ Lesson 2
1. เข้าใจการใช้งาน Lib OpenAI เบื้องต้น
2. เข้าใจความแตกต่างระหว่าง Chat Completions API vs Responses API ทั้งการใช้งาน (Request) และรูปแบบข้อมูลที่ได้ (Response) สามารถดูเพิ่มเติมได้ที่ 
[https://platform.openai.com/docs/guides/responses-vs-chat-completions?api-mode=responses#why-the-responses-api](https://platform.openai.com/docs/guides/responses-vs-chat-completions?api-mode=responses#why-the-responses-api)
<br/>

## คำสั่งที่ใช้
1. `uv pip install openai`
2. `uv pip install python-dotenv`
3. `uv run src/2_connect_open_ai.py`
<br/>

## ผลลัพธ์
1. Output ที่ได้จากการใช้ Completions API ซึ่งเป็นแบบเก่า
```yaml
{
  "ChatCompletion": {
    "id": "chatcmpl-BBniuLGXPgJxqT3Q9NZE7xOZp5cYZ",
    "choices": [
      {
        "finish_reason": "stop",
        "index": 0,
        "logprobs": null,
        "message": {
          "content": "I'm sorry, but I don't have any information about you. Could you please provide some details or context?",
          "refusal": null,
          "role": "assistant",
          "annotations": [],
          "audio": null,
          "function_call": null,
          "tool_calls": null
        }
      }
    ],
    "created": 1742152444,
    "model": "gpt-4o-2024-08-06",
    "object": "chat.completion",
    "service_tier": "default",
    "system_fingerprint": "fp_f9f4fb6dbf",
    "usage": {
      "completion_tokens": 22,
      "prompt_tokens": 13,
      "total_tokens": 35,
      "completion_tokens_details": {
        "accepted_prediction_tokens": 0,
        "audio_tokens": 0,
        "reasoning_tokens": 0,
        "rejected_prediction_tokens": 0
      },
      "prompt_tokens_details": {
        "audio_tokens": 0,
        "cached_tokens": 0
      }
    }
  }
}
```

2. Output ที่ได้จากการใช้ Responses API ซึ่งเป็นแบบใหม่
```yaml
{
  "id": "resp_67d722fd64f08190a103d3be91a0d3e30dc4fcd39fffcf23",
  "created_at": 1742152445.0,
  "error": null,
  "incomplete_details": null,
  "instructions": null,
  "metadata": {},
  "model": "gpt-4o-2024-08-06",
  "object": "response",
  "output": [
    {
      "id": "msg_67d722fdafb88190ab63189fdde20a480dc4fcd39fffcf23",
      "content": [
        {
          "annotations": [],
          "text": "Of course! Please provide some details about yourself so I can help craft a sentence for you.",
          "type": "output_text"
        }
      ],
      "role": "assistant",
      "status": "completed",
      "type": "message"
    }
  ],
  "parallel_tool_calls": true,
  "temperature": 1.0,
  "tool_choice": "auto",
  "tools": [],
  "top_p": 1.0,
  "max_output_tokens": null,
  "previous_response_id": null,
  "reasoning": {
    "effort": null,
    "generate_summary": null
  },
  "status": "completed",
  "text": {
    "format": {
      "type": "text"
    }
  },
  "truncation": "disabled",
  "usage": {
    "input_tokens": 31,
    "output_tokens": 20,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 51,
    "input_tokens_details": {
      "cached_tokens": 0
    }
  },
  "user": null,
  "store": true
}
```

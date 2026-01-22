"""
Gemini AI Integration for Enhanced Code Analysis
Uses Google Gemini API for sophisticated code understanding
"""

import json
import os
from typing import Dict, List, Optional

from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    MODEL = genai.GenerativeModel('gemini-2.5-flash')
else:
    MODEL = None


def is_gemini_available() -> bool:
    """Check if Gemini API is available and configured"""
    return GEMINI_API_KEY is not None and MODEL is not None


def analyze_complexity_with_gemini(code: str) -> Optional[Dict]:
    """
    Use Gemini to analyze code complexity with deep understanding

    Args:
        code: The code to analyze

    Returns:
        Dictionary with complexity analysis or None if unavailable
    """
    if not is_gemini_available():
        return None

    try:
        prompt = f"""Analyze the time and space complexity of this code. Provide a detailed, accurate analysis.

Code:
```python
{code}
```

Provide your analysis in the following JSON format:
{{
    "functions": [
        {{
            "name": "function_name",
            "time_complexity": "O(...)",
            "space_complexity": "O(...)",
            "confidence": "high|medium|low",
            "reasoning": [
                "Point 1 about why this complexity",
                "Point 2 about algorithm analysis",
                "Point 3 about optimization insights"
            ],
            "best_case": "O(...)",
            "average_case": "O(...)",
            "worst_case": "O(...)",
            "optimization_suggestions": [
                "Suggestion 1 if applicable",
                "Suggestion 2 if applicable"
            ]
        }}
    ]
}}

Be precise and thorough. Consider:
1. Loop depths and iterations
2. Recursive calls and their branching
3. Data structure operations
4. Hidden complexities in library functions
5. Best, average, and worst case scenarios"""

        response = MODEL.generate_content(prompt)
        response_text = response.text.strip()
        if '```json' in response_text:
            json_start = response_text.find('```json') + 7
            json_end = response_text.find('```', json_start)
            response_text = response_text[json_start:json_end].strip()
        elif '```' in response_text:
            json_start = response_text.find('```') + 3
            json_end = response_text.find('```', json_start)
            response_text = response_text[json_start:json_end].strip()
        return json.loads(response_text)
    except ValueError as ve:
        print(f"JSON parsing error: {ve}")
    except Exception as e:
        print(f"Gemini API error: {e}")
    return None


def detect_patterns_with_gemini(code: str) -> Optional[Dict]:
    """
    Use Gemini to detect DSA patterns with high accuracy

    Args:
        code: The code to analyze

    Returns:
        Dictionary with pattern detection results or None if unavailable
    """
    if not is_gemini_available():
        return None

    try:
        prompt = f"""Analyze this code and identify all Data Structures & Algorithms patterns being used.

Code:
```python
{code}
```

Provide your analysis in the following JSON format:
{{
    "patterns": [
        {{
            "pattern_name": "Pattern Name",
            "confidence": 0.95,
            "evidence": [
                "Evidence point 1",
                "Evidence point 2",
                "Evidence point 3"
            ],
            "description": "Brief description of how this pattern is implemented"
        }}
    ],
    "data_structures": [
        {{
            "structure": "Data Structure Name",
            "usage": "How it's being used",
            "efficiency": "Why this choice is good/bad"
        }}
    ],
    "algorithm_type": "Type of algorithm (e.g., Greedy, Dynamic Programming, Divide and Conquer)",
    "coding_techniques": [
        "Technique 1 (e.g., Two Pointers, Sliding Window)",
        "Technique 2"
    ]
}}

Common patterns to look for:
- Binary Search
- Two Pointers
- Sliding Window
- Fast & Slow Pointers
- Merge Intervals
- Cyclic Sort
- In-place Reversal of LinkedList
- Tree BFS/DFS
- Graph BFS/DFS
- Dynamic Programming
- Backtracking
- Greedy Algorithms
- Divide and Conquer
- Monotonic Stack/Queue
- Top K Elements
- K-way Merge
- Topological Sort"""

        response = MODEL.generate_content(prompt)
        response_text = response.text.strip()
        if '```json' in response_text:
            json_start = response_text.find('```json') + 7
            json_end = response_text.find('```', json_start)
            response_text = response_text[json_start:json_end].strip()
        elif '```' in response_text:
            json_start = response_text.find('```') + 3
            json_end = response_text.find('```', json_start)
            response_text = response_text[json_start:json_end].strip()
        return json.loads(response_text)
    except ValueError as ve:
        print(f"JSON parsing error: {ve}")
    except Exception as e:
        print(f"Gemini API error: {e}")
    return None


def get_optimization_suggestions(code: str) -> Optional[List[str]]:
    """
    Get optimization suggestions from Gemini

    Args:
        code: The code to analyze

    Returns:
        List of optimization suggestions or None if unavailable
    """
    if not is_gemini_available():
        return None

    try:
        prompt = f"""Analyze this code and provide specific optimization suggestions.

Code:
```python
{code}
```

Provide 3-5 concrete optimization suggestions focusing on:
1. Time complexity improvements
2. Space complexity improvements
3. Code readability and maintainability
4. Pythonic best practices
5. Edge case handling

Format as a JSON array:
[
    "Suggestion 1 with specific code change",
    "Suggestion 2 with reasoning",
    "Suggestion 3 with example"
]"""

        response = MODEL.generate_content(prompt)
        response_text = response.text.strip()
        if '```json' in response_text:
            json_start = response_text.find('```json') + 7
            json_end = response_text.find('```', json_start)
            response_text = response_text[json_start:json_end].strip()
        elif '```' in response_text:
            json_start = response_text.find('```') + 3
            json_end = response_text.find('```', json_start)
            response_text = response_text[json_start:json_end].strip()
        return json.loads(response_text)
    except ValueError as ve:
        print(f"JSON parsing error: {ve}")
    except Exception as e:
        print(f"Gemini API error: {e}")
    return None


def explain_algorithm(code: str) -> Optional[str]:
    """
    Get a natural language explanation of the algorithm

    Args:
        code: The code to explain

    Returns:
        Explanation string or None if unavailable
    """
    if not is_gemini_available():
        return None

    try:
        prompt = f"""Provide a clear, educational explanation of what this algorithm does and how it works.

Code:
```python
{code}
```

Explain in 2-3 paragraphs:
1. What the algorithm does (high-level purpose)
2. How it works (step-by-step logic)
3. Why it's implemented this way (design decisions)

Keep it clear and educational, as if teaching a student."""

        response = MODEL.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Gemini API error: {e}")
        return None

"""
Code-Sensei: DSA Logic and Time Complexity Analyzer
Powered by Gemini AI for Advanced Code Analysis
"""

import click
from pathlib import Path
from colorama import init, Fore, Style
from gemini_analyzer import (
    is_gemini_available,
    analyze_complexity_with_gemini,
    detect_patterns_with_gemini,
    get_optimization_suggestions,
    explain_algorithm
)

# Initialize colorama for cross-platform colored output
init()


def print_header():
    """Print the Code-Sensei header"""
    gemini_status = "✨ Powered by Gemini AI" if is_gemini_available() else "⚠️  Gemini API Required"
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{Fore.CYAN}🥋  CODE-SENSEI - DSA & Complexity Analyzer  🥋")
    print(f"{Fore.CYAN}{gemini_status:^60}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")


def print_gemini_complexity_results(results):
    """Print Gemini complexity analysis results"""
    if not results or 'functions' not in results:
        return
    
    print(f"{Fore.GREEN}🤖 GEMINI AI COMPLEXITY ANALYSIS{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{'─'*60}{Style.RESET_ALL}\n")
    
    for func in results['functions']:
        print(f"{Fore.CYAN}Function: {Style.BRIGHT}{func['name']}{Style.RESET_ALL}")
        print(f"  ⏱️  Time Complexity:  {Fore.YELLOW}{func['time_complexity']}{Style.RESET_ALL}")
        print(f"  💾 Space Complexity: {Fore.YELLOW}{func['space_complexity']}{Style.RESET_ALL}")
        print(f"  🎯 Confidence:       {Fore.YELLOW}{func['confidence'].upper()}{Style.RESET_ALL}")
        
        # Show case analysis if available
        if 'best_case' in func:
            print(f"\n  {Fore.MAGENTA}Case Analysis:{Style.RESET_ALL}")
            print(f"    • Best Case:    {func.get('best_case', 'N/A')}")
            print(f"    • Average Case: {func.get('average_case', 'N/A')}")
            print(f"    • Worst Case:   {func.get('worst_case', 'N/A')}")
        
        if 'reasoning' in func and func['reasoning']:
            print(f"\n  {Fore.MAGENTA}Reasoning:{Style.RESET_ALL}")
            for reason in func['reasoning']:
                print(f"    • {reason}")
        
        if 'optimization_suggestions' in func and func['optimization_suggestions']:
            print(f"\n  {Fore.GREEN}💡 Optimizations:{Style.RESET_ALL}")
            for suggestion in func['optimization_suggestions']:
                print(f"    • {suggestion}")
        print()


def print_gemini_pattern_results(results):
    """Print Gemini pattern detection results"""
    if not results or 'patterns' not in results:
        return
    
    print(f"{Fore.GREEN}🤖 GEMINI AI PATTERN DETECTION{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{'─'*60}{Style.RESET_ALL}\n")
    
    # Algorithm type
    if 'algorithm_type' in results:
        print(f"{Fore.CYAN}Algorithm Type: {Style.BRIGHT}{results['algorithm_type']}{Style.RESET_ALL}\n")
    
    # Patterns
    for pattern in results['patterns']:
        confidence_color = Fore.GREEN if pattern['confidence'] > 0.8 else Fore.YELLOW
        print(f"{Fore.CYAN}Pattern: {Style.BRIGHT}{pattern['pattern_name']}{Style.RESET_ALL}")
        print(f"  🎯 Confidence: {confidence_color}{pattern['confidence']*100:.0f}%{Style.RESET_ALL}")
        
        if 'description' in pattern:
            print(f"  📝 {pattern['description']}")
        
        if 'evidence' in pattern and pattern['evidence']:
            print(f"  {Fore.MAGENTA}Evidence:{Style.RESET_ALL}")
            for evidence in pattern['evidence']:
                print(f"    • {evidence}")
        print()
    
    # Data structures
    if 'data_structures' in results and results['data_structures']:
        print(f"{Fore.CYAN}Data Structures Used:{Style.RESET_ALL}")
        for ds in results['data_structures']:
            print(f"  • {Style.BRIGHT}{ds['structure']}{Style.RESET_ALL}: {ds['usage']}")
            if 'efficiency' in ds:
                print(f"    {Fore.YELLOW}→ {ds['efficiency']}{Style.RESET_ALL}")
        print()
    
    # Coding techniques
    if 'coding_techniques' in results and results['coding_techniques']:
        print(f"{Fore.CYAN}Coding Techniques:{Style.RESET_ALL}")
        for technique in results['coding_techniques']:
            print(f"  • {technique}")
        print()


def analyze_file(filepath: str, detailed: bool = False):
    """Analyze a code file using Gemini AI"""
    path = Path(filepath)
    
    if not path.exists():
        print(f"{Fore.RED}❌ Error: File '{filepath}' not found{Style.RESET_ALL}")
        return
    
    if path.suffix != '.py':
        print(f"{Fore.YELLOW}⚠️  Warning: This tool is optimized for Python files{Style.RESET_ALL}")
    
    print_header()
    
    # Check if Gemini is available
    if not is_gemini_available():
        print(f"{Fore.RED}❌ ERROR: Gemini API is not configured!{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Please set your GEMINI_API_KEY in the .env file{Style.RESET_ALL}\n")
        return
    
    print(f"{Fore.CYAN}Analyzing: {Style.BRIGHT}{filepath}{Style.RESET_ALL}\n")
    
    # Read the code
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()
    except Exception as e:
        print(f"{Fore.RED}❌ Error reading file: {e}{Style.RESET_ALL}")
        return
    
    print(f"{Fore.MAGENTA}✨ Analyzing with Gemini AI...{Style.RESET_ALL}\n")
    
    # Gemini complexity analysis
    gemini_complexity = analyze_complexity_with_gemini(code)
    if gemini_complexity:
        print_gemini_complexity_results(gemini_complexity)
    else:
        print(f"{Fore.YELLOW}⚠️  Could not analyze complexity{Style.RESET_ALL}\n")
    
    # Gemini pattern detection
    gemini_patterns = detect_patterns_with_gemini(code)
    if gemini_patterns:
        print_gemini_pattern_results(gemini_patterns)
    else:
        print(f"{Fore.YELLOW}⚠️  Could not detect patterns{Style.RESET_ALL}\n")
    
    # Algorithm explanation
    if detailed:
        explanation = explain_algorithm(code)
        if explanation:
            print(f"{Fore.GREEN}📖 ALGORITHM EXPLANATION{Style.RESET_ALL}")
            print(f"{Fore.GREEN}{'─'*60}{Style.RESET_ALL}\n")
            print(f"{Fore.WHITE}{explanation}{Style.RESET_ALL}\n")
    
    # Optimization suggestions
    optimizations = get_optimization_suggestions(code)
    if optimizations:
        print(f"{Fore.GREEN}💡 OPTIMIZATION SUGGESTIONS{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{'─'*60}{Style.RESET_ALL}\n")
        for i, suggestion in enumerate(optimizations, 1):
            print(f"{Fore.YELLOW}{i}. {suggestion}{Style.RESET_ALL}\n")
    
    # Summary
    print(f"{Fore.GREEN}{'─'*60}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}✅ Analysis Complete!{Style.RESET_ALL}\n")


@click.group()
def cli():
    """Code-Sensei: DSA Logic and Time Complexity Analyzer"""
    pass


@cli.command()
@click.argument('filepath', type=click.Path())
@click.option('--detailed', '-d', is_flag=True, help='Show detailed analysis')
def analyze(filepath, detailed):
    """Analyze a code file for DSA patterns and complexity"""
    analyze_file(filepath, detailed)


@cli.command()
def interactive():
    """Interactive mode - paste your code for analysis"""
    print_header()
    
    # Check if Gemini is available
    if not is_gemini_available():
        print(f"{Fore.RED}❌ ERROR: Gemini API is not configured!{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Please set your GEMINI_API_KEY in the .env file{Style.RESET_ALL}\n")
        return
    
    print(f"{Fore.CYAN}Interactive Mode{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Paste your Python code below.")
    print(f"Press Ctrl+Z (Windows) or Ctrl+D (Unix) and Enter when done:{Style.RESET_ALL}\n")
    
    # Read multi-line input
    lines = []
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        pass
    
    code = '\n'.join(lines)
    
    if not code.strip():
        print(f"{Fore.RED}❌ No code provided{Style.RESET_ALL}")
        return
    
    print(f"\n{Fore.MAGENTA}✨ Analyzing with Gemini AI...{Style.RESET_ALL}\n")
    
    # Gemini complexity analysis
    gemini_complexity = analyze_complexity_with_gemini(code)
    if gemini_complexity:
        print_gemini_complexity_results(gemini_complexity)
    
    # Gemini pattern detection
    gemini_patterns = detect_patterns_with_gemini(code)
    if gemini_patterns:
        print_gemini_pattern_results(gemini_patterns)
    
    # Optimization suggestions
    optimizations = get_optimization_suggestions(code)
    if optimizations:
        print(f"{Fore.GREEN}💡 OPTIMIZATION SUGGESTIONS{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{'─'*60}{Style.RESET_ALL}\n")
        for i, suggestion in enumerate(optimizations, 1):
            print(f"{Fore.YELLOW}{i}. {suggestion}{Style.RESET_ALL}\n")
    
    print(f"{Fore.GREEN}{'─'*60}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}✅ Analysis Complete!{Style.RESET_ALL}\n")


@cli.command()
def demo():
    """Run a demo with example code"""
    print_header()
    
    # Check if Gemini is available
    if not is_gemini_available():
        print(f"{Fore.RED}❌ ERROR: Gemini API is not configured!{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Please set your GEMINI_API_KEY in the .env file{Style.RESET_ALL}\n")
        return
    
    print(f"{Fore.CYAN}Running Demo Analysis with Gemini AI...{Style.RESET_ALL}\n")
    
    # Example code
    example_code = '''
def binary_search(arr, target):
    """Binary search implementation"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def bubble_sort(arr):
    """Bubble sort implementation"""
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr


def fibonacci(n):
    """Recursive fibonacci"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
'''
    
    print(f"{Fore.YELLOW}Example Code:{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{example_code}{Style.RESET_ALL}\n")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")
    
    # Gemini complexity analysis
    gemini_complexity = analyze_complexity_with_gemini(example_code)
    if gemini_complexity:
        print_gemini_complexity_results(gemini_complexity)
    
    # Gemini pattern detection
    gemini_patterns = detect_patterns_with_gemini(example_code)
    if gemini_patterns:
        print_gemini_pattern_results(gemini_patterns)
    
    # Optimization suggestions
    optimizations = get_optimization_suggestions(example_code)
    if optimizations:
        print(f"{Fore.GREEN}💡 OPTIMIZATION SUGGESTIONS{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{'─'*60}{Style.RESET_ALL}\n")
        for i, suggestion in enumerate(optimizations, 1):
            print(f"{Fore.YELLOW}{i}. {suggestion}{Style.RESET_ALL}\n")
    
    print(f"{Fore.GREEN}{'─'*60}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}✅ Demo Complete!{Style.RESET_ALL}\n")


if __name__ == '__main__':
    cli()

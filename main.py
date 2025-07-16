#!/usr/bin/env python3
"""
Test AI Module - Main Application
A simple Python application for testing AI functionalities.
"""

import datetime
import random


class AITestModule:
    """A simple class to demonstrate AI testing capabilities."""
    
    def __init__(self, name="AI Test"):
        self.name = name
        self.created_at = datetime.datetime.now()
        print(f"Initialized {self.name} at {self.created_at}")
    
    def greet(self, user_name="User"):
        """Greet the user with a friendly message."""
        greetings = [
            f"Hello {user_name}! Welcome to {self.name}!",
            f"Hi there {user_name}! Great to see you!",
            f"Greetings {user_name}! Ready to test some AI?",
            f"Welcome {user_name}! Let's explore AI together!"
        ]
        return random.choice(greetings)
    
    def generate_random_data(self, count=5):
        """Generate some random test data."""
        data = []
        for i in range(count):
            item = {
                'id': i + 1,
                'value': random.randint(1, 100),
                'timestamp': datetime.datetime.now().isoformat(),
                'status': random.choice(['active', 'inactive', 'pending'])
            }
            data.append(item)
        return data
    
    def analyze_data(self, data):
        """Simple data analysis function."""
        if not data:
            return {"error": "No data provided"}
        
        values = [item['value'] for item in data]
        analysis = {
            'count': len(data),
            'sum': sum(values),
            'average': sum(values) / len(values),
            'min': min(values),
            'max': max(values),
            'range': max(values) - min(values)
        }
        return analysis


def main():
    """Main function to run the AI test module."""
    print("=" * 50)
    print("AI Test Module - Demo Application")
    print("=" * 50)
    
    # Initialize the AI test module
    ai_module = AITestModule("Advanced AI Test System")
    
    # Greet user
    print(ai_module.greet("Developer"))
    print()
    
    # Generate and analyze test data
    print("Generating random test data...")
    test_data = ai_module.generate_random_data(10)
    
    print(f"Generated {len(test_data)} data points:")
    for item in test_data[:3]:  # Show first 3 items
        print(f"  ID: {item['id']}, Value: {item['value']}, Status: {item['status']}")
    print("  ... and more")
    print()
    
    # Analyze the data
    print("Analyzing data...")
    analysis = ai_module.analyze_data(test_data)
    
    print("Analysis Results:")
    for key, value in analysis.items():
        if isinstance(value, float):
            print(f"  {key.capitalize()}: {value:.2f}")
        else:
            print(f"  {key.capitalize()}: {value}")
    
    print()
    print("Demo completed successfully!")
    print("=" * 50)


if __name__ == "__main__":
    main()
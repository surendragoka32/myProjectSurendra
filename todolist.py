#!/usr/bin/env python3
"""
Simple Todo List Application
A command-line todo list manager with add, remove, view, and mark complete features.
"""

import json
import os
from datetime import datetime
# Note: For simplicity, this app uses a JSON file to store todos. In a real application, you might want to use a database or more robust storage solution.
class TodoList:
    def __init__(self, filename='todos.json'):
        self.filename = filename
        self.todos = self.load_todos()
    
    def load_todos(self):
        """Load todos from file if it exists."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []
    
    def save_todos(self):
        """Save todos to file."""
        with open(self.filename, 'w') as f:
            json.dump(self.todos, f, indent=2)
    
    def add_todo(self, task):
        """Add a new todo item."""
        todo = {
            'id': len(self.todos) + 1,
            'task': task,
            'completed': False,
            'created_at': datetime.now().isoformat()
        }
        self.todos.append(todo)
        self.save_todos()
        print(f"✓ Added: {task}")
    
    def remove_todo(self, todo_id):
        """Remove a todo by ID."""
        self.todos = [t for t in self.todos if t['id'] != todo_id]
        self.save_todos()
        print(f"✓ Removed todo {todo_id}")
    
    def mark_complete(self, todo_id):
        """Mark a todo as completed."""
        for todo in self.todos:
            if todo['id'] == todo_id:
                todo['completed'] = True
                self.save_todos()
                print(f"✓ Marked '{todo['task']}' as completed")
                return
        print(f"✗ Todo {todo_id} not found")
    
    def view_todos(self):
        """Display all todos."""
        if not self.todos:
            print("No todos yet!")
            return
        
        print("\n--- Todo List ---")
        for todo in self.todos:
            status = "✓" if todo['completed'] else "○"
            print(f"{status} [{todo['id']}] {todo['task']}")
        print()
    
    def get_stats(self):
        """Get todo statistics."""
        total = len(self.todos)
        completed = sum(1 for t in self.todos if t['completed'])
        pending = total - completed
        return {'total': total, 'completed': completed, 'pending': pending}


def main():
    """Main function to run the todo list app."""
    todo_list = TodoList()
    
    while True:
        print("\n--- Todo List Menu ---")
        print("1. Add todo")
        print("2. View todos")
        print("3. Mark complete")
        print("4. Remove todo")
        print("5. View stats")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            task = input("Enter task: ").strip()
            if task:
                todo_list.add_todo(task)
        
        elif choice == '2':
            todo_list.view_todos()
        
        elif choice == '3':
            try:
                todo_id = int(input("Enter todo ID to mark complete: "))
                todo_list.mark_complete(todo_id)
            except ValueError:
                print("Invalid ID")
        
        elif choice == '4':
            try:
                todo_id = int(input("Enter todo ID to remove: "))
                todo_list.remove_todo(todo_id)
            except ValueError:
                print("Invalid ID")
        
        elif choice == '5':
            stats = todo_list.get_stats()
            print(f"\nTotal: {stats['total']}, Completed: {stats['completed']}, Pending: {stats['pending']}")
        
        elif choice == '6':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

# 3.12 Combined DS Program
todo_list = []

def add_task(task_name, tags_set):
    task = {
        "task": task_name,
        "tags": set(tags_set)
    }
    todo_list.append(task)

def display_all():
    print("\n--- All To-Do Tasks ---")
    for idx, item in enumerate(todo_list, start=1):
        tags_str = ", ".join(item['tags'])
        print(f"{idx}. Task: {item['task']:<25} | Tags: [{tags_str}]")

def find_by_tag(search_tag):
    print(f"\n--- Tasks tagged with '{search_tag}' ---")
    matched = [t['task'] for t in todo_list if search_tag in t['tags']]
    if matched:
        for t in matched:
            print(f"  - {t}")
    else:
        print("  No tasks found for this tag.")


# Demonstration
add_task("Submit Assignment", {"college", "urgent"})
add_task("Buy Groceries", {"personal", "shopping"})
add_task("Prepare Presentation", {"college", "work"})

display_all()
find_by_tag("college")
find_by_tag("shopping")
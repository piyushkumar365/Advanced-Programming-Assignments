from typing import List, Dict, Set
from functools import reduce
import time


def total_time_per_user(logs: List[Dict]) -> Dict[str, float]:

    users = {log["user"] for log in logs}

    return {
        u: sum(log["duration"] for log in logs if log["user"] == u)
        for u in users
    }


def most_active_users(logs: List[Dict], k: int) -> List[str]:

    totals = total_time_per_user(logs)

    return sorted(totals, key=lambda x: totals[x], reverse=True)[:k]


def unique_actions(logs: List[Dict]) -> Set[str]:

    return {log["action"] for log in logs}


logs = [
{"user": "CSB24051", "action": "YouTube", "duration": 1.5},
{"user": "CSB24052", "action": "Instagram", "duration": 2.0},
{"user": "CSB24053", "action": "Google", "duration": 0.5},
{"user": "CSB24054", "action": "YouTube", "duration": 3.0},
{"user": "CSB24055", "action": "WhatsApp", "duration": 1.0}
]

k = 2

start = time.perf_counter()

totals = total_time_per_user(logs)
top_users = most_active_users(logs, k)
actions = unique_actions(logs)

total_activity_time = reduce(lambda x, log: x + log["duration"], logs, 0)

end = time.perf_counter()


print("Input Size (n):", len(logs))

print("\nTotal Time Per User:")
print(totals)

print("\nTop", k, "Most Active Users:")
print(top_users)

print("\nUnique Actions:")
print(actions)

print("\nTotal Activity Time:", total_activity_time)

print("\nExecution Time:", end - start, "seconds")

print("\nTime Complexity for Top K Users: O(n + m log m)")
print("Space Complexity for Intermediate Results: O(m + a)")
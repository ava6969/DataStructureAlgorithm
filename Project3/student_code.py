import math
import heapq
from collections import defaultdict


def eucli(dist, goal):
    return math.sqrt(math.pow(dist[0]-goal[0], 2) + math.pow(dist[1]-goal[1], 2) )

def reconstruct_path(cameFrom, current):
    total_path = [current]
    while current in cameFrom.keys():
        current = cameFrom[current]
        total_path.append(current)
    return total_path.reverse()

# A* finds a path from start to goal.
# h is the heuristic function. h(n) estimates the cost to reach goal from node n.
def shortest_path(M, start, goal):
    # The set of discovered nodes that may need to be (re-)expanded.
    # Initially, only the start node is known.
    # This is usually implemented as a min-heap or priority queue rather than a hash-set.
    openSet = []
    heapq.heappush(openSet, (0, start))

    # For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from start
    # to n currently known.
    cameFrom = {}

    # For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
    gScore = defaultdict(float('inf'))
    gScore[start] = 0

    # For node n, fScore[n] := gScore[n] + h(n). fScore[n] represents our current best guess as to
    # how short a path from start to finish can be if it goes through n.
    fScore = defaultdict(float('inf'))
    fScore[start] = gScore[start] + eucli(M.intersections[start], M.intersections[goal])

    while len(openSet) > 0:
        # This operation can occur in O(1) time if openSet is a min-heap or a priority queue
        # current := the node in openSet having the lowest fScore[] value
        current = heapq.heappop(openSet)

        if current == goal:
            return reconstruct_path(cameFrom, current)

        # openSet.Remove(current)
        for neighbor in M.roads[current]:
            # d(current,neighbor) is the weight of the edge from current to neighbor
            # tentative_gScore is the distance from start to the neighbor through current
            tentative_gScore = gScore[current] + eucli(M.intersections[current], M.intersections[neighbor])
            if tentative_gScore < gScore[neighbor]:
                # This path to neighbor is better than any previous one. Record it!
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = gScore[neighbor] + eucli(M.intersections[neighbor], M.intersections[goal])
                if neighbor not in openSet:
                    heapq.heappush(openSet, (fScore[neighbor], neighbor))

    # Open set is empty but goal was never reached
    return []
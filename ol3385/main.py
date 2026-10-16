"""BusStop I"""

def main():
    """BusStop I"""
    p = int(input())
    n = int(input())

    stops = {}
    for _ in range(n):
        parts = list(map(int, input().split()))
        stop_id = parts[0]
        destinations = parts[1:]
        stops[stop_id] = destinations

    bus = []
    delivered = 0

    for curr_stop in range(1, n + 1):
        remaining_bus = []
        for dest in bus:
            if dest == curr_stop:
                delivered += 1
            else:
                remaining_bus.append(dest)
        bus = remaining_bus

        if curr_stop in stops:
            for dest in stops[curr_stop]:
                if len(bus) >= p:
                    break
                if dest > curr_stop:
                    bus.append(dest)

    print(delivered)


if __name__ == "__main__":
    main()

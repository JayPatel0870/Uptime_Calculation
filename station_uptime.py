from collections import defaultdict

def parse_input(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        stations_section = []
        availability_section = []
        current_section = None

        for line in lines:
            line = line.strip()
            if line == "[Stations]":
                current_section = "stations"
            elif line == "[Charger Availability Reports]":
                current_section = "availability"
            elif current_section == "stations":
                if line:
                    stations_section.append(line)
            elif current_section == "availability":
                availability_section.append(line)

        if not stations_section or not availability_section:
            raise ValueError("Invalid input format: Missing sections")

        station_map = {}
        for entry in stations_section:
            parts = entry.split()
            if len(parts) < 2:
                raise ValueError(f"Invalid station entry: {entry}")
            station_id = int(parts[0])
            charger_ids = list(map(int, parts[1:]))
            station_map[station_id] = charger_ids

        charger_reports = defaultdict(list)
        for entry in availability_section:
            parts = entry.split()
            if len(parts) != 4:
                raise ValueError(f"Invalid availability entry: {entry}")
            charger_id = int(parts[0])
            start_time = int(parts[1])
            end_time = int(parts[2])
            is_up = parts[3].lower() == "true"
            charger_reports[charger_id].append((start_time, end_time, is_up))

        return station_map, charger_reports

    except Exception as e:
        print("ERROR:", e)
        raise

def calculate_uptime(station_map, charger_reports):
    station_uptime = {}

    for station_id, chargers in station_map.items():
        total_time = 0
        up_time = 0

        intervals = []
        for charger_id in chargers:
            if charger_id not in charger_reports:
                continue

            for start, end, is_up in charger_reports[charger_id]:
                intervals.append((start, end, is_up))

        intervals.sort()

        merged_intervals = []
        for start, end, is_up in intervals:
            if not merged_intervals:
                merged_intervals.append([start, end, is_up])
            else:
                if start <= merged_intervals[-1][1]:
                    if is_up == merged_intervals[-1][2]:
                        merged_intervals[-1][1] = max(merged_intervals[-1][1], end)
                    else:
                        merged_intervals.append([start, end, is_up])
                else:
                    merged_intervals.append([start, end, is_up])

        if merged_intervals:
            total_time = max(merged_intervals, key=lambda x: x[1])[1] - min(merged_intervals, key=lambda x: x[0])[0]

        for start, end, is_up in merged_intervals:
            duration = end - start
            if is_up:
                up_time += duration

        if total_time == 0:
            uptime_percentage = 0
        else:
            uptime_percentage = (up_time * 100) // total_time

        station_uptime[station_id] = uptime_percentage

    return station_uptime

def main():
    file_path = "input_1.txt"
    # file_path = "input_2.txt"

    station_map, charger_reports = parse_input(file_path)
    station_uptime = calculate_uptime(station_map, charger_reports)

    for station_id in sorted(station_uptime):
        print(f"{station_id} {station_uptime[station_id]}")

if __name__ == "__main__":
    main()

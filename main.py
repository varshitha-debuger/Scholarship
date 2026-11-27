
        if result["violations"]:
            summary["violations"] += 1

    for floor, summary in floors.items():
        if summary["electricity_limit_total"] > 0:
            summary["electricity_utilization"] = (
                summary["electricity"] / summary["electricity_limit_total"] * 100
            )
        else:
            summary["electricity_utilization"] = 0

        if summary["water_limit_total"] > 0:
            summary["water_utilization"] = (
                summary["water"] / summary["water_limit_total"] * 100
            )
        else:
            summary["water_utilization"] = 0

    return floors


def display_report(room_results, floor_summary):
    """Print room details, violations, and floor-wise comparison."""
    print("\nSMART HOSTEL RESOURCE MONITORING")
    print("=" * 72)
    print("Rates: electricity = {:.2f} per kWh; water = {:.2f} per kL".format(
        ELECTRICITY_RATE, WATER_RATE
    ))
    print("Limits per room: electricity = {:.1f} kWh; water = {:.1f} kL".format(
        ELECTRICITY_LIMIT, WATER_LIMIT
    ))

    print("\nROOM-WISE REPORT")
    print("-" * 72)

    for item in room_results:
        status = ", ".join(item["violations"]) if item["violations"] else "None"
        print(
            "Room {} (Floor {}) | Electricity: {:.1f} kWh | Water: {:.1f} kL".format(
                item["room"], item["floor"], item["electricity"], item["water"]
            )
        )
        print(
            "  Charges: Electricity = {:.2f}, Water = {:.2f}, Total = {:.2f}".format(
                item["electricity_charge"],
                item["water_charge"],
                item["total_charge"]
            )
        )
        print(
            "  Threshold use: Electricity = {:.1f}%, Water = {:.1f}%".format(
                item["electricity_utilization"], item["water_utilization"]
            )
        )
        print("  Threshold violations: {}".format(status))

    print("\nFLOOR-WISE RESOURCE COMPARISON")
    print("-" * 72)

    highest_electricity_floor = None
    highest_water_floor = None
    highest_electricity = -1
    highest_water = -1

    for floor in sorted(floor_summary):
        item = floor_summary[floor]
        print("Floor {} ({} rooms)".format(floor, item["rooms"]))
        print(
            "  Electricity: {:.1f} kWh ({:.1f}% of combined room limits)".format(
                item["electricity"], item["electricity_utilization"]
            )
        )
        print(
            "  Water: {:.1f} kL ({:.1f}% of combined room limits)".format(
                item["water"], item["water_utilization"]
            )
        )
        print("  Total charges: {:.2f}".format(item["total_charge"]))
        print("  Rooms with at least one violation: {}".format(item["violations"]))

        if item["electricity"] > highest_electricity:
            highest_electricity = item["electricity"]
            highest_electricity_floor = floor

        if item["water"] > highest_water:
            highest_water = item["water"]
            highest_water_floor = floor

    print("\nHIGHLIGHTS")
    print("Highest electricity consumption: Floor {}".format(highest_electricity_floor))
    print("Highest water consumption: Floor {}".format(highest_water_floor))


def main():
    errors = validate_data(rooms)

    if errors:
        print("DATA VALIDATION FAILED:")
        for error in errors:
            print("- " + error)
        return

    room_results = analyse_rooms(rooms)
    floor_summary = compare_floors(room_results)
    display_report(room_results, floor_summary)


if __name__ == "__main__":
    main()


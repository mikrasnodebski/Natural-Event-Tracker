import natural_event_tracker.tracker


def main():
    world_natural_events = natural_event_tracker.tracker.Map()
    world_natural_events.create_full_map_and_save()
    world_natural_events.show_map()


if __name__ == "__main__":
    main()

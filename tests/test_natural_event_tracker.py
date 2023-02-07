import src.natural_event_tracker.tracker as tracker
from os.path import exists


def test_check_default_name_map():
    world_natural_events = tracker.Map()
    assert world_natural_events.name == "map"


def test_check_new_name_map():
    world_natural_events = tracker.Map(123)
    assert world_natural_events.name == "123"


def test_save_file():
    world_natural_events = tracker.Map()
    world_natural_events.create_full_map_and_save()
    assert exists(world_natural_events.name + ".html")


def test_category_propriety():
    all_possible_categories = tracker.get_all_possible_event_categories()
    all_event_categories = [event.category_id() for event in tracker.
                            get_events()]
    result = True
    for element in all_event_categories:
        if element not in all_possible_categories:
            result = False
    assert result

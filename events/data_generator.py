from eventanalytics.models import *


def get_events_list():
    event1 = Event('2017-10-01T12:00:00.001Z', 'Downloading the module database causes module 11 restart', 0)
    event2 = Event('2017-10-01T12:00:01.001Z', 'The direction for forwarding the time of day is '
                                               'recognized automatically by the module', 0)
    event3 = Event('2017-10-01T12:00:02.001Z', 'Status@Flame On', 0)
    event4 = Event('2017-10-01T12:00:00.001Z', 'Downloading the module database causes module 11 restart', 0)
    event5 = Event('2017-10-01T12:00:01.001Z', 'The direction for forwarding the time of day is '
                                               'recognized automatically by the module', 0)
    event6 = Event('2017-10-01T12:00:02.001Z', 'Status@Flame On', 0)
    events_list = [event1, event2, event3, event4, event5, event6]
    return events_list


def get_patterns_list():
    pattern_def = PatternDefinition()
    matching_pattern1 = MatchingPattern('INTRODUCING FUEL', 1, 2)
    pattern_list = [matching_pattern1]
    matching_pattern2 = MatchingPattern('Status@Flame On', 0, 1)
    pattern_def.pattern = pattern_list
    pattern_list.append(matching_pattern2)
    matching_pattern3 = MatchingPattern('Module STOP due to parameter assignment', 1, 1)
    pattern_list.append(matching_pattern3)
    pattern_def.pattern = pattern_list

    pattern_def1 = PatternDefinition()
    matching_pattern4 = MatchingPattern('Downloading the module database causes module .. restart', 1, 1)
    pattern_list1 = [matching_pattern4]
    matching_pattern5 = MatchingPattern(
        'The SIMATIC mode was selected for time-of-day synchronization of the module with Id: ..', 1, 1)
    pattern_list1.append(matching_pattern5)
    pattern_def.pattern = pattern_list
    pattern_def1.pattern = pattern_list1
    pattern_def_list = [pattern_def, pattern_def1]
    return pattern_def_list


def get_events_input():
    event1 = Event('2017-10-01T12:00:00.001Z', 'Downloading the module database causes module 11 restart', 0)
    event2 = Event('2017-10-01T12:00:01.001Z',
                   'The direction for forwarding the time of day is recognized automatically by the module', 0)
    event3 = Event('2017-10-01T12:00:02.001Z', 'Status@Flame On', 0)
    event4 = Event('2017-10-01T12:00:03.001Z',
                   'The SIMATIC mode was selected for time-of-day synchronization of the module with Id: 33', 0)
    event5 = Event('2017-10-01T12:00:06.001Z',
                   'INTRODUCING FUEL', 0)
    event6 = Event('2017-10-01T12:00:09.001Z', 'Module STOP due to parameter assignment', 0)
    events_input = [event1, event2, event3, event4, event5, event6]
    return events_input


def get_top_events_data():
    metadata = EventsInputModelEventsMetadata('text')
    events_list = get_events_list()
    data = TopEventsInputDataModel(metadata, events_list, 12)
    return data


def get_filter_events_data():
    metadata = EventsInputModelEventsMetadata('text')
    events_list = get_events_list()
    filter_list = ['Introduction fuel']
    data = EventSearchInputDataModel(metadata, events_list, filter_list)
    return data


def get_count_events_data():
    metadata = EventInputEventsMetadata('text', 5000)
    events_list = get_events_list()
    data = EventInput(metadata, events_list)
    return data


def remove_duplicates_data():
    metadata = EventInputEventsMetadata('text', 5000)
    events_list = get_events_list()
    data = EventInput(metadata, events_list)
    return data


def get_pattern_mattching_data():
    patterns_list = get_patterns_list()
    metadata = EventsInputModelEventsMetadata('text')
    non_events = ['Error 2.. occurred', 'STOPPING ENGINE']
    events_list = get_events_input()
    events_input = EventInput(metadata, events_list)
    data = PatternMatchingInputDataModel(20000, patterns_list, non_events, events_input)
    return data

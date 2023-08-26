import unittest
from next_command import search_next_event
import datetime

class TestNextCommand(unittest.TestCase):

    def setUp(self) -> None:
        self.osu_filename = 'osu_events.json'
        return super().setUp()

    def test_search_next_event_with_existing_date_left(self):
        """Test with a date that exists at the front"""
        target_date = datetime.datetime(2023, 9, 4)
        event = search_next_event(target_date, self.osu_filename)
        self.assertTrue(event is not None)
        self.assertEqual(event.get_description(), 'Autumn Break Begins 10/12~13 - offices open')

    def test_search_next_event_with_existing_date_center(self):
        """Test with a date that exists in the middle"""
        target_date = datetime.datetime(2023, 11, 24)
        event = search_next_event(target_date, self.osu_filename)
        self.assertTrue(event is not None)
        self.assertEqual(event.get_description(), 'Last Day of Classes')

    def test_search_next_event_with_existing_date_right(self):
        """Test with a date that exists at the very end"""
        target_date = datetime.datetime(2024, 4, 22)
        event = search_next_event(target_date, self.osu_filename)
        self.assertTrue(event is not None)
        self.assertTrue(event.get_description().startswith('No future'))

    def test_search_next_event_with_nonexisting_date_0(self):
        """Random date"""
        target_date = datetime.datetime(2023, 10, 15)
        event = search_next_event(target_date, self.osu_filename)
        self.assertTrue(event is not None)
        self.assertEqual(event.get_description(), 'Veterans Day - offices closed')

    def test_search_next_event_with_nonexisting_date_1(self):
        """Day before the first event"""
        target_date = datetime.datetime(2023, 8, 24)
        event = search_next_event(target_date, self.osu_filename)
        self.assertTrue(event is not None)
        self.assertEqual(event.get_description(), 'Labor Day - offices closed')

    def test_search_next_event_with_nonexisting_date_2(self):
        """Day before the last event"""
        target_date = datetime.datetime(2024, 4, 20)
        event = search_next_event(target_date, self.osu_filename)
        self.assertTrue(event is not None)
        self.assertEqual(event.get_description(), 'Last Day of Classes')

    def test_search_next_event_with_nonexisting_date_3(self):
        """Day past the last event"""
        target_date = datetime.datetime(2024, 4, 23)
        event = search_next_event(target_date, self.osu_filename)
        self.assertTrue(event is not None)
        self.assertTrue(event.get_description().startswith('No future'))


if __name__ == '__main__':
    unittest.main()
from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse
from sport.models import Athlete, Event


class IndexPageTestCase(TestCase):

    def setUp(self):
        super().setUp()

        self.athlete1 = Athlete()
        self.athlete1.name = 'Athlete #1'
        self.athlete1.save()

        self.athlete2 = Athlete()
        self.athlete2.name = 'Athlete #2'
        self.athlete2.save()

        self.athlete3 = Athlete()
        self.athlete3.name = 'Athlete #3'
        self.athlete3.save()

        self.event1 = Event()
        self.event1.name = 'Event #1'
        self.event1.save()

        self.event2 = Event()
        self.event2.name = 'Event #2'
        self.event2.save()

    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_index_page_has_events(self):
        response = self.client.get(reverse('index'))
        self.assertContains(response, self.event1.name)
        self.assertContains(response, self.event2.name)

    def test_index_page_event_has_athlets(self):
        self.event1.participants.add(self.athlete1)
        self.event1.participants.add(self.athlete2)
        response = self.client.get(reverse('index'))
        self.assertContains(response, self.athlete1.name)
        self.assertContains(response, self.athlete2.name)
        self.assertNotContains(response, self.athlete3.name)

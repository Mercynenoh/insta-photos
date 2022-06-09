from django.test import TestCase


class ProfileTest(TestCase):

    def create_profile(self, pic="https://mdbcdn.b-cdn.net/img/new/fluid/nature/011.webp",bio="this is my bio"):
        return Profile.objects.create(pic=pic, bio=bio)

    def test_profile_creation(self):
        w = self.create_profile()
        self.assertTrue(isinstance(w, Profile))
        self.assertEqual(w.__unicode__(), w.title)

class PostTest(TestCase):

    def create_post(self, image="https://mdbcdn.b-cdn.net/img/new/fluid/nature/011.webp",imagename="beach"),caption="i love this", comments="good" , created_at=timezone.now() :
        return Profile.objects.create(pic=pic, bio=bio, imagename=imagename, comments=comments, caption=caption created_at=timezone.now())

    def test_post_creation(self):
        w = self.create_post()
        self.assertTrue(isinstance(w, Post))
        self.assertEqual(w.__unicode__(), w.title)

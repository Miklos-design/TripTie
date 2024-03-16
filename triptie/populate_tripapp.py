import os
import django
import datetime
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "triptie.settings")

django.setup()

from django.contrib.auth.models import User
from tripapp.models import UserProfile, TripPlan, LikePost, Comment


def populate():
    # Users
    user_data = [
        {"username": "alice", "password": "alice12345", "email": "alice@example.com"},
        {"username": "bob", "password": "bob12345", "email": "bob@example.com"},
        {"username": "charlie", "password": "charlie12345", "email": "charlie@example.com"},
        {"username": "dave", "password": "dave12345", "email": "dave@example.com"},
        {"username": "eve", "password": "eve12345", "email": "eve@example.com"},
    ]

    users = {}
    for user_info in user_data:
        user = add_user(user_info["username"], user_info["email"], user_info["password"])
        users[user_info["username"]] = user

    # UserProfiles
    user_profiles = [
        {"user": users["alice"], "gender": "F", "age": 28, "bio": "Love traveling.",
         "image_name": "1.jpg"},
        {"user": users["bob"], "gender": "M", "age": 30, "bio": "Enjoy outdoor activities.",
         "image_name": "2.jpg"},
        {"user": users["charlie"], "gender": "M", "age": 25, "bio": "Passionate about photography.",
         "image_name": "3.jpg"},
        {"user": users["dave"], "gender": "M", "age": 35, "bio": "Adventurous spirit.",
         "image_name": "4.jpg"},
        {"user": users["eve"], "gender": "F", "age": 27, "bio": "Foodie and culture enthusiast.",
         "image_name": "5.jpg"},
    ]

    for profile_info in user_profiles:
        add_user_profile(profile_info)

    user_alice = User.objects.get(username="alice")
    user_bob = User.objects.get(username="bob")
    user_charlie = User.objects.get(username="charlie")
    user_dave = User.objects.get(username="dave")
    user_eve = User.objects.get(username="eve")

    trip_plans = [
        {"user": user_alice, "title": "Exploring the Amazon Rainforest",
         "description": "Embark on an epic adventure deep into the heart of the Amazon Rainforest. Experience the lush greenery, exotic wildlife, and vibrant culture of this natural wonderland.",
         "destination_city": "Amazon Rainforest", "start_date": datetime.date(2024, 8, 10),
         "end_date": datetime.date(2024, 8, 20), "is_private": False, "image_name": "1.jpg"},

        {"user": user_bob, "title": "Safari in Serengeti National Park",
         "description": "Set off on a thrilling safari expedition through the vast plains of Serengeti National Park. Witness the majestic wildlife, including lions, elephants, and giraffes, in their natural habitat.",
         "destination_city": "Serengeti National Park", "start_date": datetime.date(2024, 9, 5),
         "end_date": datetime.date(2024, 9, 15), "is_private": False, "image_name": "2.jpg"},

        {"user": user_charlie, "title": "Road Trip along the Pacific Coast Highway",
         "description": "Hit the open road and embark on an unforgettable journey along the stunning Pacific Coast Highway. Marvel at breathtaking ocean views, charming coastal towns, and iconic landmarks.",
         "destination_city": "Pacific Coast Highway", "start_date": datetime.date(2024, 10, 1),
         "end_date": datetime.date(2024, 10, 10), "is_private": False, "image_name": "3.jpg"},

        {"user": user_dave, "title": "Trekking in the Himalayas",
         "description": "Challenge yourself with an exhilarating trek through the towering peaks and rugged terrain of the Himalayas. Experience breathtaking landscapes, serene mountain villages, and the warm hospitality of the locals.",
         "destination_city": "Himalayas", "start_date": datetime.date(2024, 11, 5),
         "end_date": datetime.date(2024, 11, 15), "is_private": False, "image_name": "4.jpg"},

        {"user": user_eve, "title": "Cultural Immersion in Kyoto",
         "description": "Immerse yourself in the rich history and traditions of Kyoto, Japan. Explore ancient temples, stroll through picturesque gardens, and savor the flavors of authentic Japanese cuisine.",
         "destination_city": "Kyoto", "start_date": datetime.date(2024, 12, 1), "end_date": datetime.date(2024, 12, 10),
         "is_private": False, "image_name": "5.jpg"},

        {"user": user_alice, "title": "Island Hopping in Greece",
         "description": "Escape to the sun-drenched islands of Greece and embark on an unforgettable island-hopping adventure. Discover pristine beaches, charming villages, and ancient ruins steeped in history.",
         "destination_city": "Greece", "start_date": datetime.date(2024, 9, 1), "end_date": datetime.date(2024, 9, 10),
         "is_private": False, "image_name": "6.jpg"},

        {"user": user_bob, "title": "Exploring the Grand Canyon",
         "description": "Witness the awe-inspiring beauty of the Grand Canyon as you embark on a journey through one of the world's most iconic natural wonders. Experience breathtaking vistas, rugged terrain, and stunning sunsets.",
         "destination_city": "Grand Canyon", "start_date": datetime.date(2024, 10, 15),
         "end_date": datetime.date(2024, 10, 25), "is_private": False, "image_name": "7.jpg"},

        {"user": user_charlie, "title": "Camping under the Northern Lights",
         "description": "Experience the magic of the Northern Lights as you camp beneath the starry Arctic skies. Marvel at the dancing colors of the Aurora Borealis and immerse yourself in the serene beauty of the Arctic wilderness.",
         "destination_city": "Arctic Circle", "start_date": datetime.date(2024, 11, 1),
         "end_date": datetime.date(2024, 11, 10), "is_private": False, "image_name": "8.jpg"},

        {"user": user_dave, "title": "Exploring the Great Barrier Reef",
         "description": "Dive into the crystal-clear waters of the Great Barrier Reef and discover a world of vibrant coral reefs, exotic marine life, and stunning underwater landscapes. Experience the wonders of one of the world's most diverse ecosystems.",
         "destination_city": "Great Barrier Reef", "start_date": datetime.date(2024, 12, 15),
         "end_date": datetime.date(2024, 12, 25), "is_private": False, "image_name": "9.jpg"},

        {"user": user_eve, "title": "Wine Tasting in Tuscany",
         "description": "Indulge your senses with a wine tasting tour through the picturesque vineyards of Tuscany. Savor the flavors of world-renowned wines, enjoy gourmet cuisine, and soak up the breathtaking views of the Italian countryside.",
         "destination_city": "Tuscany", "start_date": datetime.date(2025, 1, 1), "end_date": datetime.date(2025, 1, 10),
         "is_private": False, "image_name": "10.jpg"},

        {"user": user_alice, "title": "Adventure in the Australian Outback",
         "description": "Embark on an adrenaline-fueled adventure through the rugged landscapes of the Australian Outback. Explore vast desert plains, encounter unique wildlife, and discover ancient Aboriginal culture.",
         "destination_city": "Australian Outback", "start_date": datetime.date(2025, 2, 5),
         "end_date": datetime.date(2025, 2, 15), "is_private": False, "image_name": "11.jpg"},

        {"user": user_bob, "title": "Exploring the Inca Trail",
         "description": "Follow in the footsteps of ancient civilizations as you trek along the legendary Inca Trail to Machu Picchu. Marvel at breathtaking mountain scenery, explore ancient ruins, and immerse yourself in the rich history of the Inca Empire.",
         "destination_city": "Machu Picchu", "start_date": datetime.date(2025, 3, 1),
         "end_date": datetime.date(2025, 3, 10), "is_private": False, "image_name": "12.jpg"},

        {"user": user_charlie, "title": "Sailing in the Caribbean",
         "description": "Set sail on a luxurious yacht and explore the pristine waters of the Caribbean. Relax on sun-drenched beaches, snorkel among colorful coral reefs, and experience the laid-back island lifestyle.",
         "destination_city": "Caribbean", "start_date": datetime.date(2025, 4, 1),
         "end_date": datetime.date(2025, 4, 10), "is_private": False, "image_name": "13.jpg"},
    ]

    for plan_info in trip_plans:
        add_trip_plan(plan_info)

    comments = [
        {"user": user_alice, "trip_plan": TripPlan.objects.get(title="Exploring the Amazon Rainforest"),
         "comment_content": "Wow, this sounds like an amazing adventure! Can't wait to explore the Amazon!"},
        {"user": user_bob, "trip_plan": TripPlan.objects.get(title="Safari in Serengeti National Park"),
         "comment_content": "The Serengeti is breathtaking! I hope to see the wildlife up close."},
        {"user": user_charlie, "trip_plan": TripPlan.objects.get(title="Road Trip along the Pacific Coast Highway"),
         "comment_content": "I've always wanted to do a road trip along the Pacific Coast! Count me in!"},
        {"user": user_dave, "trip_plan": TripPlan.objects.get(title="Trekking in the Himalayas"),
         "comment_content": "Trekking in the Himalayas has been a dream of mine. Can't wait for this adventure!"},
        {"user": user_eve, "trip_plan": TripPlan.objects.get(title="Cultural Immersion in Kyoto"),
         "comment_content": "Kyoto is so rich in history and culture. I'm excited to explore every corner!"},
        {"user": user_alice, "trip_plan": TripPlan.objects.get(title="Island Hopping in Greece"),
         "comment_content": "Greece has been on my bucket list forever! Island hopping sounds like paradise."},
        {"user": user_bob, "trip_plan": TripPlan.objects.get(title="Exploring the Grand Canyon"),
         "comment_content": "The Grand Canyon is one of those places that leaves you speechless. Can't wait to visit again!"},
        {"user": user_charlie, "trip_plan": TripPlan.objects.get(title="Camping under the Northern Lights"),
         "comment_content": "Camping under the Northern Lights? That's a once-in-a-lifetime experience!"},
        {"user": user_dave, "trip_plan": TripPlan.objects.get(title="Exploring the Great Barrier Reef"),
         "comment_content": "Diving in the Great Barrier Reef has always been a dream of mine. Can't wait for this adventure!"},
        {"user": user_eve, "trip_plan": TripPlan.objects.get(title="Wine Tasting in Tuscany"),
         "comment_content": "Tuscany is the epitome of romance! Looking forward to wine tasting amidst picturesque vineyards."},
        {"user": user_alice, "trip_plan": TripPlan.objects.get(title="Adventure in the Australian Outback"),
         "comment_content": "The Australian Outback is calling my name! Ready for some adrenaline-fueled adventures!"},
        {"user": user_bob, "trip_plan": TripPlan.objects.get(title="Exploring the Inca Trail"),
         "comment_content": "Trekking the Inca Trail to Machu Picchu has been on my bucket list forever! So excited!"},
        {"user": user_charlie, "trip_plan": TripPlan.objects.get(title="Sailing in the Caribbean"),
         "comment_content": "Sailing in the Caribbean? Yes, please! Can't wait to relax on those beautiful beaches."},
        {"user": user_dave, "trip_plan": TripPlan.objects.get(title="Exploring the Amazon Rainforest"),
         "comment_content": "I've always been fascinated by the Amazon Rainforest. This trip is a dream come true!"},
        {"user": user_eve, "trip_plan": TripPlan.objects.get(title="Cultural Immersion in Kyoto"),
         "comment_content": "The blend of tradition and modernity in Kyoto is simply mesmerizing! Can't wait to explore!"},
        {"user": user_alice, "trip_plan": TripPlan.objects.get(title="Island Hopping in Greece"),
         "comment_content": "Greece is so picturesque! Island hopping will be the highlight of my year!"},
        {"user": user_bob, "trip_plan": TripPlan.objects.get(title="Exploring the Grand Canyon"),
         "comment_content": "The Grand Canyon is one of those places that stays with you forever. Can't wait to go back!"},
        {"user": user_charlie, "trip_plan": TripPlan.objects.get(title="Camping under the Northern Lights"),
         "comment_content": "Camping under the Northern Lights? Sign me up! This is a dream come true!"},
        {"user": user_dave, "trip_plan": TripPlan.objects.get(title="Exploring the Great Barrier Reef"),
         "comment_content": "Diving in the Great Barrier Reef has been on my bucket list for years! So excited for this trip!"},
        {"user": user_eve, "trip_plan": TripPlan.objects.get(title="Wine Tasting in Tuscany"),
         "comment_content": "Tuscany's rolling hills and vineyards are calling my name! Can't wait to indulge in some fine wines!"},
    ]

    for comment_info in comments:
        add_comment(comment_info)

    # Likes
    likes = [
        {"user": user_alice, "trip_plan": TripPlan.objects.get(title="Exploring the Amazon Rainforest")},
        {"user": user_bob, "trip_plan": TripPlan.objects.get(title="Safari in Serengeti National Park")},
        {"user": user_charlie, "trip_plan": TripPlan.objects.get(title="Road Trip along the Pacific Coast Highway")},
        {"user": user_dave, "trip_plan": TripPlan.objects.get(title="Trekking in the Himalayas")},
        {"user": user_eve, "trip_plan": TripPlan.objects.get(title="Cultural Immersion in Kyoto")},
        {"user": user_alice, "trip_plan": TripPlan.objects.get(title="Island Hopping in Greece")},
        {"user": user_bob, "trip_plan": TripPlan.objects.get(title="Exploring the Grand Canyon")},
        {"user": user_charlie, "trip_plan": TripPlan.objects.get(title="Camping under the Northern Lights")},
        {"user": user_dave, "trip_plan": TripPlan.objects.get(title="Exploring the Great Barrier Reef")},
        {"user": user_eve, "trip_plan": TripPlan.objects.get(title="Wine Tasting in Tuscany")},
        {"user": user_alice, "trip_plan": TripPlan.objects.get(title="Adventure in the Australian Outback")},
        {"user": user_bob, "trip_plan": TripPlan.objects.get(title="Exploring the Inca Trail")},
        {"user": user_charlie, "trip_plan": TripPlan.objects.get(title="Sailing in the Caribbean")},
        {"user": user_dave, "trip_plan": TripPlan.objects.get(title="Exploring the Amazon Rainforest")},
        {"user": user_eve, "trip_plan": TripPlan.objects.get(title="Cultural Immersion in Kyoto")},
        {"user": user_alice, "trip_plan": TripPlan.objects.get(title="Island Hopping in Greece")},
        {"user": user_bob, "trip_plan": TripPlan.objects.get(title="Exploring the Grand Canyon")},
        {"user": user_charlie, "trip_plan": TripPlan.objects.get(title="Camping under the Northern Lights")},
        {"user": user_dave, "trip_plan": TripPlan.objects.get(title="Exploring the Great Barrier Reef")},
        {"user": user_eve, "trip_plan": TripPlan.objects.get(title="Wine Tasting in Tuscany")}
    ]

    for like_info in likes:
        add_like(like_info)


def add_user(username, email, password):
    user, created = User.objects.get_or_create(username=username, email=email)
    if created:
        user.set_password(password)
        user.save()
    return user


def add_user_profile(profile_info):
    user = profile_info["user"]
    gender = profile_info["gender"]
    age = profile_info["age"]
    bio = profile_info["bio"]
    image_name = profile_info["image_name"]

    # Construct the URL for the profile image using MEDIA_URL
    image_url = os.path.join('profile_images', image_name)

    profile = UserProfile.objects.get_or_create(user=user, gender=gender, age=age, bio=bio, picture=image_url)[0]
    profile.save()
    return profile


def add_trip_plan(plan_info):
    user = plan_info["user"]
    title = plan_info["title"]
    description = plan_info["description"]
    destination_city = plan_info["destination_city"]
    start_date = plan_info["start_date"]
    end_date = plan_info["end_date"]
    is_private = plan_info["is_private"]
    image_name = plan_info["image_name"]
    print(user.username)

    # Construct the URL for the trip image using MEDIA_URL
    image_url = os.path.join('trip_images', image_name)

    trip_plan = TripPlan(user=user, title=title, description=description, destination_city=destination_city,
                         start_date=start_date, end_date=end_date, is_private=is_private, image=image_url)
    trip_plan.full_clean()  # Validate the trip plan data
    trip_plan.save()
    return trip_plan


def add_comment(comment_info):
    user = comment_info["user"]
    trip_plan = comment_info["trip_plan"]
    comment_content = comment_info["comment_content"]

    comment = Comment.objects.create(user=user, trip_plan=trip_plan, comment_content=comment_content)
    return comment


def add_like(like_info):
    user = like_info["user"]
    trip_plan = like_info["trip_plan"]

    like, created = LikePost.objects.get_or_create(user=user, trip_plan=trip_plan)
    return like


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()

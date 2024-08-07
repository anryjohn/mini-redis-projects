# Mini Redis Projects
This is a directory containing a number of small-scale Redis and Flask based applications and utilities as a means of
getting more familiar with the technology. To run each of the apps, install the necessary dependencies listed
in each of the apps requirements.txt file using the following command

    pip install -r requirements.txt

The apps included are as follows:

## Event Tracker

This is a basic Real-Time Analytics project that is designed to provide real-time event tracking and a dashboard system. It includes two main components:

1. **Event Tracker (`event_tracker.py`)**: A Flask application that tracks and records events in real time and stores them in Redis.
2. **Dashboard (`dashboard.py`)**: A Flask application that visualizes the events and provides real-time analytics via a web interface.

To run this application, run the following commands:

    python event-tracker/event-tracker.py 
    # This following command must ben ran in a separate terminal
    python event-tracker/dashboard.py

## Rate Limiter

This is a simple API rate limiting solution using Flask and Redis. It provides a mechanism to control the number of requests a user can make to an API endpoint within a given time window. This helps prevent abuse and ensures fair usage of resources. The

To run this application, run the following commands:

    python rate-limiter/rate-limiter.py


## URL Shortener

The URL Shortener project is a simple web application built with Flask and Redis that allows users to shorten long URLs and redirect them to their original destinations. It provides a straightforward API for creating and resolving shortened URLs.

To run this application, run the following commands:

    python url-shortener/url-shortener.py 
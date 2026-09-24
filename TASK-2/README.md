# Event Reservation API

## 1. Project Description

The Event Reservation API is a REST API developed using FastAPI and SQLModel.

It is used to manage college events such as workshops, hackathons, seminars, and technical events. Students can reserve seats for events, view reservations, check availability, and cancel reservations.

The application uses SQLite for storing event and reservation data.

## 2. Technologies Used

- Python
- FastAPI
- SQLModel
- Pydantic
- SQLite

## 3. Database Models

### Event

The Event model contains:

- id
- title
- venue
- capacity
- organizer
- status

### Reservation

The Reservation model contains:

- id
- event_id
- student_name
- roll_number
- email

## 4. Installation Steps

### Step 1: Create a virtual environment

```bash
python -m venv .venv

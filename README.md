# 🌸 The Flora Project - Unsent Messages Archive

A beautiful Django web application that serves as an archive for unsent messages to loved ones. Users can anonymously or with their name share heartfelt, unsent messages that they never got to send.

## ✨ Features

### 1. **Message Submission**
- Submit messages with optional sender name (can be anonymous)
- Required receiver name field
- Clean, beautiful form interface
- Messages are instantly added to the archive

### 2. **Search Functionality**
- Case-insensitive search for both sender and receiver names
- Search works with any capitalization: JB, Jb, jB, jb all return the same results
- Real-time search results display
- Search results show message count

### 3. **Random Color Generator**
- Each message card displays with a random vibrant color
- Colors change on every page load/refresh
- Full message view also shows random colors for visual variety
- 25+ unique color palette for visual appeal

### 4. **Message Display**
- Recent messages displayed on homepage
- Full message view with expanded content
- Timestamp display for each message
- #thefloraproject hashtag on every message

### 5. **Admin Interface**
- Django admin panel for message management
- View and moderate messages
- Message preview in admin list view
- Search messages by content, sender, or receiver
- Filter by creation date

## 🛠️ Technology Stack

- **Backend**: Django 6.0.1
- **Database**: SQLite
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Python**: 3.x

## 📁 Project Structure

```
sitenijb/
├── manage.py                 # Django management script
├── db.sqlite3               # Database file
├── homepage/                # Main Django app
│   ├── models.py           # UnsentMessage model
│   ├── views.py            # View functions
│   ├── urls.py             # URL routing
│   ├── forms.py            # Django forms
│   ├── admin.py            # Admin configuration
│   ├── migrations/         # Database migrations
│   └── templates/
│       └── homepage/
│           ├── home.html              # Homepage
│           ├── message_detail.html    # Individual message view
│           └── search.html            # Search results page
└── sitenijb/               # Django project settings
    ├── settings.py         # Project settings
    ├── urls.py            # Main URL configuration
    ├── wsgi.py            # WSGI configuration
    └── asgi.py            # ASGI configuration
```

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- Django 6.0.1

### Installation

1. **Navigate to the project directory**
```bash
cd c:\Users\Acer\Desktop\django_lesson\sitenijb
```

2. **Install Django** (if not already installed)
```bash
pip install django
```

3. **Apply migrations** (already done, but if needed)
```bash
python manage.py migrate
```

4. **Start the development server**
```bash
python manage.py runserver
```

5. **Access the website**
- Open browser and go to: `http://localhost:8000`
- Admin panel: `http://localhost:8000/admin`

## 📋 Database Schema

### UnsentMessage Model
```
- id (Auto-generated Primary Key)
- sender_name (CharField, max_length=100, optional, nullable)
- receiver_name (CharField, max_length=100, required)
- message_content (TextField)
- created_at (DateTimeField, auto-generated)
```

## 🎨 Color Palette

The application uses a carefully selected palette of 25+ vibrant colors:
- #FF6B6B, #4ECDC4, #45B7D1, #FFA07A, #98D8C8
- #F7DC6F, #BB8FCE, #85C1E2, #F8B88B, #A9DFBF
- #F1948A, #AED6F1, #F9E79F, #D7BDE2, #A3E4D7
- #F5B7B1, #AEB6BF, #F9E2AF, #D2B4DE, #81C784
- #64B5F6, #FFB74D, #E57373, #81C784, #64B5F6

## 🔍 Search Guide

The search feature is case-insensitive and searches both:
- Sender names
- Receiver names

**Examples:**
- Searching "jb" will find messages from/to "JB", "Jb", "jB", "jb"
- Searching "john" will find messages from/to "john", "John", "JOHN", "JoHn"
- Partial matches work: "joh" will find "John"

## 📝 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET, POST | Homepage - display recent messages or submit new message |
| `/search/` | GET | Search messages by sender/receiver name |
| `/message/<id>/` | GET | View full individual message with random color |
| `/admin/` | GET | Django admin interface |

## 🎯 Usage

### To Submit a Message:
1. Go to the homepage
2. Fill in your name (optional) or leave blank for anonymous
3. Enter the receiver's name
4. Write your message
5. Click "Send to Archive"

### To Search Messages:
1. Use the search bar on any page
2. Enter a sender or receiver name
3. Results display with random colors
4. Click "View Full Message" to see the complete message

### To Manage Messages (Admin):
1. Go to `/admin/`
2. Log in with admin credentials
3. Navigate to "Unsent Messages"
4. View, edit, or delete messages as needed

## 🎨 Visual Features

- **Gradient Background**: Beautiful purple gradient throughout
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Smooth Animations**: Fade-in and slide-up effects on page load
- **Hover Effects**: Cards lift up on hover for better interactivity
- **Color-coded Messages**: Each message has a unique random background color
- **Typography**: Clean, modern fonts with proper hierarchy

## 🌟 Key Features Explained

### Case-Insensitive Search
All searches are done using Django's `__icontains` lookup, making searches completely case-insensitive:
```python
Q(sender_name__icontains=search_query) | 
Q(receiver_name__icontains=search_query)
```

### Random Color Generation
Colors are generated fresh on each page view using Python's `random.choice()`:
```python
def get_random_colors():
    colors = [/* list of hex colors */]
    return random.choice(colors)
```

### Message Display
- Recent messages on homepage (limited to 10)
- Full detail view with all message content
- Timestamps formatted for readability
- Hashtag #thefloraproject on every message

## 🔐 Security Features

- CSRF protection on all forms
- Secure admin interface
- User input validation through Django forms
- SQL injection prevention through ORM

## 📦 Dependencies

```
Django==6.0.1
asgiref>=3.9.1
sqlparse>=0.5.0
tzdata
```

## 🚀 Deployment Considerations

For production deployment:
1. Set `DEBUG = False` in settings.py
2. Generate a new SECRET_KEY
3. Add your domain to ALLOWED_HOSTS
4. Use a production-grade database (PostgreSQL recommended)
5. Serve static files through a web server (Nginx/Apache)
6. Use environment variables for sensitive data

## 🐛 Troubleshooting

### Django not found error:
```bash
pip install django
```

### Database errors:
```bash
python manage.py migrate
```

### Port 8000 already in use:
```bash
python manage.py runserver 8001
```

## 📄 License

This project is open source and available for personal and educational use.

## 💝 About The Flora Project

The Flora Project is inspired by the idea that sometimes the most meaningful messages are the ones that never get sent. This archive gives voice to those unspoken words, creating a beautiful collection of emotional honesty and human connection.

---

**Created with ❤️ for heartfelt moments**

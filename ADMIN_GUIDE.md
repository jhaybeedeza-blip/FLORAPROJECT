# 🌸 The Flora Project - Admin Guide

## 🔐 Admin Access

### Login Credentials:
- **Username**: `admin`
- **Password**: `admin123`
- **Admin Panel URL**: `http://localhost:8000/admin/`

## 📋 Admin Features

### Manage Messages
In the admin panel, you can:

1. **View All Messages**
   - See all unsent messages submitted to the archive
   - Filter by creation date
   - Search by sender name, receiver name, or message content

2. **Delete Messages**
   - Select messages to delete
   - Use bulk actions to delete multiple messages at once
   - Message will be permanently removed from the archive

3. **Edit Messages**
   - View full message details
   - Edit sender name or receiver name
   - Edit the message content
   - View when the message was created

4. **Filter & Search**
   - Filter messages by date range
   - Search by partial text match
   - Sort by newest or oldest first

### Admin Interface Features:
- Message preview in list view
- Timestamps for all messages
- Bulk delete actions
- Advanced search capabilities

## 🚀 To Access Admin Panel:

1. Make sure the Django server is running:
   ```bash
   python manage.py runserver
   ```

2. Go to: `http://localhost:8000/admin/`

3. Enter credentials:
   - Username: `admin`
   - Password: `admin123`

4. Click "Log In"

## 📝 Message Management

### Delete a Single Message:
1. Go to "Unsent Messages" in admin
2. Click on the message you want to delete
3. Scroll down and click "Delete"
4. Confirm deletion

### Delete Multiple Messages:
1. Go to "Unsent Messages" in admin
2. Check the boxes next to messages to delete
3. From "Action" dropdown, select "Delete selected unsent messages"
4. Click "Go"
5. Confirm deletion

### View Message Details:
1. Go to "Unsent Messages" in admin
2. Click any message to see full details
3. View sender, receiver, content, and timestamp
4. Make edits if needed and save

## 🔍 Searching in Admin:

Use the search bar to find messages:
- Search by sender name (e.g., "John")
- Search by receiver name (e.g., "Sarah")
- Search by message content (e.g., "love" or "sorry")

Search is case-insensitive and matches partial text.

## ⚙️ Admin Dashboard Overview

The admin dashboard shows:
- **Recent Messages**: Newest messages submitted
- **Message Preview**: First 75 characters of each message
- **Creation Date**: When each message was added
- **Filter Options**: By date range
- **Search Function**: By sender, receiver, or content

## 🆘 Troubleshooting

**Forgot password?**
```bash
python manage.py changepassword admin
```

**Want to create another admin user?**
```bash
python manage.py createsuperuser
```

**Reset admin user to default password:**
```bash
cd sitenijb
python create_superuser.py
```

## 📱 Important Notes

- Only logged-in admins can delete messages
- Deletions are permanent - no undo
- You can edit any message after submission
- All admin actions are logged in Django
- Timestamps are automatically recorded for each message

---

**Stay in control of your archive! 🌸**

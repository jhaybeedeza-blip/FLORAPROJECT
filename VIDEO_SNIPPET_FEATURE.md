# 🎥 Video Loop & Volume Control + 🎵 Song Snippet Selector - Implementation Guide

## Overview
Three major features have been added to The Flora Project:

### 1. **Video Loop & Volume Control** ✅
- Videos now loop automatically when they finish
- Custom volume slider with percentage display
- Volume level indicator (🔊/🔉/🔇)

### 2. **Song Snippet Selector** ✅
- Drag-to-select song portions with two range sliders
- Real-time preview of selected snippet
- Time display: Start, End, Duration
- Automatic playback stop at end time

### 3. **Song Snippet Playback** ✅
- Messages with snippets play only the selected portion
- Displays snippet info on message detail page
- Auto-restarts at beginning when snippet ends

---

## File Changes

### Backend Files

#### [models.py](sitenijb/homepage/models.py)
- Added `music_start_time` (FloatField) - Start time in seconds
- Added `music_end_time` (FloatField) - End time in seconds
- Added `get_music_snippet_data()` method - Returns snippet timing info

#### [forms.py](sitenijb/homepage/forms.py)
- Added `music_start_time` field - Hidden input for start time
- Added `music_end_time` field - Hidden input for end time
- Updated form fields list to include snippet fields
- Updated `presetMusicSelect` to have ID for JavaScript integration

#### [0008_add_music_snippet.py](sitenijb/homepage/migrations/0008_add_music_snippet.py)
- New migration file to add music snippet fields to database

### Frontend Files

#### [home.html](sitenijb/homepage/templates/homepage/home.html)
**CSS Additions:**
- `.song-snippet-selector` - Container for snippet selector
- `.snippet-controls` - Control buttons layout
- `.snippet-range-container` - Range slider container
- `.snippet-range` - Custom styled range slider
- `.snippet-preview` - Preview audio player container

**HTML Additions:**
- Song snippet selector section with:
  - Two range sliders (start/end time)
  - Time display (start, end, duration)
  - Preview audio player
  - Selected length display

**JavaScript Additions:**
- Event listeners for preset music selection
- Range slider input handlers
- Time formatting function (MM:SS)
- Preview audio management
- Hidden field population (music_start_time, music_end_time)
- Auto-stop at end time during preview

#### [message_detail.html](sitenijb/homepage/templates/homepage/message_detail.html)
**Video Section Updates:**
- Added `loop` attribute to video element
- Custom volume control slider
- Volume percentage display
- JavaScript volume handler

**Music Player Updates:**
- Displays snippet info if available
- Shows start time, end time, and duration
- JavaScript detects snippet times from page
- Implements `timeupdate` event to stop at snippet end
- Auto-rewinds to start when snippet ends

---

## User Interface Features

### On Message Submission (home.html)
1. User selects preset music from dropdown
2. Song snippet selector appears
3. User drags two sliders:
   - **Start slider**: Sets where snippet begins
   - **End slider**: Sets where snippet ends
4. Real-time preview plays selected portion
5. Time displays update as sliders move
6. Values automatically saved to hidden form fields
7. Submit button sends message with snippet data

### On Message Display (message_detail.html)
1. Video plays with:
   - Built-in browser controls
   - **Loop enabled** - repeats automatically
   - **Volume slider** - 0-100% with emoji feedback
2. Music player shows snippet info:
   - "🎵 Song Snippet: Start: Xs — End: Ys"
   - Duration calculation
3. When playing:
   - Starts from snippet start time
   - Automatically stops at end time
   - Restarts at beginning for next play

---

## JavaScript Features

### Song Snippet Selector (home.html)
```javascript
// Format time as MM:SS
formatTime(seconds) → "1:23"

// On preset music change:
- Load audio file
- Get duration
- Set max values for sliders
- Reset sliders to default (0 to 30s)

// On slider move:
- Update time displays
- Prevent start > end or end < start
- Calculate duration
- Update hidden form fields
- Set audio preview time
```

### Video Volume Control (message_detail.html)
```javascript
// On volume slider input:
- Set video volume (0.0 to 1.0)
- Update percentage display
- Video maintains volume on loop

// Video properties:
- loop="true" → auto-restart
- controlsList="nodownload" → hide download button
```

### Song Snippet Playback (message_detail.html)
```javascript
// On audio timeupdate:
if (currentTime >= snippetEnd) {
  - Pause audio
  - Reset to snippetStart
  - Update play button display
}

// On play button click:
if (snippetStart exists) {
  - Jump to snippetStart time
  - Begin playback
}
```

---

## Database Schema

### UnsentMessage Model
```python
music_start_time = FloatField(
    blank=True,
    null=True,
    default=0,
    help_text="Song snippet start time in seconds"
)

music_end_time = FloatField(
    blank=True,
    null=True,
    help_text="Song snippet end time in seconds"
)
```

---

## How to Use

### As an Admin
1. Run migration: `python manage.py migrate`
2. View messages in admin panel
3. See music snippet times in message details

### As a User
1. **Creating a Message with Song Snippet:**
   - Fill in message content
   - Select preset music from dropdown
   - Range sliders appear
   - Drag to select portion of song
   - Listen to preview
   - Click Send

2. **Viewing a Message with Video:**
   - Video auto-loops at end
   - Use volume slider (0-100%)
   - Volume persists across loops

3. **Viewing a Message with Song Snippet:**
   - See snippet time info
   - Only selected portion plays
   - Auto-stops and restarts at snippet beginning

---

## Browser Compatibility
- HTML5 Video with loop: ✅ All modern browsers
- HTML5 Audio with timeupdate: ✅ All modern browsers
- Range slider styling: ✅ Chrome, Firefox, Safari, Edge
- Web Audio API (visualizer): ✅ Chrome, Firefox, Safari, Edge

---

## Styling Notes
- All controls use project's purple gradient (#667eea to #764ba2)
- Range sliders have custom thumbs and tracks
- Volume control shows emoji feedback (🔊/🔉/🔇)
- Snippet selector matches form styling
- Responsive design: works on mobile and desktop

---

## Testing Checklist
- [ ] Upload video and verify loop works
- [ ] Test video volume slider (0%, 50%, 100%)
- [ ] Select preset music and see snippet selector
- [ ] Drag start slider - preview updates
- [ ] Drag end slider - preview updates
- [ ] Prevent start > end with sliders
- [ ] Submit form with snippet selected
- [ ] View message detail with snippet
- [ ] Verify snippet plays only selected portion
- [ ] Verify snippet auto-stops at end time

---

## Customization Options

### Adjust Default Snippet Length (home.html)
```javascript
snippetEnd.value = Math.min(duration, 30); // Change 30 to desired default
```

### Change Video Loop Behavior
```html
<!-- Change loop to: -->
<!-- No loop: remove "loop" attribute -->
<!-- Custom loop count: handle via JavaScript timeupdate -->
```

### Modify Volume Control
```html
<!-- Change slider range: -->
min="0" max="100" step="5" <!-- Use step="5" for 5% increments -->
```

### Customize Time Display Format
```javascript
// Modify formatTime() function for different format:
// "1m 23s" format, "1:23:45" for hours, etc.
```

---

## Known Limitations
- Video loop requires browser support for HTML5 video loop
- Volume control is visual only (no system-level control)
- Song snippet requires audio file to be accessible
- Preview accuracy depends on browser audio implementation
- Very long songs (>10min) may have browser performance impact

---

## Future Enhancements
- [ ] Visual waveform display for audio selection
- [ ] Audio visualization during snippet preview
- [ ] Fade-in/fade-out effects at snippet boundaries
- [ ] Save frequently used snippets as templates
- [ ] Audio equalizer controls
- [ ] Multiple audio tracks support


# 🎬 Visual Guide - Video Loop, Volume Control & Song Snippet Selector

## 1. VIDEO PLAYBACK WITH LOOP & VOLUME CONTROL
### Message Detail Page

```
┌─────────────────────────────────────────────────┐
│  Your Video Message                             │
├─────────────────────────────────────────────────┤
│                                                  │
│  ┌───────────────────────────────────────────┐  │
│  │                                           │  │
│  │         VIDEO PREVIEW (LOOPING)           │  │
│  │    Automatically restarts when finished   │  │
│  │                                           │  │
│  └───────────────────────────────────────────┘  │
│                                                  │
│  Volume Control Panel:                          │
│  ┌──────────────────────────────────────────┐   │
│  │ 🔊  [===============●=====]  100%        │   │
│  └──────────────────────────────────────────┘   │
│       ↑                                          │
│    Volume                                       │
│    Slider                                       │
│                                                  │
└─────────────────────────────────────────────────┘

Features:
✅ Video loops infinitely
✅ Volume range: 0% - 100%
✅ Emoji feedback: 🔊 (loud) 🔉 (medium) 🔇 (silent)
✅ Volume persists across loops
```

---

## 2. SONG SNIPPET SELECTOR
### Message Submission Form (home.html)

```
┌──────────────────────────────────────────────────────┐
│  💌 Share Your Unsent Message                        │
├──────────────────────────────────────────────────────┤
│                                                       │
│  Message Content: [textarea]                         │
│                                                       │
│  🎵 Select Preset Music: [Dropdown ▼]               │
│      └─ Song1.mp3 (selected)                        │
│      └─ Song2.mp3                                   │
│      └─ Song3.mp3                                   │
│                                                       │
│  ┌────────────────────────────────────────────────┐ │
│  │ 🎵 Select Song Snippet (Drag to Choose)        │ │
│  ├────────────────────────────────────────────────┤ │
│  │                                                 │ │
│  │ Start: 0:15   Duration: 1:30   End: 1:45       │ │
│  │                                                 │ │
│  │ [START SLIDER]                                  │ │
│  │ ●═══════════════════════════════════════════   │ │
│  │                                                 │ │
│  │ [END SLIDER]                                    │ │
│  │ ═════════════════════════════════════════●     │ │
│  │                                                 │ │
│  ├────────────────────────────────────────────────┤ │
│  │ 🎧 Preview Selected Snippet                    │ │
│  │                                                 │ │
│  │ [Play] [====●====] [Volume] [Time]              │ │
│  │                                                 │ │
│  │ Selected length: 1:30                           │ │
│  │                                                 │ │
│  └────────────────────────────────────────────────┘ │
│                                                       │
│  [SEND BUTTON]                                       │
│                                                       │
└──────────────────────────────────────────────────────┘
```

### Slider Behavior

```
RANGE 1: START TIME
┌──────────────────────────────┐
│ Full Song: [════════════════│
│           0:00           1:50 │
│                               │
│ START SLIDER:                 │
│ ●════════════════════════════ │
│ 0:15 (User dragged here)      │
└──────────────────────────────┘

RANGE 2: END TIME
┌──────────────────────────────┐
│ Full Song: [════════════════│
│           0:00           1:50 │
│                               │
│ END SLIDER:                   │
│ ════════════════════════════● │
│           1:45 (User dragged) │
└──────────────────────────────┘

SELECTED SNIPPET: 0:15 to 1:45 (Duration: 1:30)
┌──────────────────────────────┐
│ Only this part plays:         │
│ [────●════════════════●──────│
│ 0:15          1:45      1:50  │
│ (start)       (end)           │
└──────────────────────────────┘
```

---

## 3. TIME DISPLAY UPDATES

```
User drags START slider to 0:15
↓
┌──────────────────────────────────────┐
│ Start: 0:15  Duration: 1:30  End: 1:45 │
│            (auto-calculated)            │
└──────────────────────────────────────┘

User drags END slider to 1:45
↓
┌──────────────────────────────────────┐
│ Start: 0:15  Duration: 1:30  End: 1:45 │
│            (auto-updated)               │
└──────────────────────────────────────┘

Preview audio player:
↓
Audio starts at 0:15
Plays until 1:45
Auto-stops
Shows "Selected length: 1:30"
```

---

## 4. SONG SNIPPET PLAYBACK ON MESSAGE VIEW

```
MESSAGE DETAIL PAGE
┌──────────────────────────────────────────────────┐
│  Message from: John → Sarah                      │
│  📅 Jan 15, 2025                                 │
├──────────────────────────────────────────────────┤
│                                                   │
│  "This song reminds me of you..."                │
│                                                   │
│  ┌─────────────────────────────────────────────┐ │
│  │ 🎵 Song Snippet:                            │ │
│  │ Start: 0:15s — End: 1:45s                   │ │
│  │ Duration: 1:30                              │ │
│  └─────────────────────────────────────────────┘ │
│                                                   │
│  ┌─────────────────────────────────────────────┐ │
│  │ [▶]   [🔊] [───────●─────] [🔇] [🔉] [🔊]   │ │
│  │       Volume Control + Mute                 │ │
│  └─────────────────────────────────────────────┘ │
│                                                   │
│  Waveform visualizer (optional)                  │
│  [═════════════════════════════════════════]    │
│                                                   │
│  #thefloraproject                                │
│                                                   │
└──────────────────────────────────────────────────┘

User clicks Play (▶):
1. Audio jumps to 0:15s (snippet start)
2. Song plays normally
3. At 1:45s (snippet end):
   - Audio automatically stops
   - Play button shows ▶ again
   - Next click restarts from 0:15s

Behavior: Song plays 0:15 → 1:45, stops, repeats
```

---

## 5. COLOR & STYLING

### Purple Theme (existing project)
```
Primary:   #667eea (Light Purple)
Secondary: #764ba2 (Dark Purple)
Accent:    White, Transparent overlays

Song Snippet Selector:
├─ Background: rgba(102, 126, 234, 0.1) - very light purple
├─ Border: 2px solid #667eea - medium purple
├─ Sliders: Linear gradient #667eea → #764ba2
├─ Thumb: White with purple border
└─ Text: Dark gray on light background

Video Volume Control:
├─ Background: rgba(255,255,255,0.1) - semi-transparent
├─ Text: White
├─ Slider accent: rgba(255,255,255,0.8)
└─ Layout: Rounded pill shape
```

---

## 6. INTERACTION FLOW

### CREATING MESSAGE WITH SNIPPET

```
START: Message form loaded
   ↓
[USER INPUT]
1. Type message
2. Select preset music from dropdown
   ↓
[AUTO TRIGGER]
Song snippet selector appears with animation
   ↓
[USER INTERACTION]
3. Drag START slider ← → (shows time in real-time)
4. Drag END slider ← → (shows time in real-time)
5. Adjust until desired portion selected
6. Listen to preview if needed
   ↓
[AUTO SAVE]
Hidden fields populated:
- music_start_time = 15 (seconds)
- music_end_time = 105 (seconds)
   ↓
7. Click SEND button
   ↓
[SUBMIT]
Form posts with snippet data to backend
Message saved with snippet times in database
   ↓
SUCCESS: Message created with song snippet
```

### VIEWING MESSAGE WITH SNIPPET

```
START: Message detail page loads
   ↓
[DISPLAY]
Shows snippet info: "🎵 Song Snippet: Start: 0:15s — End: 1:45s"
   ↓
[LOAD AUDIO]
Audio file loaded with snippet boundaries
   ↓
[USER INTERACTION]
User clicks Play button
   ↓
[JAVASCRIPT LOGIC]
1. Check if snippet exists
2. If yes: currentTime = snippetStart (0:15s)
3. Start playback
   ↓
[PLAYBACK]
Audio plays from 0:15s → 1:45s
   ↓
[AUTO STOP]
timeupdate event detects currentTime >= snippetEnd
Pause audio
Reset currentTime = snippetStart
Update play button to ▶
   ↓
[USER CAN REPLAY]
Next play click restarts snippet from beginning
```

---

## 7. RESPONSIVE LAYOUT

### Desktop (Wide screens)
```
┌──────────────────────────────────────┐
│  Full width slider                   │
│  ●──────────────────────────────────│
└──────────────────────────────────────┘

┌──────────────────────────────────────┐
│  Preview player inline                │
│  [▶] ════════ [🔊][Volume]           │
└──────────────────────────────────────┘
```

### Mobile (Small screens)
```
┌──────────────┐
│ Full width   │
│ ●────────── │
│ slider      │
│             │
│ ●────────── │
│ slider      │
│             │
│ [▶] [🔊]    │
│ [volume]    │
└──────────────┘
```

---

## 8. STATE INDICATORS

### Video Volume Slider States
```
0%   → 🔇 MUTED (red visual)
1-49% → 🔉 QUIET (orange visual)
50-99% → 🔊 LOUD (green visual)
100% → 🔊 MAX (bright green visual)
```

### Song Snippet Selector States
```
NO MUSIC SELECTED
└─ Snippet selector hidden

MUSIC SELECTED
├─ Snippet selector visible
├─ Sliders set to: Start=0, End=min(30s, song_duration)
├─ Preview audio ready
└─ User can drag

PREVIEW PLAYING
├─ Audio plays from Start → End
├─ Auto-stops at End
├─ Time updates shown
└─ Duration calculation active

FORM SUBMITTED
├─ Hidden fields populated
├─ Start/End times saved
└─ Message created with snippet data
```

---

## 9. KEYBOARD SHORTCUTS (Future Enhancement)

```
Possible additions:
├─ Space: Play/Pause
├─ ← →: Move snippet boundaries by 1 second
├─ Shift+← →: Move by 5 seconds
├─ Volume up/down: Arrow keys
└─ M: Mute/Unmute
```

---

## 10. ACCESSIBILITY FEATURES

```
Video Controls:
✅ label="Video Volume" for screen readers
✅ title attributes on all controls
✅ Keyboard accessible range sliders
✅ Emoji + text labels (not emoji only)

Song Snippet Selector:
✅ "Select Song Snippet" heading
✅ Time displayed numerically (not just visual)
✅ Label for each slider
✅ Instructions in form

Color:
✅ Not relying on color alone
✅ Emoji icons for quick recognition
✅ High contrast on light/dark backgrounds
```


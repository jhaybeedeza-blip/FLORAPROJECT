# 🔍 CODE SNIPPETS - Video Loop, Volume & Song Snippet Implementation

## 1. MODEL UPDATES (models.py)

### Added Fields
```python
from django.db import models
import json

class UnsentMessage(models.Model):
    # ... existing fields ...
    
    # NEW FIELDS:
    music_start_time = models.FloatField(
        blank=True, 
        null=True, 
        default=0, 
        help_text="Song snippet start time in seconds"
    )
    music_end_time = models.FloatField(
        blank=True, 
        null=True, 
        help_text="Song snippet end time in seconds"
    )
    
    # ... existing methods ...
    
    def get_music_snippet_data(self):
        """Return music snippet timing info as dict"""
        if self.music_start_time is not None or self.music_end_time is not None:
            return {
                'start': float(self.music_start_time or 0),
                'end': float(self.music_end_time or 0),
                'duration': float((self.music_end_time or 0) - (self.music_start_time or 0))
            }
        return None
```

---

## 2. FORM UPDATES (forms.py)

### Added Form Fields
```python
class UnsentMessageForm(forms.ModelForm):
    preset_music = forms.ChoiceField(
        choices=get_preset_music_choices(),
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'presetMusicSelect'  # ADDED ID
        }),
        label='🎵 Select Preset Music'
    )
    
    # NEW FIELDS:
    music_start_time = forms.FloatField(
        required=False,
        initial=0,
        widget=forms.HiddenInput(attrs={
            'id': 'musicStartTime'
        }),
        label='Music Start Time'
    )
    
    music_end_time = forms.FloatField(
        required=False,
        widget=forms.HiddenInput(attrs={
            'id': 'musicEndTime'
        }),
        label='Music End Time'
    )
    
    class Meta:
        model = UnsentMessage
        # UPDATED: Added new fields to list
        fields = [
            'sender_name', 'receiver_name', 'message_content', 
            'preset_music', 'music_file', 
            'music_start_time', 'music_end_time',  # NEW
            'voicemail', 'image_file', 'video_clip', 'ghost_draft'
        ]
        widgets = {
            # ... existing widgets ...
        }
```

---

## 3. MIGRATION FILE (0008_add_music_snippet.py)

```python
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_add_ghost_draft'),
    ]

    operations = [
        migrations.AddField(
            model_name='unsentmessage',
            name='music_start_time',
            field=models.FloatField(
                blank=True, 
                default=0, 
                help_text='Song snippet start time in seconds', 
                null=True
            ),
        ),
        migrations.AddField(
            model_name='unsentmessage',
            name='music_end_time',
            field=models.FloatField(
                blank=True, 
                help_text='Song snippet end time in seconds', 
                null=True
            ),
        ),
    ]
```

---

## 4. HOME.HTML - CSS ADDITIONS

### Song Snippet Selector Styles
```css
.song-snippet-selector {
    background: rgba(102, 126, 234, 0.1);
    border: 2px solid #667eea;
    padding: 15px;
    border-radius: 8px;
    margin-top: 15px;
    margin-bottom: 15px;
    display: none;
}

.song-snippet-selector.active {
    display: block;
}

.snippet-controls {
    display: flex;
    gap: 10px;
    flex-direction: column;
    margin-bottom: 15px;
}

.snippet-range-container {
    background: white;
    padding: 15px;
    border-radius: 6px;
    margin-bottom: 15px;
}

.range-label {
    display: flex;
    justify-content: space-between;
    margin-bottom: 10px;
    font-size: 0.9em;
    color: #333;
    font-weight: bold;
}

.snippet-range {
    width: 100%;
    height: 8px;
    border-radius: 5px;
    background: linear-gradient(to right, #667eea 0%, #764ba2 100%);
    outline: none;
    -webkit-appearance: none;
    appearance: none;
    cursor: pointer;
}

.snippet-range::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: white;
    border: 3px solid #667eea;
    cursor: pointer;
    box-shadow: 0 2px 8px rgba(102, 126, 234, 0.4);
}

.snippet-range::-moz-range-thumb {
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: white;
    border: 3px solid #667eea;
    cursor: pointer;
    box-shadow: 0 2px 8px rgba(102, 126, 234, 0.4);
}

.snippet-preview {
    background: #f5f5f5;
    border-radius: 6px;
    padding: 15px;
    margin-top: 15px;
    text-align: center;
}

.preview-label {
    font-weight: bold;
    color: #667eea;
    margin-bottom: 10px;
}

.snippet-preview audio {
    width: 100%;
    max-width: 400px;
    margin: 10px 0;
}

.snippet-duration {
    font-size: 0.9em;
    color: #666;
    margin-top: 8px;
}
```

---

## 5. HOME.HTML - HTML ADDITIONS

### Song Snippet Selector HTML
```html
<!-- Song Snippet Selector -->
<div class="song-snippet-selector" id="songSnippetSelector">
    <h4 style="color: #667eea; margin-bottom: 15px;">🎵 Select Song Snippet (Drag to Choose)</h4>
    
    <div class="snippet-range-container">
        <div class="range-label">
            <span>Start: <span id="startDisplay">0:00</span></span>
            <span>Duration: <span id="durationDisplay">0:00</span></span>
            <span>End: <span id="endDisplay">0:00</span></span>
        </div>
        <input type="range" id="snippetStart" class="snippet-range" min="0" max="0" step="0.1" value="0" title="Drag to set start time">
        <div style="height: 8px; margin-top: 10px; border-radius: 5px; background: linear-gradient(to right, #667eea 0%, #764ba2 100%);"></div>
        <input type="range" id="snippetEnd" class="snippet-range" min="0" max="0" step="0.1" value="0" title="Drag to set end time" style="margin-top: 10px;">
    </div>
    
    <div class="snippet-preview">
        <div class="preview-label">🎧 Preview Selected Snippet</div>
        <audio id="snippetAudio" controls style="width: 100%; max-width: 400px;">
            Your browser does not support the audio element.
        </audio>
        <div class="snippet-duration">
            Selected length: <strong id="selectedLength">0:00</strong>
        </div>
    </div>
</div>

<!-- Hidden fields for start/end times -->
{{ form.music_start_time }}
{{ form.music_end_time }}
```

---

## 6. HOME.HTML - JAVASCRIPT ADDITIONS

### Song Snippet Selector JavaScript
```javascript
// Song Snippet Selector - Drag to select part of song
(function() {
    const presetMusicSelect = document.getElementById('presetMusicSelect');
    const snippetSelector = document.getElementById('songSnippetSelector');
    const snippetStart = document.getElementById('snippetStart');
    const snippetEnd = document.getElementById('snippetEnd');
    const snippetAudio = document.getElementById('snippetAudio');
    const startDisplay = document.getElementById('startDisplay');
    const endDisplay = document.getElementById('endDisplay');
    const durationDisplay = document.getElementById('durationDisplay');
    const selectedLength = document.getElementById('selectedLength');
    const musicStartTimeInput = document.getElementById('musicStartTime');
    const musicEndTimeInput = document.getElementById('musicEndTime');
    
    if (!presetMusicSelect) return;
    
    // Format time as MM:SS
    function formatTime(seconds) {
        if (!isFinite(seconds)) return '0:00';
        const mins = Math.floor(seconds / 60);
        const secs = Math.floor(seconds % 60);
        return `${mins}:${secs.toString().padStart(2, '0')}`;
    }
    
    // Update audio source when preset music is selected
    presetMusicSelect.addEventListener('change', function() {
        if (this.value) {
            const musicPath = `/static/music/${this.value}`;
            snippetAudio.src = musicPath;
            snippetSelector.classList.add('active');
            
            // Reset sliders when new song is selected
            snippetStart.value = 0;
            snippetEnd.value = 0;
            musicStartTimeInput.value = 0;
            musicEndTimeInput.value = 0;
            
            // Load metadata to get duration
            snippetAudio.addEventListener('loadedmetadata', function() {
                const duration = snippetAudio.duration;
                snippetStart.max = duration;
                snippetEnd.max = duration;
                snippetEnd.value = Math.min(duration, 30); // Default to 30 seconds or full song
                musicEndTimeInput.value = snippetEnd.value;
                
                startDisplay.textContent = formatTime(0);
                endDisplay.textContent = formatTime(snippetEnd.value);
                durationDisplay.textContent = formatTime(snippetEnd.value);
            }, { once: true });
        } else {
            snippetSelector.classList.remove('active');
        }
    });
    
    // Update display when start slider changes
    snippetStart.addEventListener('input', function() {
        let startVal = parseFloat(this.value);
        let endVal = parseFloat(snippetEnd.value);
        
        // Prevent start from exceeding end
        if (startVal > endVal) {
            startVal = endVal;
            snippetStart.value = startVal;
        }
        
        musicStartTimeInput.value = startVal;
        startDisplay.textContent = formatTime(startVal);
        
        const duration = endVal - startVal;
        durationDisplay.textContent = formatTime(duration);
        selectedLength.textContent = formatTime(duration);
        
        // Update audio preview playback to start from selected position
        snippetAudio.currentTime = startVal;
    });
    
    // Update display when end slider changes
    snippetEnd.addEventListener('input', function() {
        let endVal = parseFloat(this.value);
        let startVal = parseFloat(snippetStart.value);
        
        // Prevent end from going below start
        if (endVal < startVal) {
            endVal = startVal;
            snippetEnd.value = endVal;
        }
        
        musicEndTimeInput.value = endVal;
        endDisplay.textContent = formatTime(endVal);
        
        const duration = endVal - startVal;
        durationDisplay.textContent = formatTime(duration);
        selectedLength.textContent = formatTime(duration);
    });
    
    // Auto-stop audio preview at end time
    snippetAudio.addEventListener('timeupdate', function() {
        const endVal = parseFloat(snippetEnd.value);
        if (this.currentTime >= endVal) {
            this.pause();
            this.currentTime = parseFloat(snippetStart.value);
        }
    });
})();
```

---

## 7. MESSAGE_DETAIL.HTML - VIDEO LOOP & VOLUME

### Video Element Update
```html
<!-- Video Preview with Loop and Volume Control -->
{% if message.video_clip %}
<div style="margin:20px 0; text-align:center;">
    <video id="messageVideo" loop style="max-width:100%; border-radius:8px; background: #000;" controlsList="nodownload">
        <source src="{{ message.video_clip.url }}" type="video/webm">
        <source src="{{ message.video_clip.url }}" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    <!-- Custom Video Volume Control -->
    <div style="margin-top: 12px; display: flex; align-items: center; justify-content: center; gap: 10px; background: rgba(255,255,255,0.1); padding: 8px 15px; border-radius: 20px; width: fit-content; margin-left: auto; margin-right: auto;">
        <span style="font-size: 18px; min-width: 25px;">🔊</span>
        <input type="range" id="videoVolume" min="0" max="100" value="100" style="width: 120px; cursor: pointer; accent-color: rgba(255,255,255,0.8);" title="Video Volume">
        <span id="volumePercent" style="font-size: 0.85em; min-width: 35px;">100%</span>
    </div>
</div>
<script>
    const videoElement = document.getElementById('messageVideo');
    const videoVolume = document.getElementById('videoVolume');
    const volumePercent = document.getElementById('volumePercent');
    
    if (videoVolume && videoElement) {
        videoVolume.addEventListener('input', function() {
            videoElement.volume = this.value / 100;
            volumePercent.textContent = this.value + '%';
        });
        
        // Initialize volume
        videoElement.volume = videoVolume.value / 100;
    }
</script>
{% endif %}
```

---

## 8. MESSAGE_DETAIL.HTML - SNIPPET INFO DISPLAY

### Snippet Information Display
```html
<!-- Display music snippet info if selected -->
{% if message.music_start_time != nil or message.music_end_time != nil %}
<div style="background: rgba(255,255,255,0.2); padding: 12px; border-radius: 8px; margin-bottom: 15px; font-size: 0.95em;">
    <strong>🎵 Song Snippet:</strong>
    {% if message.music_start_time %}Start: {{ message.music_start_time|floatformat:1 }}s{% endif %}
    {% if message.music_end_time %} — End: {{ message.music_end_time|floatformat:1 }}s{% endif %}
    {% if message.music_start_time and message.music_end_time %}<br><small>Duration: {{ message.music_end_time|add:"-1"|mul:message.music_start_time|floatformat:1 }}s</small>{% endif %}
</div>
{% endif %}
```

---

## 9. MESSAGE_DETAIL.HTML - SNIPPET PLAYBACK LOGIC

### Enhanced Music Player JavaScript
```javascript
<script>
    const audioPlayer = document.getElementById('audioPlayer');
    const playBtn = document.getElementById('playBtn');
    const muteBtn = document.getElementById('muteBtn');
    const volumeSlider = document.getElementById('volumeSlider');
    const volumeIcon = document.getElementById('volumeIcon');
    let isMuted = false;
    
    // Get song snippet data from template
    let snippetStart = null;
    let snippetEnd = null;
    
    // Check if song snippet info exists in the page
    const musicPlayerDiv = document.querySelector('.music-player');
    if (musicPlayerDiv) {
        const snippetInfoText = musicPlayerDiv.textContent;
        if (snippetInfoText.includes('Song Snippet')) {
            // Extract start and end times from the page content
            const startMatch = snippetInfoText.match(/Start: ([\d.]+)s/);
            const endMatch = snippetInfoText.match(/End: ([\d.]+)s/);
            if (startMatch) snippetStart = parseFloat(startMatch[1]);
            if (endMatch) snippetEnd = parseFloat(endMatch[1]);
        }
    }
    
    // ... [existing code] ...
    
    playBtn.addEventListener('click', function(e) {
        e.preventDefault();
        if (!audioPlayer) {
            console.error('No audio player');
            return;
        }
        
        console.log('Play clicked. Paused:', audioPlayer.paused);
        
        // If song snippet is selected, start from snippet start time
        if (audioPlayer.paused && snippetStart !== null) {
            audioPlayer.currentTime = snippetStart;
        }
        
        // ... [rest of existing play logic] ...
    });
    
    // Handle song snippet - stop at end time
    audioPlayer.addEventListener('timeupdate', function() {
        if (snippetEnd !== null && this.currentTime >= snippetEnd) {
            this.pause();
            this.currentTime = snippetStart !== null ? snippetStart : 0;
            playBtn.textContent = '▶';
            playBtn.title = 'Play';
        }
    });
    
    // ... [rest of existing code] ...
</script>
```

---

## Key Implementation Points 🎯

1. **Hidden Form Fields:** Store exact times in database
2. **Range Sliders:** Prevent invalid selections (start > end)
3. **Real-time Validation:** Synchronize both sliders
4. **Time Formatting:** Convert seconds to MM:SS display
5. **Preview Audio:** Load on demand, stop at boundary
6. **Playback Control:** Jump to start, stop at end
7. **Database Fields:** Store as FloatField for precision
8. **CSS Styling:** Match project's purple theme

---

## Testing Code Snippets 🧪

### Test Creating Message with Snippet
```python
from homepage.models import UnsentMessage

msg = UnsentMessage(
    sender_name="Test User",
    receiver_name="Test Recipient",
    message_content="Test message",
    preset_music="song.mp3",
    music_start_time=15.0,
    music_end_time=105.0
)
msg.save()

# Verify
assert msg.music_start_time == 15.0
assert msg.music_end_time == 105.0
assert msg.get_music_snippet_data()['duration'] == 90.0
```

### Test Database Schema
```bash
python manage.py dbshell
SELECT music_start_time, music_end_time FROM homepage_unsentmessage WHERE id = 1;
```

### Test Migration
```bash
python manage.py migrate
python manage.py showmigrations
```


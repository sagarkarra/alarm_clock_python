# ⏰ Alarm Clock Using Python Tkinter

## Overview

The Alarm Clock is a simple desktop application built using Python and the Tkinter library. It allows users to set an alarm by selecting the desired hour, minute, and second. When the current system time matches the selected alarm time, the application plays an alarm sound.

This project demonstrates the use of GUI development, multithreading, and date-time management in Python.

---

## Features

- Simple and user-friendly graphical interface
- Set alarm time using dropdown menus
- Real-time alarm monitoring
- Automatic alarm sound playback
- Multithreading support for smooth GUI performance

---

## Technologies Used

- Python 3
- Tkinter
- ttk Widgets
- Datetime Module
- Time Module
- Threading Module
- Winsound Module
- Pillow (PIL)

---

## Project Structure

```text
Alarm-Clock/
│
├── main.py          # Main application file
├── icon.png         # Application icon
└── README.md        # Project documentation

---

## Requirements

Make sure the following are installed before running the project:

- Python 3.x
- Pillow Library

Install Pillow using:

```bash
pip install pillow
```

---

## How to Run

1. Download or clone the repository.
2. Ensure the following files are present in the project directory:
   - `main.py`
   - `icon.png`
3. Open a terminal or command prompt in the project folder.
4. Run the application:

```bash
python main.py
```

---

## Working Procedure

1. Start the application.
2. Select the desired:
   - Hour
   - Minute
   - Second
3. Click the **Set Alarm** button.
4. The application continuously checks the current system time.
5. When the selected alarm time matches the current time, the alarm sound is played.

---

## Learning Outcomes

This project helps in understanding:

- GUI Development using Tkinter
- Event Handling in Python
- Multithreading Concepts
- Date and Time Operations
- Audio Playback in Python
- Usage of Combobox Widgets

---

## Future Enhancements

- Add Snooze functionality
- Add Stop Alarm button
- Display a live digital clock
- Support multiple alarms
- Allow custom alarm tones
- Improve AM/PM support
- Add cross-platform audio compatibility

---

## Known Limitations

- The application uses the `winsound` module, which is supported only on Windows.
- AM/PM functionality may not be fully implemented.
- The hour selection may include `24`, while valid 24-hour format ranges from `00` to `23`.

---

## Conclusion

The Alarm Clock project is a beginner-friendly Python application that demonstrates the fundamentals of GUI programming using Tkinter. It combines threading and time management concepts to create a practical and useful desktop utility.

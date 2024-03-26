import time
import threading
import keyboard
import matplotlib.pyplot as plt

class KeyloggerDetector:
    def __init__(self):
        self.detected = False
        self.keystrokes = {'normal': [], 'suspicious': []}

    def detect_keylogger(self):
        while not self.detected:
            for event in keyboard.record():
                if event.event_type == keyboard.KEY_DOWN:
                    key = event.name
                    if self.is_potential_keylogger(key):
                        self.detected = True
                        self.notify_user()
                        break
                    else:
                        self.keystrokes['normal'].append(key)
                else:
                    self.keystrokes['normal'].append(event.name)

    def is_potential_keylogger(self, key):
        if len(key) > 1:
            return True
        return False

    def notify_user(self):
        print("Potential keylogger detected!")
        self.plot_keystrokes()

    def plot_keystrokes(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.keystrokes['normal'], label='Normal Keystrokes')
        plt.plot(self.keystrokes['suspicious'], 'ro', label='Suspicious Keystrokes')
        plt.title('Keylogger Detection')
        plt.xlabel('Time')
        plt.ylabel('Key Pressed')
        plt.legend()
        plt.savefig('keylogger_detection_plot.png')  # Save plot as image
        plt.show()

    def start_detection(self):
        detection_thread = threading.Thread(target=self.detect_keylogger)
        detection_thread.start()

if __name__ == "__main__":
    detector = KeyloggerDetector()
    detector.start_detection()

    # Keep the program running indefinitely
    while True:
        time.sleep(1)

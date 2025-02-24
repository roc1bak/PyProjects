import tkinter as tk  # Import tkinter for GUI
import speedtest  # Import speedtest-cli for internet speed test

# Function to get the speed and display it in the GUI
def test_speed():
    st = speedtest.Speedtest()  # Initialize Speedtest object
    st.get_best_server()  # Get the best server based on ping
    download_speed = st.download() / 1_000_000  # Convert download speed to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert upload speed to Mbps
    ping = st.results.ping  # Get ping value
    
    # Update the labels with the results
    download_label.config(text=f"Download Speed: {download_speed:.2f} Mbps")
    upload_label.config(text=f"Upload Speed: {upload_speed:.2f} Mbps")
    ping_label.config(text=f"Ping: {ping} ms")

# Create the main window
root = tk.Tk()  # Initialize the window
root.title("Internet Speed Test")  # Set window title

# Create and pack labels to display the results
download_label = tk.Label(root, text="Download Speed: Not Tested", font=("Arial", 14))  # Download speed label
download_label.pack(pady=10)  # Add label to window

upload_label = tk.Label(root, text="Upload Speed: Not Tested", font=("Arial", 14))  # Upload speed label
upload_label.pack(pady=10)  # Add label to window

ping_label = tk.Label(root, text="Ping: Not Tested", font=("Arial", 14))  # Ping label
ping_label.pack(pady=10)  # Add label to window

# Button to trigger the speed test
test_button = tk.Button(root, text="Test Speed", command=test_speed, font=("Arial", 14))  # Speed test button
test_button.pack(pady=20)  # Add button to window

# Run the tkinter event loop
root.mainloop()  # Start the GUI loop
 

 #Warning, it takes a while to work, do not interfere while it is running the test.
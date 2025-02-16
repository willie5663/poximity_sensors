def clear_log():
    with open('scan_log.csv', 'w') as csvfile:  # Open in write mode (this clears the file)
        csvfile.write('')  # Write nothing, effectively erasing contents
    print("Log file cleared.")

# Run the function
clear_log()

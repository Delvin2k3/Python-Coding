import time

# Start the timer
start_time = time.time()

chunk_size = 1000  # Number of repetitions per chunk
total_repetitions = 1000000  # Total number of repetitions 

for _ in range(total_repetitions // chunk_size):
    print('xoxo \n' * chunk_size, end='')

# Print the remaining repetitions if total_repetitions is not a multiple of chunk_size
remaining_repetitions = total_repetitions % chunk_size
if remaining_repetitions > 0:
    print('xoxo \n' * remaining_repetitions, end='')

# End the timer
end_time = time.time()

# Calculate and print the elapsed time
elapsed_time = end_time - start_time
print(f"\nTime taken for execution: {elapsed_time} seconds")
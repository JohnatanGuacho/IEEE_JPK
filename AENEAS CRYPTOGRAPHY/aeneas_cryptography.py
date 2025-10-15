import math
import sys

def myFunction():
    try:
        input_data = sys.stdin.read().split()
    except:
        print(0)
        return

    if not input_data:
        print(0)
        return
    
    try:
        R = float(input_data[0])
    except (IndexError, ValueError):
        print(0)
        return

    angle_map = {}
    angle_tokens_end = 1 + 2 * 26
    
    for i in range(1, angle_tokens_end, 2):
        if i + 1 < len(input_data):
            letter_token = input_data[i]
            angle_token = input_data[i+1]
            try:
                angle_map[letter_token] = float(angle_token)
            except ValueError:
                angle_tokens_end = i 
                break
        else:
            angle_tokens_end = i
            break

    raw_message_tokens = input_data[angle_tokens_end:]
    processed_message = []
    last_letter = None
    for token in raw_message_tokens:
        for char in token:
            upper_char = char.upper()
            if upper_char in angle_map:
                if upper_char != last_letter:
                    processed_message.append(upper_char)
                    last_letter = upper_char

    if not processed_message:
        print(0)
        return
    
    total_length = 0.0
    total_length += R
    current_angle = angle_map[processed_message[0]]
    for i in range(1, len(processed_message)):
        next_angle = angle_map[processed_message[i]]
        theta = abs(current_angle - next_angle)
        central_angle_degrees = min(theta, 360.0 - theta)
        half_central_angle_degrees = central_angle_degrees / 2.0
        half_central_angle_radians = math.radians(half_central_angle_degrees)
        distance = 2.0 * R * math.sin(half_central_angle_radians)
        total_length += distance 
        current_angle = next_angle

    result = math.ceil(total_length)
    print(int(result))


if __name__ == "__main__":
    myFunction()
